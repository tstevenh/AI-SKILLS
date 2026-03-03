#!/usr/bin/env python3
"""
IndexChex API client for checking and submitting URLs for indexing.
https://indexchex.com/api
"""

import sys
import json
import argparse
import urllib.request
import urllib.error
import os
import time
from datetime import datetime
from typing import List, Dict, Optional

BASE_URL = "https://indexchex.com/api/v1"

class IndexChexClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            'Authorization': api_key,
            'Content-Type': 'application/json',
            'User-Agent': 'BacklinkIndexer/1.0'
        }
    
    def _request(self, method: str, endpoint: str, data: dict = None) -> dict:
        """Make API request."""
        url = f"{BASE_URL}{endpoint}"
        
        if data:
            body = json.dumps(data).encode('utf-8')
        else:
            body = None
        
        req = urllib.request.Request(url, data=body, headers=self.headers, method=method)
        
        try:
            with urllib.request.urlopen(req, timeout=60) as response:
                return json.loads(response.read().decode())
        except urllib.error.HTTPError as e:
            error_body = e.read().decode()
            try:
                error_data = json.loads(error_body)
                raise Exception(f"API Error {e.code}: {error_data.get('message', error_body)}")
            except json.JSONDecodeError:
                raise Exception(f"API Error {e.code}: {error_body}")
    
    def get_balance(self) -> int:
        """Get current credit balance."""
        result = self._request('GET', '/balance')
        return result.get('balance', 0)
    
    def create_index_check(self, urls: List[str], name: str = None) -> dict:
        """Create an index check job."""
        data = {'urls': urls}
        if name:
            data['name'] = name
        return self._request('POST', '/index-check/jobs', data)
    
    def get_index_check_status(self, job_id: int) -> dict:
        """Get index check job status."""
        return self._request('GET', f'/index-check/jobs/{job_id}')
    
    def create_index_submit(self, urls: List[str], name: str = None) -> dict:
        """Create an index submit job."""
        data = {'urls': urls}
        if name:
            data['name'] = name
        return self._request('POST', '/index-submit/jobs', data)
    
    def get_index_submit_status(self, job_id: int) -> dict:
        """Get index submit job status."""
        return self._request('GET', f'/index-submit/jobs/{job_id}')
    
    def wait_for_job(self, job_id: int, job_type: str = 'check', 
                     poll_interval: int = 5, max_wait: int = 600) -> dict:
        """Poll job until complete."""
        start = time.time()
        
        while time.time() - start < max_wait:
            if job_type == 'check':
                status = self.get_index_check_status(job_id)
            else:
                status = self.get_index_submit_status(job_id)
            
            if status.get('status') in ['completed', 'failed']:
                return status
            
            progress = status.get('progress_percent', 0)
            print(f"  Progress: {progress}%", end='\r')
            
            time.sleep(poll_interval)
        
        raise Exception(f"Job {job_id} timed out after {max_wait}s")


def cmd_balance(client: IndexChexClient, args):
    """Check credit balance."""
    balance = client.get_balance()
    print(f"💰 IndexChex Balance: {balance:,} credits")


def cmd_check(client: IndexChexClient, args):
    """Check if URLs are indexed."""
    urls = collect_urls(args)
    if not urls:
        print("Error: No URLs provided")
        sys.exit(1)
    
    print(f"🔍 Checking {len(urls)} URLs for indexing status...")
    
    # Split into batches of 10,000
    results = []
    for i in range(0, len(urls), 10000):
        batch = urls[i:i+10000]
        batch_num = (i // 10000) + 1
        total_batches = (len(urls) + 9999) // 10000
        
        name = args.name or f"Index check {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        if total_batches > 1:
            name += f" (batch {batch_num}/{total_batches})"
        
        print(f"\n📤 Submitting batch {batch_num}/{total_batches} ({len(batch)} URLs)...")
        job = client.create_index_check(batch, name)
        job_id = job['job_id']
        print(f"   Job ID: {job_id}")
        
        if args.wait:
            print(f"   Waiting for completion...")
            result = client.wait_for_job(job_id, 'check', args.poll_interval)
            results.append(result)
            
            print(f"\n   ✅ Completed!")
            print(f"   Total: {result['total_urls']}")
            print(f"   Indexed: {result['indexed_count']} ({result['indexed_count']/result['total_urls']*100:.1f}%)")
            print(f"   Not Indexed: {result['not_indexed_count']}")
            if result.get('failed_count'):
                print(f"   Failed: {result['failed_count']}")
        else:
            results.append(job)
            print(f"   Status: {job['status']}")
            print(f"   Check status: indexchex.py status {job_id} --type check")
    
    # Summary
    if args.wait and results:
        print(f"\n{'='*50}")
        print("SUMMARY")
        print(f"{'='*50}")
        total_indexed = sum(r.get('indexed_count', 0) for r in results)
        total_not_indexed = sum(r.get('not_indexed_count', 0) for r in results)
        total_checked = sum(r.get('total_urls', 0) for r in results)
        print(f"Total URLs:    {total_checked}")
        print(f"Indexed:       {total_indexed} ({total_indexed/total_checked*100:.1f}%)")
        print(f"Not Indexed:   {total_not_indexed} ({total_not_indexed/total_checked*100:.1f}%)")
    
    # Output
    if args.output:
        with open(args.output, 'w') as f:
            json.dump({'jobs': results}, f, indent=2)
        print(f"\nResults saved to: {args.output}")


def cmd_submit(client: IndexChexClient, args):
    """Submit URLs for indexing."""
    urls = collect_urls(args)
    if not urls:
        print("Error: No URLs provided")
        sys.exit(1)
    
    print(f"📤 Submitting {len(urls)} URLs for indexing...")
    
    # Split into batches of 10,000
    results = []
    for i in range(0, len(urls), 10000):
        batch = urls[i:i+10000]
        batch_num = (i // 10000) + 1
        total_batches = (len(urls) + 9999) // 10000
        
        name = args.name or f"Index submit {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        if total_batches > 1:
            name += f" (batch {batch_num}/{total_batches})"
        
        print(f"\n📤 Submitting batch {batch_num}/{total_batches} ({len(batch)} URLs)...")
        job = client.create_index_submit(batch, name)
        job_id = job['job_id']
        print(f"   Job ID: {job_id}")
        
        if args.wait:
            print(f"   Waiting for completion...")
            result = client.wait_for_job(job_id, 'submit', args.poll_interval)
            results.append(result)
            
            print(f"\n   ✅ Completed!")
            print(f"   Total: {result['total_urls']}")
            print(f"   Successful: {result['successful_count']}")
            if result.get('failed_count'):
                print(f"   Failed: {result['failed_count']}")
        else:
            results.append(job)
            print(f"   Status: {job['status']}")
            print(f"   Check status: indexchex.py status {job_id} --type submit")
    
    # Output
    if args.output:
        with open(args.output, 'w') as f:
            json.dump({'jobs': results}, f, indent=2)
        print(f"\nResults saved to: {args.output}")


def cmd_status(client: IndexChexClient, args):
    """Check job status."""
    job_id = args.job_id
    
    if args.type == 'check':
        status = client.get_index_check_status(job_id)
        print(f"📊 Index Check Job #{job_id}")
        print(f"   Status: {status['status']}")
        print(f"   Progress: {status.get('progress_percent', 0)}%")
        print(f"   Total URLs: {status['total_urls']}")
        print(f"   Checked: {status.get('checked_urls', 0)}")
        print(f"   Indexed: {status.get('indexed_count', 0)}")
        print(f"   Not Indexed: {status.get('not_indexed_count', 0)}")
        if status.get('failed_count'):
            print(f"   Failed: {status['failed_count']}")
        if status.get('completed_at'):
            print(f"   Completed: {status['completed_at']}")
    else:
        status = client.get_index_submit_status(job_id)
        print(f"📊 Index Submit Job #{job_id}")
        print(f"   Status: {status['status']}")
        print(f"   Progress: {status.get('progress_percent', 0)}%")
        print(f"   Total URLs: {status['total_urls']}")
        print(f"   Submitted: {status.get('submitted_urls', 0)}")
        print(f"   Successful: {status.get('successful_count', 0)}")
        if status.get('failed_count'):
            print(f"   Failed: {status['failed_count']}")
        if status.get('completed_at'):
            print(f"   Completed: {status['completed_at']}")


def collect_urls(args) -> List[str]:
    """Collect URLs from args and file."""
    urls = list(args.urls) if hasattr(args, 'urls') and args.urls else []
    if hasattr(args, 'file') and args.file:
        with open(args.file) as f:
            urls.extend([line.strip() for line in f if line.strip() and not line.startswith('#')])
    return urls


def main():
    parser = argparse.ArgumentParser(description='IndexChex API client')
    parser.add_argument('-k', '--api-key', help='API key (or set INDEXCHEX_API_KEY env var)')
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Balance
    balance_parser = subparsers.add_parser('balance', help='Check credit balance')
    
    # Check
    check_parser = subparsers.add_parser('check', help='Check if URLs are indexed')
    check_parser.add_argument('urls', nargs='*', help='URLs to check')
    check_parser.add_argument('-f', '--file', help='File containing URLs')
    check_parser.add_argument('-n', '--name', help='Job name')
    check_parser.add_argument('-w', '--wait', action='store_true', help='Wait for completion')
    check_parser.add_argument('--poll-interval', type=int, default=5, help='Poll interval (seconds)')
    check_parser.add_argument('-o', '--output', help='Output JSON file')
    
    # Submit
    submit_parser = subparsers.add_parser('submit', help='Submit URLs for indexing')
    submit_parser.add_argument('urls', nargs='*', help='URLs to submit')
    submit_parser.add_argument('-f', '--file', help='File containing URLs')
    submit_parser.add_argument('-n', '--name', help='Job name')
    submit_parser.add_argument('-w', '--wait', action='store_true', help='Wait for completion')
    submit_parser.add_argument('--poll-interval', type=int, default=5, help='Poll interval (seconds)')
    submit_parser.add_argument('-o', '--output', help='Output JSON file')
    
    # Status
    status_parser = subparsers.add_parser('status', help='Check job status')
    status_parser.add_argument('job_id', type=int, help='Job ID')
    status_parser.add_argument('-t', '--type', choices=['check', 'submit'], default='check', help='Job type')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Get API key
    api_key = args.api_key or os.environ.get('INDEXCHEX_API_KEY')
    if not api_key:
        print("Error: No API key provided.")
        print("Set --api-key or INDEXCHEX_API_KEY env var")
        print("\nGet your API key at: https://indexchex.com/settings (API Access)")
        sys.exit(1)
    
    client = IndexChexClient(api_key)
    
    if args.command == 'balance':
        cmd_balance(client, args)
    elif args.command == 'check':
        cmd_check(client, args)
    elif args.command == 'submit':
        cmd_submit(client, args)
    elif args.command == 'status':
        cmd_status(client, args)


if __name__ == '__main__':
    main()
