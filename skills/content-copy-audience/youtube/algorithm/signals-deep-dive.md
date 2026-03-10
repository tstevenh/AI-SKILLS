# Algorithm Signals Deep Dive

> A comprehensive breakdown of every signal YouTube uses to rank and recommend videos. Understanding these signals helps you optimize strategically rather than guessing.

## Table of Contents

1. [Click-Through Rate (CTR)](#click-through-rate-ctr)
2. [Average View Duration (AVD)](#average-view-duration-avd)
3. [Average Percentage Viewed (APV)](#average-percentage-viewed-apv)
4. [Likes, Comments, Shares, Saves](#likes-comments-shares-saves)
5. [Subscriber Conversion Rate](#subscriber-conversion-rate)
6. [Session Starts vs Session Ends](#session-starts-vs-session-ends)
7. [Re-watches and Loops](#re-watches-and-loops)
8. [Survey Satisfaction Signals](#survey-satisfaction-signals)
9. [Negative Signals](#negative-signals)
10. [Signal Interactions](#signal-interactions)

---

## Click-Through Rate (CTR)

### What CTR Measures

Click-through rate is the percentage of impressions that result in views. If 100 people see your video thumbnail and 5 click, your CTR is 5%.

```
CTR = (Clicks ÷ Impressions) × 100
```

### Why CTR Matters

CTR is the **gateway signal**. Without clicks, nothing else matters. You could have the most valuable content ever created, but if no one clicks, no one knows.

For YouTube's algorithm, CTR indicates:
- Thumbnail effectiveness
- Title appeal
- Topic interest
- Audience match quality

### CTR Benchmarks by Context

**Overall channel benchmarks**:
| Performance | CTR |
|-------------|-----|
| Poor | <2% |
| Below average | 2-4% |
| Average | 4-6% |
| Good | 6-8% |
| Excellent | 8-10% |
| Viral potential | 10%+ |

**Important context**: CTR varies dramatically by:
- **Traffic source**: Browse CTR is typically higher than search CTR
- **Impression pool**: Wider audiences = lower CTR (less targeted)
- **Video age**: New videos often have higher CTR (shown to subscribers first)
- **Topic**: Some niches have inherently higher/lower CTRs
- **Thumbnail quality relative to niche**: What counts as "good" varies

### CTR Dynamics Over Video Lifetime

**Day 1-3**: CTR is typically highest because YouTube shows to your most engaged viewers first.

**Week 1-2**: CTR drops as YouTube expands to broader audiences who don't know you.

**Month 1+**: CTR stabilizes at a natural level based on how well your content matches the audiences YouTube serves it to.

**Long-term**: Evergreen content may see CTR fluctuate based on search trends and suggested placement.

### The CTR-Impressions Relationship

Here's a critical insight many creators miss: **CTR and impressions are inversely related**.

When YouTube shows your video to more people (more impressions), CTR typically drops. Why? Because the broader audience is less targeted than your initial subscribers.

This means:
- High CTR + Low Impressions = Niche appeal
- Lower CTR + High Impressions = Broad appeal

A 5% CTR on 1 million impressions is far more valuable than 15% CTR on 10,000 impressions.

**What this means for optimization**: Don't panic when CTR drops as impressions increase. It's expected. Focus on the absolute number of views, not just the percentage.

### CTR by Traffic Source

Different traffic sources have different CTR benchmarks:

**Browse features (Homepage)**: 3-8%
- Viewers are browsing, less intent
- Thumbnail competition is high
- But massive volume

**Suggested videos**: 2-6%
- Viewers already watching something
- Your video needs to look like a good "next"
- Can be very high volume

**YouTube Search**: 2-4%
- Viewers have specific intent
- Relevance matters more than packaging
- Lower volume but more qualified

**External**: 1-3%
- Depends entirely on context
- Often lower because audience isn't in "YouTube mode"

**Notifications**: 10-20%+
- Highly engaged subscribers
- Low volume but valuable

### How to Improve CTR

**Thumbnail optimization** (see `thumbnails/` section):
- High contrast colors
- Expressive faces with emotion
- Clear, readable text (2-4 words max)
- Single focal point
- Works at small sizes

**Title optimization** (see `titles/` section):
- Curiosity without clickbait
- Clear value proposition
- Front-loaded keywords
- Specific and concrete
- 50-60 characters max

**Topic selection**:
- Match trending interests
- Solve problems people search for
- Cover topics your audience cares about
- Avoid oversaturated topics unless you have a unique angle

**Audience targeting**:
- Create for a specific viewer avatar
- Use niche-specific terminology
- Reference relevant cultural touchpoints
- Build on what's worked before

### CTR Myths Debunked

**Myth**: "Higher CTR is always better"
**Reality**: CTR must be balanced with impression volume. Optimizing only for CTR can shrink your audience.

**Myth**: "YouTube penalizes low CTR videos"
**Reality**: YouTube reduces impressions for low CTR, but it's not a penalty—it's optimization. Why show videos people don't click?

**Myth**: "CTR is the most important metric"
**Reality**: CTR × AVD together determine success. High CTR with low AVD (clickbait) hurts long-term.

**Myth**: "CTR should be consistent across all videos"
**Reality**: Different topics, audiences, and contexts lead to different CTRs. Compare within categories.

---

## Average View Duration (AVD)

### What AVD Measures

Average View Duration is the average amount of time viewers spend watching your video. If your video is 10 minutes long and viewers watch an average of 5 minutes, your AVD is 5 minutes.

### Why AVD Matters

AVD is YouTube's primary quality signal. It answers: "Did viewers actually want to watch this?"

For the algorithm, AVD indicates:
- Content quality
- Topic interest
- Pacing effectiveness
- Promise delivery
- Viewer satisfaction

### AVD vs Average Percentage Viewed

These are related but different:
- **AVD**: Absolute time watched (e.g., 5 minutes)
- **APV**: Percentage of video watched (e.g., 50%)

Which matters more? It depends:
- **Short videos**: APV matters more (a 2-minute video needs 80%+ watched)
- **Long videos**: AVD matters more (10 minutes watched on a 30-minute video is great)

YouTube values both, but tends to weight AVD for longer content and APV for shorter content.

### AVD Benchmarks

**Percentage watched benchmarks**:
| Performance | % Watched |
|-------------|-----------|
| Poor | <30% |
| Below average | 30-40% |
| Average | 40-50% |
| Good | 50-60% |
| Excellent | 60-70% |
| Outstanding | 70%+ |

**Absolute time benchmarks** (depends on video length):
| Video Length | Good AVD |
|--------------|----------|
| 2-5 minutes | 60-80% |
| 5-10 minutes | 50-70% |
| 10-20 minutes | 40-60% |
| 20-40 minutes | 30-50% |
| 40+ minutes | 25-40% |

### The AVD Breakdown

AVD is an average, which means it hides variation. Dig deeper with:

**Retention curve analysis**:
- Where do viewers drop off?
- Are there consistent patterns?
- What moments cause spikes or dips?

**Segment analysis**:
- Subscribers vs non-subscribers
- Traffic source segments
- Device type segments

**Temporal analysis**:
- First 24 hours vs first week vs long-term
- How does AVD change as audience broadens?

### Factors That Affect AVD

**Content factors**:
- Hook strength (first 30 seconds)
- Pacing (too slow or too fast)
- Value delivery timing
- Pattern interrupts
- Promise fulfillment
- Unnecessary tangents
- Natural video length for the topic

**Audience factors**:
- Viewer expertise level
- Time available
- Platform (mobile vs desktop)
- Context (at home vs commuting)

**Technical factors**:
- Video quality
- Audio quality
- Editing quality
- Thumbnail/title promise match

### How to Improve AVD

**Strengthen your hook** (see `retention/first-30-seconds.md`):
- Open with a pattern interrupt
- State the value immediately
- Preview what's coming
- Create curiosity loops

**Optimize pacing**:
- Cut ruthlessly (no filler)
- Add pattern interrupts every 20-30 seconds
- Vary shot types and B-roll
- Match energy to topic

**Deliver on promises**:
- If you teased something, deliver it
- Don't save the best for last (most won't make it)
- Front-load value

**Structure effectively** (see `retention/structure-templates.md`):
- Use proven structures
- Create "mini cliffhangers"
- Tease upcoming sections
- Use timestamps/chapters

**Match video length to content**:
- Don't pad videos to hit arbitrary lengths
- Respect viewer time
- End when the content ends

### The AVD-Video Length Debate

Should you make longer or shorter videos?

**Arguments for longer videos**:
- More total watch time
- More ad revenue potential
- Deeper content possible

**Arguments for shorter videos**:
- Higher percentage watched
- Easier to maintain quality
- Respects viewer time

**The right answer**: Make videos as long as they need to be. A video should be exactly the length required to deliver on its promise—no shorter, no longer.

The algorithm doesn't reward video length directly. It rewards watch time. A 5-minute video that 80% watch beats a 20-minute video that 15% watch.

---

## Average Percentage Viewed (APV)

### What APV Measures

Average Percentage Viewed tells you what portion of your video the average viewer watched. If your video is 10 minutes and APV is 45%, the average viewer watched 4.5 minutes.

### Why APV Matters

APV is particularly important for:
- Shorts (where 90%+ is common and expected)
- Short videos (under 5 minutes)
- Evaluating content quality relative to length
- Identifying retention issues

### APV Benchmarks

| Video Length | Target APV |
|--------------|------------|
| Shorts (<60s) | 85-100% |
| 1-3 minutes | 70-85% |
| 3-5 minutes | 60-75% |
| 5-10 minutes | 50-65% |
| 10-20 minutes | 40-55% |
| 20+ minutes | 30-45% |

### APV vs Total Watch Time

YouTube cares about both:
- **Total watch time** = Views × AVD
- **APV** = Quality signal per video

A video with 1 million views and 30% APV contributes 300,000 watch-minutes. A video with 100,000 views and 70% APV contributes less total but signals higher quality.

Both matter. Neither alone is sufficient.

### When APV Matters Most

1. **Short videos**: For a 2-minute video, going from 60% to 80% APV is significant
2. **Shorts**: Completion rate heavily impacts Shorts algorithm
3. **New channels**: Early videos need strong APV to establish trust
4. **Testing content**: APV helps evaluate quality independent of promotion

### How to Improve APV

Most APV improvements come from retention optimization (see `retention/` section). Key strategies:

1. **Eliminate drop-off points**: Find where viewers leave and fix those moments
2. **Tighten content**: Cut anything that doesn't serve the viewer
3. **Match promise to content**: Don't overpromise in thumbnail/title
4. **End strong**: Give viewers a reason to watch to the end
5. **Appropriate video length**: Don't stretch content

---

## Likes, Comments, Shares, Saves

### Likes

**What they indicate**: Approval, agreement, satisfaction

**Algorithm weight**: Medium. Likes are easy to give, so they're a weaker signal than actions requiring more effort.

**How to increase likes**:
- Ask for them (but not too early or too often)
- Create "like-worthy" moments (reveals, insights, jokes)
- Make viewers feel something
- Deliver value that warrants appreciation

**Like benchmarks**:
- Average: 3-5% like rate (likes ÷ views)
- Good: 5-8%
- Excellent: 8-12%
- Viral: 12%+

### Comments

**What they indicate**: Engagement depth, community, discussion-worthiness

**Algorithm weight**: High. Comments require effort, which signals genuine engagement.

**Comment quality matters**:
- Substantive comments > "nice video"
- Replies and conversations > single comments
- Questions and discussion > spam

**How to increase comments**:
- Ask specific questions (not "what do you think?")
- Create controversy or debate
- Encourage viewers to share their experience
- Reply to comments (especially early)
- Pin comments that encourage discussion
- Ask "which tip will you try first?"

**Comment benchmarks**:
- Average: 0.5-1% comment rate (comments ÷ views)
- Good: 1-3%
- Excellent: 3-5%
- Viral/controversial: 5%+

### Shares

**What they indicate**: Content worth recommending to others

**Algorithm weight**: Very high. Sharing means the viewer vouches for your content.

**Share platforms that matter**:
- WhatsApp/Messenger (private shares)
- Social media (Twitter, Facebook, Reddit)
- Email
- Discord/Slack
- Embeds on websites

**How to increase shares**:
- Create genuinely useful content
- Provoke strong reactions
- Make content that makes the sharer look good
- Include "did you know?" moments
- Create shareable formats (lists, facts, tutorials)

**Share benchmarks** (hard to measure accurately):
- Any measurable share rate indicates quality
- Viral videos often have 1-5% share rates

### Saves

**What they indicate**: Content worth returning to

**Algorithm weight**: Growing. Saves are a newer signal but increasingly important.

**Why saves matter**:
- Indicate lasting value
- Suggest reference-quality content
- Show intent to revisit

**How to increase saves**:
- Create resource content (tutorials, guides)
- Provide valuable information worth keeping
- Make "bookmark-worthy" content
- Create content people reference repeatedly

---

## Subscriber Conversion Rate

### What It Measures

Subscriber conversion rate measures what percentage of viewers subscribe to your channel after watching a video.

```
Sub Rate = (New Subscribers from Video ÷ Views) × 100
```

### Why It Matters

Subscriber conversion signals:
- Viewer wants more from you
- Content quality meets expectations
- Channel identity is clear
- Viewer-channel fit

### Subscriber Conversion Benchmarks

| Performance | Sub Rate |
|-------------|----------|
| Poor | <0.2% |
| Below average | 0.2-0.5% |
| Average | 0.5-1% |
| Good | 1-2% |
| Excellent | 2-4% |
| Outstanding | 4%+ |

### Factors Affecting Conversion

**Content factors**:
- Value delivered
- Unique perspective
- Series content (want more)
- Personality connection

**Channel factors**:
- Clear niche/identity
- Consistent quality
- Upload frequency
- Channel branding

**Call-to-action factors**:
- Asking for subscriptions (works!)
- Timing of the ask
- Reason given to subscribe
- Subscribe button/watermark

### How to Improve Subscriber Conversion

1. **Deliver exceptional value**: The best CTA is great content
2. **Create series content**: Give reasons to return
3. **Establish identity**: Make it clear what you're about
4. **Ask strategically**: Early in video (post-hook) or after major value delivery
5. **Give reasons**: "Subscribe for weekly tutorials on X"
6. **Use end screens**: Visual subscribe prompts
7. **Maintain consistency**: Regular uploads build anticipation

### The "Subscriber Value" Calculation

Not all subscribers are equal. YouTube values:
- Subscribers who watch (over those who don't)
- Subscribers who engage
- Subscribers who complete viewing sessions

Building subscribers who never watch can actually hurt your channel by reducing "subscriber view rate"—a metric YouTube tracks internally.

---

## Session Starts vs Session Ends

### Session Starts

A "session start" occurs when a viewer begins their YouTube session with your video. This means:
- They opened YouTube specifically for your content, or
- Your video was compelling enough to be the first thing they clicked

**Why session starts matter**:
- Indicates demand for your content
- Suggests strong packaging
- YouTube rewards videos that bring viewers to the platform

**How to get more session starts**:
- Strong thumbnail/title that pulls from external platforms
- Notification optimization
- Social media promotion
- Email newsletter links
- SEO for direct search intent

### Session Ends

A "session end" occurs when a viewer stops watching YouTube after your video. This can be:

**Positive session end**:
- Viewer watched multiple videos including yours
- Viewer left satisfied
- Session was substantial

**Negative session end**:
- Viewer clicked your video and immediately left
- Viewer was dissatisfied
- Your video ended an otherwise long session

### The Session Math

YouTube tracks whether your videos:
- **Extend sessions**: Viewers watch more after you
- **Are session-neutral**: Viewers' behavior varies
- **End sessions**: Viewers frequently leave after you

Videos that extend sessions get more recommendations. Videos that end sessions (negatively) get fewer.

### Optimizing for Sessions

**End screen optimization**:
- Link to relevant videos
- Create logical "next video" paths
- Use playlists

**Content optimization**:
- Leave viewers wanting more
- Create series content
- Reference other videos
- Don't exhaust viewers

**Avoid**:
- Clickbait that disappoints
- Content that makes viewers regret watching
- Unnecessary length that burns viewers out

---

## Re-watches and Loops

### Re-watch Signals

Re-watching indicates high value or entertainment. YouTube tracks:
- How often viewers re-watch your videos
- Which segments they re-watch
- Time between re-watches

**What re-watches signal**:
- Content is valuable enough to return to
- Specific segments have high utility
- Entertainment value sustains

### Loop Behavior

Loops are particularly relevant for:
- Shorts (where looping is common)
- Music videos
- Ambient/background content
- Short tutorials

**Loop metrics**:
- Loop rate (% who watch 2+ times)
- Average loops per viewer
- Total watch time including loops

### How to Encourage Re-watches

**For long-form**:
- Create reference content
- Include memorable moments
- Provide dense information
- Make it useful for specific tasks

**For Shorts**:
- Seamless loop points
- Satisfying endings that connect to beginnings
- Content that reveals more on re-watch
- Quick payoffs worth seeing again

---

## Survey Satisfaction Signals

### What YouTube Surveys

YouTube occasionally surveys viewers after watching videos, asking:
- How satisfied were you with this video? (1-5 stars)
- Why did you give this rating?
- Did this video match what you expected?

### How Surveys Affect Recommendations

Survey responses train YouTube's satisfaction prediction models:
1. Human raters provide explicit satisfaction scores
2. YouTube correlates these with behavioral signals
3. Models learn to predict satisfaction from behavior
4. These predictions influence recommendations

### What Drives High Survey Scores

Based on YouTube's own research:
- **Promise delivery**: Did the video match expectations?
- **Value provision**: Did the viewer learn or enjoy something?
- **Time well spent**: Does the viewer feel their time was respected?
- **Quality perception**: Was the production quality appropriate?

### Optimizing for Satisfaction

You can't control who gets surveyed or what they say, but you can:
1. Deliver on every promise
2. Respect viewer time
3. Provide genuine value
4. Avoid manipulation tactics
5. Create content you're proud of

---

## Negative Signals

### "Not Interested" Clicks

When viewers click "Not interested" on your video:
- Strong negative signal
- Reduces future recommendations to that viewer
- If pattern emerges, reduces recommendations broadly

**Why viewers click "Not interested"**:
- Misleading thumbnail/title
- Content not relevant to them
- Quality issues
- Topic aversion

### "Don't Recommend Channel"

Even stronger than "Not interested":
- Viewer actively blocks your channel
- Permanent reduction in recommendations to that viewer
- Signals potential channel-level issues if common

### Dislikes

Dislikes are a weaker negative signal than "Not interested":
- Some controversial content gets dislikes regardless of quality
- Dislikes often come from engaged viewers (they watched enough to form an opinion)
- Dislike ratio matters more than raw count

### Early Exits

Viewers who leave within:
- **0-10 seconds**: Extreme mismatch or quality issue
- **10-30 seconds**: Hook failure
- **30-60 seconds**: Content mismatch

Early exits signal to YouTube that your content doesn't satisfy the audience it's being shown to.

### How to Minimize Negative Signals

1. **Accurate thumbnails**: Show what's actually in the video
2. **Honest titles**: Deliver what you promise
3. **Strong hooks**: Give viewers reason to stay
4. **Quality foundations**: Good audio, good video, good editing
5. **Audience alignment**: Create for the right audience

---

## Signal Interactions

### The CTR × AVD Multiplication

The core recommendation formula can be simplified to:

```
Video Score ≈ CTR × AVD × Satisfaction Multiplier
```

This means:
- High CTR with low AVD = Clickbait (low score)
- Low CTR with high AVD = Hidden gem (medium score)
- High CTR with high AVD = Winner (high score)

### Signal Weights Over Time

**First 24 hours**: CTR weighted heavily
**First week**: AVD becomes equally important
**Long-term**: Satisfaction and session metrics dominate

### Context-Dependent Weighting

**Search traffic**: Relevance and AVD matter most
**Browse traffic**: CTR and session metrics matter most
**Suggested traffic**: Topical relevance and AVD matter most

### The Compounding Effect

Strong signals compound:
- High CTR → More impressions → More chances for watch time
- High AVD → Better recommendations → More impressions → Higher total watch time
- High satisfaction → Return viewers → Consistent performance → Channel authority

Weak signals also compound:
- Low CTR → Fewer impressions → Less data → Harder to improve
- Low AVD → Reduced recommendations → Fewer views → Lower total watch time

This is why struggling channels often stay stuck while successful channels grow faster—signals compound in both directions.

### The Feedback Loop

Understanding signal interactions helps you prioritize:

1. **First, get clicks** (CTR): Without clicks, nothing else matters
2. **Then, retain viewers** (AVD): Clicks without watch time hurt you
3. **Finally, satisfy** (Engagement): Watch time without satisfaction plateaus

Master them in order, because each depends on the previous.

---

*Next: Recent algorithm changes in `algorithm-changes.md`*
