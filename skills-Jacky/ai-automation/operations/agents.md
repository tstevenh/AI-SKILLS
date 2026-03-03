# AI Agents Deep Dive

> Complete guide to AI agents: what they are, how to build them, frameworks, and practical business applications.

---

## Table of Contents

1. [Understanding AI Agents](#understanding-ai-agents)
2. [Agent Architectures](#agent-architectures)
3. [Agent Frameworks](#agent-frameworks)
4. [Building Custom Agents](#building-custom-agents)
5. [Business Use Cases](#business-use-cases)
6. [Tools and Capabilities](#tools-and-capabilities)
7. [Safety and Control](#safety-and-control)
8. [Production Considerations](#production-considerations)

---

## Understanding AI Agents

### What is an AI Agent?

An AI agent is a system that can:

1. **Perceive** its environment (receive inputs)
2. **Reason** about what to do
3. **Act** using tools and APIs
4. **Learn** from feedback
5. **Persist** across interactions

### Agents vs Chatbots vs Automations

| Feature | Chatbot | Automation | Agent |
|---------|---------|------------|-------|
| Reasoning | Limited | None | Complex |
| Tool use | Few, predefined | Predefined | Dynamic |
| Autonomy | Low | None | High |
| Adaptability | Low | None | High |
| Multi-step | Limited | Hardcoded | Dynamic |
| Error recovery | Poor | Manual | Autonomous |

### The Agent Spectrum

```
Simple                                          Complex
──────────────────────────────────────────────────────────
Single-turn     Multi-turn      Tool-using      Autonomous
chatbot         assistant       agent           agent
                
"Answer this    "Remember       "Search web,    "Research
question"       context,        write code,     competitor,
                follow up"      run tests"      draft report,
                                                schedule review"
```

### Why Agents Now?

**Key enablers (2024-2026):**

1. **Better models** - GPT-4, Claude can reason reliably
2. **Function calling** - Structured tool use
3. **Longer context** - Track complex conversations
4. **Frameworks** - LangChain, CrewAI, etc.
5. **Infrastructure** - Vector DBs, observability

---

## Agent Architectures

### ReAct Pattern (Reasoning + Acting)

The foundational pattern:

```
THOUGHT → ACTION → OBSERVATION → repeat

Example:
User: "What's the weather in NYC and should I bring an umbrella?"

Agent:
THOUGHT: I need to check the NYC weather forecast
ACTION: weather_api.get_forecast(location="NYC")
OBSERVATION: {"temp": 65, "conditions": "rain", "chance": 80%}

THOUGHT: It's likely to rain, user should bring umbrella
ACTION: respond("It's 65°F in NYC with 80% chance of rain. 
         Yes, bring an umbrella!")
```

### Plan-and-Execute Pattern

For complex tasks:

```
1. PLAN: Break task into steps
2. EXECUTE: Run each step
3. VERIFY: Check results
4. ADJUST: Modify plan if needed

Example:
Task: "Analyze our competitor's pricing page"

PLAN:
1. Find competitor's website
2. Navigate to pricing page
3. Extract pricing tiers
4. Compare to our pricing
5. Summarize differences

EXECUTE:
Step 1: search_web("competitor pricing page")
Step 2: browse_url(competitor_pricing_url)
...
```

### Hierarchical Agents

Manager-worker architecture:

```
┌─────────────────────────────────┐
│         MANAGER AGENT           │
│  (Plans, delegates, combines)   │
└───────────────┬─────────────────┘
                │
    ┌───────────┼───────────┐
    │           │           │
    ▼           ▼           ▼
┌───────┐ ┌───────┐ ┌───────┐
│Research│ │Writer │ │Editor │
│ Agent │ │ Agent │ │ Agent │
└───────┘ └───────┘ └───────┘
```

### Multi-Agent Systems

Specialized agents collaborating:

```
User Request
     │
     ▼
┌─────────────┐     ┌─────────────┐
│   Router    │────▶│  Specialist │
│   Agent     │     │   Agent 1   │
└─────────────┘     └─────────────┘
     │
     ├────────────▶ ┌─────────────┐
     │              │  Specialist │
     │              │   Agent 2   │
     │              └─────────────┘
     │
     └────────────▶ ┌─────────────┐
                    │  Specialist │
                    │   Agent 3   │
                    └─────────────┘
```

---

## Agent Frameworks

### LangChain / LangGraph

**Best for:** Flexible agent building, complex chains

**Key Concepts:**
- Chains: Sequential operations
- Agents: Dynamic tool selection
- Tools: Functions the agent can use
- Memory: Conversation/state persistence

**Example:**
```python
from langchain.agents import create_react_agent
from langchain_anthropic import ChatAnthropic
from langchain.tools import tool

@tool
def search_web(query: str) -> str:
    """Search the web for information"""
    return search_api.search(query)

@tool
def calculate(expression: str) -> float:
    """Calculate a mathematical expression"""
    return eval(expression)  # Use proper parsing in production

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")

agent = create_react_agent(
    llm=llm,
    tools=[search_web, calculate],
    prompt=react_prompt
)
```

**LangGraph for Complex Flows:**
```python
from langgraph.graph import StateGraph

def research_node(state):
    # Do research
    return {"research": results}

def write_node(state):
    # Write based on research
    return {"draft": content}

def review_node(state):
    # Review the draft
    return {"feedback": review}

graph = StateGraph()
graph.add_node("research", research_node)
graph.add_node("write", write_node)
graph.add_node("review", review_node)

graph.add_edge("research", "write")
graph.add_edge("write", "review")
graph.add_conditional_edge("review", should_revise, {
    True: "write",
    False: END
})
```

### CrewAI

**Best for:** Multi-agent collaboration

```python
from crewai import Agent, Task, Crew

researcher = Agent(
    role="Research Analyst",
    goal="Find comprehensive information on topics",
    backstory="Expert at finding and synthesizing information",
    tools=[search_tool, scrape_tool]
)

writer = Agent(
    role="Content Writer",
    goal="Create engaging, informative content",
    backstory="Skilled writer who crafts compelling narratives",
    tools=[writing_tool]
)

research_task = Task(
    description="Research {topic} thoroughly",
    agent=researcher,
    expected_output="Comprehensive research brief"
)

writing_task = Task(
    description="Write article based on research",
    agent=writer,
    expected_output="Polished article",
    context=[research_task]  # Depends on research
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)

result = crew.kickoff(inputs={"topic": "AI automation trends"})
```

### AutoGen (Microsoft)

**Best for:** Conversational multi-agent systems

```python
from autogen import AssistantAgent, UserProxyAgent

assistant = AssistantAgent(
    name="assistant",
    llm_config={"model": "gpt-4"}
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    code_execution_config={"work_dir": "coding"}
)

user_proxy.initiate_chat(
    assistant,
    message="Write a Python script to analyze CSV data"
)
```

### OpenAI Assistants API

**Best for:** Managed agents with OpenAI

```python
from openai import OpenAI

client = OpenAI()

# Create assistant
assistant = client.beta.assistants.create(
    name="Data Analyst",
    instructions="You analyze data and create visualizations",
    tools=[
        {"type": "code_interpreter"},
        {"type": "retrieval"}
    ],
    model="gpt-4-turbo"
)

# Create thread and run
thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Analyze this sales data",
    file_ids=[file.id]
)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)
```

### Anthropic Computer Use

**Best for:** Full computer automation

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    tools=[
        {
            "type": "computer_20241022",
            "name": "computer",
            "display_width_px": 1024,
            "display_height_px": 768
        }
    ],
    messages=[{
        "role": "user",
        "content": "Open Chrome and search for AI news"
    }]
)
```

### Framework Comparison

| Framework | Best For | Complexity | Learning Curve |
|-----------|----------|------------|----------------|
| LangChain | Flexible chains | Medium | Medium |
| LangGraph | Complex flows | High | High |
| CrewAI | Multi-agent | Medium | Low |
| AutoGen | Conversations | Medium | Medium |
| OpenAI Assistants | Managed | Low | Low |
| Computer Use | Full automation | High | Medium |

---

## Building Custom Agents

### Basic Agent Structure

```python
class Agent:
    def __init__(self, llm, tools, system_prompt):
        self.llm = llm
        self.tools = {t.name: t for t in tools}
        self.system_prompt = system_prompt
        self.memory = []
    
    async def run(self, user_input: str, max_iterations: int = 10):
        self.memory.append({"role": "user", "content": user_input})
        
        for _ in range(max_iterations):
            # Get LLM response
            response = await self.llm.generate(
                system=self.system_prompt,
                messages=self.memory,
                tools=list(self.tools.values())
            )
            
            # Check if done
            if response.stop_reason == "end_turn":
                return response.content
            
            # Handle tool calls
            if response.tool_calls:
                for tool_call in response.tool_calls:
                    result = await self.execute_tool(tool_call)
                    self.memory.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result
                    })
            
            self.memory.append({
                "role": "assistant",
                "content": response.content
            })
        
        return "Max iterations reached"
    
    async def execute_tool(self, tool_call):
        tool = self.tools.get(tool_call.name)
        if not tool:
            return f"Error: Unknown tool {tool_call.name}"
        
        try:
            result = await tool.execute(tool_call.arguments)
            return str(result)
        except Exception as e:
            return f"Error executing {tool_call.name}: {e}"
```

### Tool Definition

```python
from dataclasses import dataclass
from typing import Callable, Any
import json

@dataclass
class Tool:
    name: str
    description: str
    parameters: dict
    function: Callable
    
    async def execute(self, arguments: dict) -> Any:
        return await self.function(**arguments)
    
    def to_schema(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "input_schema": {
                "type": "object",
                "properties": self.parameters,
                "required": list(self.parameters.keys())
            }
        }

# Example tools
search_tool = Tool(
    name="web_search",
    description="Search the web for information",
    parameters={
        "query": {
            "type": "string",
            "description": "The search query"
        }
    },
    function=lambda query: search_api.search(query)
)

email_tool = Tool(
    name="send_email",
    description="Send an email to someone",
    parameters={
        "to": {"type": "string", "description": "Recipient email"},
        "subject": {"type": "string", "description": "Email subject"},
        "body": {"type": "string", "description": "Email body"}
    },
    function=lambda to, subject, body: email_api.send(to, subject, body)
)
```

### Memory and State

```python
class AgentMemory:
    def __init__(self, max_messages: int = 100):
        self.messages = []
        self.max_messages = max_messages
        self.facts = {}  # Persistent facts
        self.working_memory = {}  # Current task state
    
    def add_message(self, role: str, content: str):
        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": time.time()
        })
        self._trim()
    
    def _trim(self):
        if len(self.messages) > self.max_messages:
            # Keep system message and recent messages
            self.messages = self.messages[:1] + self.messages[-self.max_messages+1:]
    
    def add_fact(self, key: str, value: Any):
        self.facts[key] = value
    
    def get_context(self) -> str:
        """Generate context summary for prompts"""
        context = []
        if self.facts:
            context.append("Known facts:")
            for k, v in self.facts.items():
                context.append(f"- {k}: {v}")
        if self.working_memory:
            context.append("\nCurrent task state:")
            for k, v in self.working_memory.items():
                context.append(f"- {k}: {v}")
        return "\n".join(context)
```

### Error Handling and Recovery

```python
class ResilientAgent(Agent):
    async def execute_tool(self, tool_call):
        tool = self.tools.get(tool_call.name)
        
        for attempt in range(3):  # Retry logic
            try:
                result = await tool.execute(tool_call.arguments)
                return str(result)
            except RateLimitError:
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
            except ValidationError as e:
                # Ask LLM to fix the input
                fixed = await self.fix_tool_input(tool_call, e)
                tool_call.arguments = fixed
            except Exception as e:
                return f"Error: {e}. Consider trying a different approach."
        
        return "Tool failed after 3 attempts"
    
    async def fix_tool_input(self, tool_call, error):
        prompt = f"""
        Tool call failed with error: {error}
        
        Tool: {tool_call.name}
        Arguments: {tool_call.arguments}
        
        Fix the arguments to be valid. Return only the corrected JSON.
        """
        response = await self.llm.generate(prompt)
        return json.loads(response)
```

---

## Business Use Cases

### 1. Research Agent

```python
research_agent = Agent(
    llm=claude,
    tools=[
        web_search,
        scrape_page,
        summarize_document,
        save_to_notion
    ],
    system_prompt="""
    You are a research agent. When given a topic:
    1. Search for relevant sources
    2. Scrape and read key pages
    3. Synthesize information
    4. Save findings to Notion
    
    Be thorough but focus on authoritative sources.
    """
)

# Usage
result = await research_agent.run(
    "Research the competitive landscape for AI automation tools"
)
```

### 2. Data Analysis Agent

```python
data_agent = Agent(
    llm=gpt4,
    tools=[
        read_csv,
        run_sql,
        create_chart,
        generate_insight
    ],
    system_prompt="""
    You are a data analysis agent. When given data questions:
    1. Understand what's being asked
    2. Query the data appropriately
    3. Analyze results
    4. Create visualizations
    5. Provide insights
    
    Always validate your assumptions with the data.
    """
)
```

### 3. Customer Success Agent

```python
cs_agent = Agent(
    llm=claude,
    tools=[
        get_customer_data,
        get_usage_stats,
        check_health_score,
        draft_email,
        schedule_call,
        create_task
    ],
    system_prompt="""
    You are a customer success agent. Monitor customer health:
    1. Check usage patterns
    2. Identify at-risk customers
    3. Draft personalized outreach
    4. Schedule check-ins
    5. Create follow-up tasks
    
    Be proactive but not intrusive.
    """
)
```

### 4. Content Operations Agent

```python
content_agent = Agent(
    llm=claude,
    tools=[
        get_content_calendar,
        research_topic,
        generate_outline,
        write_draft,
        schedule_publish,
        create_social_posts
    ],
    system_prompt="""
    You are a content operations agent. Manage the content pipeline:
    1. Check content calendar for upcoming needs
    2. Research topics
    3. Create outlines and drafts
    4. Schedule publishing
    5. Create social distribution
    
    Maintain brand voice and quality standards.
    """
)
```

### 5. Sales Development Agent

```python
sdr_agent = Agent(
    llm=claude,
    tools=[
        enrich_lead,
        research_company,
        personalize_email,
        add_to_sequence,
        update_crm,
        check_engagement
    ],
    system_prompt="""
    You are a sales development agent. For new leads:
    1. Enrich lead data
    2. Research the company
    3. Personalize outreach
    4. Add to appropriate sequence
    5. Monitor engagement
    
    Focus on quality over quantity.
    """
)
```

---

## Tools and Capabilities

### Common Tool Categories

```python
# Web/Research
web_search = Tool("web_search", "Search the internet")
scrape_page = Tool("scrape_page", "Extract content from URL")
fetch_api = Tool("fetch_api", "Make HTTP requests")

# Data
query_database = Tool("query_database", "Run SQL queries")
read_spreadsheet = Tool("read_spreadsheet", "Read Excel/CSV")
write_spreadsheet = Tool("write_spreadsheet", "Write to sheets")

# Communication
send_email = Tool("send_email", "Send emails")
send_slack = Tool("send_slack", "Post to Slack")
schedule_meeting = Tool("schedule_meeting", "Book calendar slot")

# File Operations
read_file = Tool("read_file", "Read file contents")
write_file = Tool("write_file", "Write to file")
create_document = Tool("create_document", "Create Google Doc")

# Integrations
create_task = Tool("create_task", "Create task in PM tool")
update_crm = Tool("update_crm", "Update CRM record")
trigger_workflow = Tool("trigger_workflow", "Start automation")
```

### Tool Composition

Combine simple tools into powerful capabilities:

```python
class ResearchCapability:
    """Composed capability for deep research"""
    
    def __init__(self, search_tool, scrape_tool, summarize_tool):
        self.search = search_tool
        self.scrape = scrape_tool
        self.summarize = summarize_tool
    
    async def deep_research(self, topic: str, depth: int = 5) -> dict:
        # Search for sources
        search_results = await self.search(topic)
        
        # Scrape top results
        contents = []
        for result in search_results[:depth]:
            content = await self.scrape(result.url)
            contents.append(content)
        
        # Summarize
        summary = await self.summarize("\n\n".join(contents))
        
        return {
            "sources": search_results[:depth],
            "summary": summary,
            "full_content": contents
        }
```

---

## Safety and Control

### Human-in-the-Loop

```python
class SupervisedAgent(Agent):
    def __init__(self, *args, require_approval_for=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.require_approval = require_approval_for or []
    
    async def execute_tool(self, tool_call):
        if tool_call.name in self.require_approval:
            approved = await self.request_approval(tool_call)
            if not approved:
                return "Action not approved by user"
        
        return await super().execute_tool(tool_call)
    
    async def request_approval(self, tool_call):
        print(f"Agent wants to: {tool_call.name}")
        print(f"With arguments: {tool_call.arguments}")
        response = input("Approve? (yes/no): ")
        return response.lower() == "yes"

# Usage
agent = SupervisedAgent(
    require_approval_for=["send_email", "update_crm", "schedule_meeting"]
)
```

### Guardrails

```python
class GuardedAgent(Agent):
    def __init__(self, *args, guardrails=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.guardrails = guardrails or []
    
    async def run(self, user_input: str, **kwargs):
        # Check input guardrails
        for guardrail in self.guardrails:
            if not await guardrail.check_input(user_input):
                return guardrail.rejection_message
        
        result = await super().run(user_input, **kwargs)
        
        # Check output guardrails
        for guardrail in self.guardrails:
            if not await guardrail.check_output(result):
                return guardrail.sanitize(result)
        
        return result

class Guardrail:
    async def check_input(self, input: str) -> bool:
        raise NotImplementedError
    
    async def check_output(self, output: str) -> bool:
        raise NotImplementedError

class PIIGuardrail(Guardrail):
    async def check_output(self, output: str) -> bool:
        # Check for PII in output
        return not contains_pii(output)
    
    def sanitize(self, output: str) -> str:
        return mask_pii(output)
```

### Action Limits

```python
class RateLimitedAgent(Agent):
    def __init__(self, *args, limits=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.limits = limits or {
            "send_email": 10,  # per hour
            "api_calls": 100,
            "cost": 1.00  # dollars
        }
        self.usage = {}
    
    async def execute_tool(self, tool_call):
        # Check limits
        current = self.usage.get(tool_call.name, 0)
        limit = self.limits.get(tool_call.name, float('inf'))
        
        if current >= limit:
            return f"Limit reached for {tool_call.name}"
        
        result = await super().execute_tool(tool_call)
        
        self.usage[tool_call.name] = current + 1
        return result
```

---

## Production Considerations

### Observability

```python
import logging
from opentelemetry import trace

tracer = trace.get_tracer("agent")

class ObservableAgent(Agent):
    async def run(self, user_input: str, **kwargs):
        with tracer.start_as_current_span("agent_run") as span:
            span.set_attribute("input", user_input[:100])
            
            try:
                result = await super().run(user_input, **kwargs)
                span.set_attribute("success", True)
                return result
            except Exception as e:
                span.set_attribute("error", str(e))
                span.record_exception(e)
                raise
    
    async def execute_tool(self, tool_call):
        with tracer.start_as_current_span(f"tool_{tool_call.name}"):
            logging.info(f"Executing tool: {tool_call.name}")
            return await super().execute_tool(tool_call)
```

### Cost Tracking

```python
class CostTrackedAgent(Agent):
    def __init__(self, *args, budget=10.0, **kwargs):
        super().__init__(*args, **kwargs)
        self.budget = budget
        self.spent = 0.0
    
    async def run(self, user_input: str, **kwargs):
        if self.spent >= self.budget:
            return "Budget exceeded"
        
        result = await super().run(user_input, **kwargs)
        
        # Track LLM cost
        self.spent += self.calculate_cost()
        
        return result
    
    def calculate_cost(self) -> float:
        # Estimate based on tokens
        tokens = sum(len(m["content"]) / 4 for m in self.memory)
        return tokens * 0.00003  # $0.03 per 1K tokens estimate
```

### Deployment Patterns

```yaml
# Agent as microservice
agent-service:
  image: agent:latest
  environment:
    - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    - REDIS_URL=redis://redis:6379
    - MAX_CONCURRENT=10
  ports:
    - "8080:8080"
  healthcheck:
    test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
  resources:
    limits:
      memory: 2G
      cpu: 1
```

---

## Summary

### When to Use Agents

✅ **Good fit:**
- Multi-step tasks with uncertainty
- Tasks requiring tool orchestration
- Dynamic decision-making needed
- Research and analysis
- Complex customer interactions

❌ **Not ideal:**
- Simple, deterministic tasks (use automations)
- Latency-critical applications
- Cost-sensitive high-volume tasks
- When predictability is critical

### Getting Started

1. **Start simple** - Single tool, single purpose
2. **Add tools incrementally** - Test each addition
3. **Build guardrails first** - Safety before capability
4. **Monitor everything** - Cost, latency, failures
5. **Human oversight** - Approve high-risk actions

### Recommended Stack

| Need | Tool |
|------|------|
| Simple agents | LangChain |
| Multi-agent | CrewAI |
| Complex flows | LangGraph |
| Managed | OpenAI Assistants |
| Computer control | Anthropic Computer Use |

See [../workflows/](../workflows/) for workflow automation templates →
