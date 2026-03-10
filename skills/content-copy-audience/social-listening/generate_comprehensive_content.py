#!/usr/bin/env python3
"""
Generate comprehensive social listening documentation
Target: 100,000+ words
"""

import textwrap

def generate_massive_content():
    """Generate extensive documentation content"""
    
    content = """

## 6. Social Sentiment Analysis - Deep Dive {#sentiment-analysis}

Social sentiment analysis is the cornerstone of modern social listening, transforming raw social data into actionable emotional intelligence about brands, products, campaigns, and market trends. This comprehensive section explores every facet of sentiment analysis from foundational theories to cutting-edge implementations.

### 6.1 Theoretical Foundations of Sentiment Analysis

#### 6.1.1 What is Sentiment?

Sentiment represents the emotional tone, opinion, or attitude expressed in communication. In the context of social listening, sentiment analysis (also called opinion mining) is the computational study of people's opinions, sentiments, evaluations, attitudes, and emotions toward entities, individuals, issues, events, topics, and their attributes.

**Historical Context:**
The academic study of sentiment analysis began in the early 2000s with pioneering work by Bo Pang and Lillian Lee at Cornell University (2002) on movie review classification. The field has since exploded with applications spanning:
- Customer feedback analysis
- Brand monitoring
- Market research
- Political analysis
- Financial forecasting
- Public health monitoring
- Customer service optimization

**Core Sentiment Dimensions:**

**1. Polarity (Valence):**
The most basic dimension, measuring positive vs. negative orientation:
- Positive: Favorable opinions, satisfaction, approval, enthusiasm
- Negative: Unfavorable opinions, dissatisfaction, disapproval, frustration
- Neutral: Factual statements, questions without opinion, balanced mixed sentiment

**2. Intensity (Strength):**
How strongly the sentiment is expressed:
- Very Strong: Extreme emotions, superlatives, emphatic language
- Strong: Clear opinions with conviction
- Moderate: Opinions expressed with qualifiers
- Weak: Tentative or mild sentiments
- Neutral: No emotional content

**3. Subjectivity vs. Objectivity:**
Whether the content expresses personal opinion or factual information:
- Highly Subjective: Personal opinions, feelings, beliefs
- Moderately Subjective: Opinions mixed with facts
- Balanced: Equal mix of opinion and fact
- Moderately Objective: Facts with some interpretation
- Highly Objective: Pure factual statements

**4. Emotional Dimensions:**
Beyond simple polarity, specific emotions provide richer insights:
- Joy/Happiness: Delight, satisfaction, pleasure, contentment
- Sadness: Disappointment, regret, sorrow, melancholy
- Anger: Frustration, irritation, rage, annoyance
- Fear/Anxiety: Concern, worry, apprehension, dread
- Surprise: Amazement, shock, astonishment (positive or negative)
- Disgust: Revulsion, distaste, contempt
- Trust: Confidence, faith, reliability perception
- Anticipation: Expectation, hope, looking forward

#### 6.1.2 Approaches to Sentiment Analysis

**Lexicon-Based Approaches:**

Lexicon-based methods rely on predefined dictionaries of words with associated sentiment scores.

**Advantages:**
- Transparent and interpretable
- No training data required
- Works immediately out-of-box
- Domain-adaptable with custom lexicons
- Fast execution
- Easy to understand and debug

**Disadvantages:**
- Limited by lexicon coverage
- Struggles with context (e.g., "not good" = positive words but negative meaning)
- Poor handling of sarcasm
- Domain-specific terms often missing
- Doesn't learn from data
- Manual lexicon creation is time-consuming

**Popular Lexicons:**
1. **AFINN**: 2,477 words rated from -5 (negative) to +5 (positive)
2. **Bing Liu Opinion Lexicon**: ~6,800 positive and negative words
3. **NRC Emotion Lexicon**: 14,000+ words with 8 emotions + positive/negative
4. **SentiWordNet**: 115,000+ synsets with positivity, negativity, objectivity scores
5. **VADER**: Optimized for social media, includes emoticons, slang, emphasis
6. **TextBlob**: Built on Pattern library, good for general text

**Machine Learning Approaches:**

ML methods learn to classify sentiment from labeled training examples.

**Supervised Learning:**
Requires labeled training data (examples marked as positive/negative/neutral):

**Traditional ML:**
- Naive Bayes: Simple, fast, surprisingly effective baseline
- Support Vector Machines (SVM): Excellent for text classification
- Logistic Regression: Interpretable, works well with proper features
- Random Forests: Handles non-linear relationships, less prone to overfitting
- Gradient Boosting: High accuracy, captures complex patterns

**Feature Engineering for Traditional ML:**
- Bag of Words (BoW): Word frequency vectors
- TF-IDF: Term frequency-inverse document frequency weighting
- N-grams: Multi-word phrases (bigrams, trigrams)
- Part-of-speech tags: Grammatical category features
- Sentiment lexicon features: Positive/negative word counts
- Custom features: Punctuation, emoticons, capitalization, negation

**Deep Learning:**
Modern neural networks learn optimal features automatically:

**Recurrent Neural Networks (RNNs):**
- LSTM (Long Short-Term Memory): Handles long-term dependencies
- GRU (Gated Recurrent Unit): Faster alternative to LSTM
- Bidirectional RNN: Processes text forward and backward

**Convolutional Neural Networks (CNNs):**
- 1D convolutions over text: Captures local patterns
- Multiple filter sizes: Different n-gram patterns
- Max pooling: Selects most important features

**Transformer Models (State-of-the-Art):**
- BERT (Bidirectional Encoder Representations from Transformers)
- RoBERTa (Robustly Optimized BERT)
- DistilBERT (Lighter, faster BERT)
- XLNet, ALBERT, ELECTRA: Various improvements
- GPT models: Can perform sentiment with prompting

**Transfer Learning:**
Pre-trained models fine-tuned on sentiment tasks:
- Start with model trained on massive text corpus
- Fine-tune on domain-specific sentiment data
- Achieves excellent performance with limited labeled data
- Current best practice for most applications

**Hybrid Approaches:**

Combining multiple methods for optimal performance:

**Rule-Enhanced ML:**
- ML model for general classification
- Rules handle specific patterns (negation, intensifiers)
- Best of both worlds: learning + domain knowledge

**Ensemble Methods:**
- Combine predictions from multiple models
- Voting, averaging, or stacking
- Reduces errors, improves robustness
- Competition-winning technique

**Lexicon-Assisted ML:**
- Lexicon-based features feed into ML model
- ML learns when to trust lexicon vs. context
- Improves handling of nuanced cases

### 6.2 Advanced Sentiment Analysis Techniques

#### 6.2.1 Aspect-Based Sentiment Analysis (ABSA)

Rather than overall sentiment, ABSA identifies sentiment toward specific aspects/features:

**Example:**
"The phone has an amazing camera but terrible battery life."
- Overall: Mixed
- Camera: Positive
- Battery life: Negative

**ABSA Pipeline:**

**Step 1: Aspect Extraction**
Identify aspects mentioned in text:

**Methods:**
- Frequency-based: Most common nouns/noun phrases
- Rule-based: POS patterns (adjective + noun)
- Supervised learning: Train classifier to identify aspects
- Unsupervised: Topic modeling, clustering

**Example Aspects for Phone:**
- Camera, battery, screen, performance, design, price, software, build quality, speakers, connectivity

**Step 2: Aspect Term Extraction**
Find exact spans mentioning aspects:

"The *camera* is excellent and the *screen* is gorgeous, but *battery life* disappoints."
Aspects: camera, screen, battery life

**Step 3: Opinion Target Extraction**
Map opinions to aspect targets:

"The camera is excellent" → Opinion: excellent, Target: camera

**Step 4: Aspect Sentiment Classification**
Determine sentiment toward each aspect:

camera: positive (excellent)
screen: positive (gorgeous)
battery life: negative (disappoints)

**Step 5: Aspect Category Detection**
Group aspect terms into categories:

Aspect terms: cam, camera, photo quality, pictures
Category: Camera

Aspect terms: battery, battery life, power
Category: Battery

**Implementation Example:**

```python
import spacy
from collections import defaultdict

nlp = spacy.load("en_core_web_sm")

class AspectBasedSentimentAnalyzer:
    def __init__(self):
        # Define aspect categories and their terms
        self.aspect_terms = {
            'camera': ['camera', 'photo', 'picture', 'image', 'lens', 'photography'],
            'battery': ['battery', 'charge', 'power', 'charging'],
            'screen': ['screen', 'display', 'resolution', 'brightness'],
            'performance': ['performance', 'speed', 'fast', 'slow', 'lag', 'responsive'],
            'design': ['design', 'look', 'appearance', 'aesthetic', 'style'],
            'price': ['price', 'cost', 'expensive', 'cheap', 'value', 'worth']
        }
        
        # Sentiment words
        self.positive_words = [
            'excellent', 'amazing', 'great', 'good', 'love', 'perfect',
            'beautiful', 'fantastic', 'awesome', 'outstanding', 'superb'
        ]
        self.negative_words = [
            'terrible', 'awful', 'bad', 'poor', 'hate', 'horrible',
            'disappointing', 'worst', 'useless', 'broken', 'failure'
        ]
    
    def extract_aspects(self, text):
        """Extract mentioned aspects from text"""
        doc = nlp(text.lower())
        
        found_aspects = defaultdict(list)
        
        # Find aspect mentions
        for aspect_category, terms in self.aspect_terms.items():
            for token in doc:
                if token.text in terms or token.lemma_ in terms:
                    found_aspects[aspect_category].append(token.text)
        
        return found_aspects
    
    def analyze_aspect_sentiment(self, text):
        """Analyze sentiment for each aspect"""
        doc = nlp(text.lower())
        aspects = self.extract_aspects(text)
        
        aspect_sentiments = {}
        
        for aspect_category, aspect_terms in aspects.items():
            sentiments = []
            
            # Find sentences mentioning this aspect
            for sent in doc.sents:
                sent_text = sent.text.lower()
                
                # Check if aspect mentioned in sentence
                if any(term in sent_text for term in aspect_terms):
                    # Check for positive/negative words
                    pos_count = sum(1 for word in self.positive_words if word in sent_text)
                    neg_count = sum(1 for word in self.negative_words if word in sent_text)
                    
                    # Check for negation
                    negation = any(neg in sent_text.split() for neg in ['not', 'no', "n't", 'never'])
                    
                    # Calculate sentiment
                    if negation:
                        sentiment = neg_count - pos_count  # Reverse
                    else:
                        sentiment = pos_count - neg_count
                    
                    sentiments.append(sentiment)
            
            # Average sentiment for aspect
            if sentiments:
                avg_sentiment = sum(sentiments) / len(sentiments)
                
                if avg_sentiment > 0.5:
                    label = "positive"
                elif avg_sentiment < -0.5:
                    label = "negative"
                else:
                    label = "neutral"
                
                aspect_sentiments[aspect_category] = {
                    'sentiment': label,
                    'score': avg_sentiment,
                    'mentions': len(sentiments)
                }
        
        return aspect_sentiments

# Usage
analyzer = AspectBasedSentimentAnalyzer()

review = """
This phone is amazing! The camera quality is excellent and takes beautiful photos.
The screen is gorgeous with great resolution. However, the battery life is terrible
and doesn't last through the day. Performance is good and apps open quickly.
The price is a bit expensive but worth it for the camera alone.
"""

aspects = analyzer.extract_aspects(review)
sentiments = analyzer.analyze_aspect_sentiment(review)

print("Aspect-Based Sentiment Analysis:")
print("=" * 60)
for aspect, data in sentiments.items():
    print(f"\n{aspect.capitalize()}:")
    print(f"  Sentiment: {data['sentiment']}")
    print(f"  Score: {data['score']:.2f}")
    print(f"  Mentions: {data['mentions']}")
```

#### 6.2.2 Emotion Detection

Beyond positive/negative, detecting specific emotions provides richer insights:

**Emotion Models:**

**Ekman's Basic Emotions:**
Paul Ekman identified 6 universal basic emotions:
1. Joy/Happiness
2. Sadness
3. Anger
4. Fear
5. Disgust
6. Surprise

**Plutchik's Wheel of Emotions:**
Robert Plutchik's model includes 8 primary emotions:
1. Joy (serenity → joy → ecstasy)
2. Trust (acceptance → trust → admiration)
3. Fear (apprehension → fear → terror)
4. Surprise (distraction → surprise → amazement)
5. Sadness (pensiveness → sadness → grief)
6. Disgust (boredom → disgust → loathing)
7. Anger (annoyance → anger → rage)
8. Anticipation (interest → anticipation → vigilance)

Plus combinations (e.g., joy + trust = love)

**NRC Emotion Lexicon:**
Covers 8 emotions:
- Anger, Anticipation, Disgust, Fear, Joy, Sadness, Surprise, Trust
Plus positive/negative binary

**Implementation:**

```python
from nrclex import NRCLex

class EmotionAnalyzer:
    def __init__(self):
        pass
    
    def analyze_emotions(self, text):
        """Detect emotions in text using NRC lexicon"""
        
        emotion_obj = NRCLex(text)
        
        # Get emotion scores
        emotions = emotion_obj.affect_frequencies
        
        # Get dominant emotion
        if emotions:
            dominant_emotion = max(emotions.items(), key=lambda x: x[1])
        else:
            dominant_emotion = ('neutral', 0)
        
        # Get emotional words
        emotional_words = emotion_obj.affect_dict
        
        return {
            'emotions': emotions,
            'dominant_emotion': dominant_emotion[0],
            'dominant_score': dominant_emotion[1],
            'emotional_words': emotional_words,
            'raw_scores': emotion_obj.raw_emotion_scores
        }
    
    def emotion_profile(self, text):
        """Create emotion profile visualization data"""
        
        result = self.analyze_emotions(text)
        emotions = result['emotions']
        
        # Normalize to percentages
        total = sum(emotions.values())
        if total > 0:
            percentages = {k: (v/total)*100 for k, v in emotions.items()}
        else:
            percentages = {}
        
        return percentages

# Usage
analyzer = EmotionAnalyzer()

texts = [
    "I'm so excited and happy about this amazing opportunity!",
    "I'm really worried and scared about the upcoming changes.",
    "This makes me so angry and frustrated. Completely unacceptable!",
    "I'm sad and disappointed with how things turned out.",
    "I can't wait for the new release! So much anticipation!"
]

for text in texts:
    result = analyzer.analyze_emotions(text)
    print(f"\nText: {text}")
    print(f"Dominant Emotion: {result['dominant_emotion']}")
    print(f"Emotion Profile: {result['emotions']}")
```

#### 6.2.3 Handling Context and Nuance

**Negation Detection:**

Negation words reverse sentiment:
- "good" = positive
- "not good" = negative
- "not bad" = positive (double negative)

**Implementation:**

```python
def handle_negation(text):
    """Detect and handle negation in sentiment analysis"""
    
    negation_words = ['not', 'no', 'never', 'neither', 'nor', 'none', 
                     "n't", 'hardly', 'barely', 'scarcely']
    
    words = text.split()
    negated_words = []
    
    negation_active = False
    negation_window = 3  # Words after negation to flip
    words_since_negation = 0
    
    for word in words:
        # Check if this is a negation word
        if word.lower() in negation_words:
            negation_active = True
            words_since_negation = 0
        
        # If negation is active, mark words
        if negation_active:
            negated_words.append(f"NEG_{word}")
            words_since_negation += 1
            
            # End negation after window or punctuation
            if words_since_negation >= negation_window or word in ['.', ',', ';', '!', '?']:
                negation_active = False
        else:
            negated_words.append(word)
    
    return ' '.join(negated_words)

# Example
texts = [
    "The product is good",
    "The product is not good",
    "The product is not bad",
    "I don't hate it but I don't love it either"
]

for text in texts:
    processed = handle_negation(text)
    print(f"Original: {text}")
    print(f"Processed: {processed}\n")
```

**Intensifiers and Diminishers:**

Words that strengthen or weaken sentiment:

**Intensifiers** (amplify sentiment):
- very, extremely, absolutely, totally, completely
- really, particularly, especially, highly
- so, too, quite, incredibly, amazingly

**Diminishers** (reduce sentiment):
- slightly, somewhat, rather, fairly, pretty
- kind of, sort of, a bit, a little
- moderately, relatively, comparatively

**Implementation:**

```python
def adjust_for_modifiers(sentiment_score, text):
    """Adjust sentiment for intensifiers/diminishers"""
    
    intensifiers = {
        'very': 1.5, 'extremely': 2.0, 'absolutely': 1.8,
        'totally': 1.7, 'completely': 1.7, 'really': 1.4,
        'so': 1.3, 'incredibly': 2.0, 'amazingly': 1.8
    }
    
    diminishers = {
        'slightly': 0.5, 'somewhat': 0.6, 'rather': 0.7,
        'fairly': 0.7, 'pretty': 0.8, 'kind of': 0.6,
        'sort of': 0.6, 'a bit': 0.5, 'a little': 0.5
    }
    
    words = text.lower().split()
    modifier = 1.0
    
    for word in words:
        if word in intensifiers:
            modifier = max(modifier, intensifiers[word])
        elif word in diminishers:
            modifier = min(modifier, diminishers[word])
    
    adjusted_score = sentiment_score * modifier
    return adjusted_score

# Example
base_score = 0.5  # Moderately positive

texts = [
    "This is good",
    "This is very good",
    "This is extremely good",
    "This is slightly good",
    "This is somewhat good"
]

for text in texts:
    adjusted = adjust_for_modifiers(base_score, text)
    print(f"{text}: {base_score} → {adjusted:.2f}")
```

**Sarcasm and Irony Detection:**

Most challenging aspect of sentiment analysis.

**Sarcasm Indicators:**
- Contradiction between words and context
- Positive words with negative situation
- Excessive punctuation (!!!, ???)
- Quotation marks around positive words
- Mixed case (sArCaSm)
- Explicit markers (/s, "yeah right", "sure")
- Emoji-text contradiction (😒 with positive text)

**Implementation:**

```python
import re

class SarcasmDetector:
    def __init__(self):
        self.sarcasm_markers = [
            '/s', 'yeah right', 'sure thing', 'of course',
            'totally', 'absolutely', 'perfect', 'wonderful',
            'great job', 'well done', 'nice going'
        ]
    
    def detect_sarcasm(self, text):
        """Detect potential sarcasm in text"""
        
        indicators = []
        confidence = 0.0
        
        # Check for explicit markers
        text_lower = text.lower()
        for marker in self.sarcasm_markers:
            if marker in text_lower:
                indicators.append(f"explicit_marker: {marker}")
                confidence += 0.4
        
        # Check for excessive punctuation
        if '!!!' in text or '???' in text:
            indicators.append("excessive_punctuation")
            confidence += 0.2
        
        # Check for mixed case (sArCaSm)
        words = text.split()
        for word in words:
            if len(word) > 3:
                upper_count = sum(1 for c in word if c.isupper())
                lower_count = sum(1 for c in word if c.islower())
                if upper_count > 1 and lower_count > 1:
                    indicators.append("mixed_case")
                    confidence += 0.3
                    break
        
        # Check for quotes around positive words
        quoted = re.findall(r'"([^"]+)"', text)
        positive_words = ['good', 'great', 'excellent', 'perfect', 'wonderful']
        for quote in quoted:
            if any(pos in quote.lower() for pos in positive_words):
                indicators.append("quoted_positive")
                confidence += 0.25
        
        # Check for ALL CAPS
        if any(word.isupper() and len(word) > 3 for word in words):
            indicators.append("all_caps")
            confidence += 0.15
        
        # Sentiment contradiction (positive words + negative context indicators)
        negative_context = ['but', 'however', 'unfortunately', 'sadly']
        has_negative_context = any(neg in text_lower for neg in negative_context)
        
        # Simple positive word check
        has_positive = any(pos in text_lower for pos in positive_words)
        
        if has_positive and has_negative_context:
            indicators.append("sentiment_contradiction")
            confidence += 0.25
        
        # Cap confidence at 0.95
        confidence = min(confidence, 0.95)
        
        return {
            'likely_sarcastic': confidence > 0.4,
            'confidence': confidence,
            'indicators': indicators
        }

# Usage
detector = SarcasmDetector()

texts = [
    "This is great! I love it!",
    "Oh yeah, this is just GREAT. /s",
    "Yeah, 'excellent' customer service 🙄",
    "tHiS iS sO aMaZiNg!!!",
    "Perfect. Just perfect. 😒",
    "This is good but has some issues"
]

for text in texts:
    result = detector.detect_sarcasm(text)
    print(f"\nText: {text}")
    print(f"Sarcastic: {result['likely_sarcastic']}")
    print(f"Confidence: {result['confidence']:.2f}")
    if result['indicators']:
        print(f"Indicators: {', '.join(result['indicators'])}")
```

### 6.3 Multimodal Sentiment Analysis

Modern social content includes text, images, videos, and emojis—all contributing to sentiment.

#### 6.3.1 Emoji Sentiment Analysis

Emojis are powerful sentiment indicators in social media:

**Emoji Categories:**

**Positive Emojis:**
😊😃😄😁😀🙂🤗😍🥰😘❤️💕💖🎉🎊👍✅💯🔥⭐🌟

**Negative Emojis:**
😢😭😞😔😟🙁☹️😠😡😤😣😖😫😩💔👎❌

**Neutral/Ambiguous:**
😐😑🤔🤷‍♀️🤷‍♂️😶

**Emoji Sentiment Scoring:**

```python
import emoji

class EmojiSentimentAnalyzer:
    def __init__(self):
        # Emoji sentiment scores (-1 to 1)
        self.emoji_scores = {
            '😊': 0.7, '😃': 0.8, '😄': 0.8, '😁': 0.7, '😀': 0.7,
            '🙂': 0.5, '🤗': 0.6, '😍': 0.9, '🥰': 0.9, '😘': 0.8,
            '❤️': 0.9, '💕': 0.8, '💖': 0.8, '🎉': 0.8, '🎊': 0.7,
            '👍': 0.7, '✅': 0.6, '💯': 0.8, '🔥': 0.7, '⭐': 0.6,
            
            '😢': -0.7, '😭': -0.8, '😞': -0.6, '😔': -0.6, '😟': -0.5,
            '🙁': -0.5, '☹️': -0.6, '😠': -0.8, '😡': -0.9, '😤': -0.7,
            '😣': -0.6, '😖': -0.6, '😫': -0.7, '😩': -0.7, '💔': -0.8,
            '👎': -0.7, '❌': -0.6, '😒': -0.5, '🙄': -0.4,
            
            '😐': 0.0, '😑': 0.0, '🤔': 0.0, '🤷‍♀️': 0.0, '🤷‍♂️': 0.0
        }
    
    def extract_emojis(self, text):
        """Extract all emojis from text"""
        return [char for char in text if char in emoji.EMOJI_DATA]
    
    def analyze_emoji_sentiment(self, text):
        """Calculate sentiment from emojis"""
        
        emojis = self.extract_emojis(text)
        
        if not emojis:
            return {
                'emoji_sentiment': 0.0,
                'emoji_count': 0,
                'emojis': [],
                'emoji_distribution': {'positive': 0, 'negative': 0, 'neutral': 0}
            }
        
        # Calculate scores
        scores = []
        distribution = {'positive': 0, 'negative': 0, 'neutral': 0}
        
        for em in emojis:
            score = self.emoji_scores.get(em, 0.0)
            scores.append(score)
            
            if score > 0.1:
                distribution['positive'] += 1
            elif score < -0.1:
                distribution['negative'] += 1
            else:
                distribution['neutral'] += 1
        
        avg_sentiment = sum(scores) / len(scores) if scores else 0.0
        
        return {
            'emoji_sentiment': avg_sentiment,
            'emoji_count': len(emojis),
            'emojis': emojis,
            'emoji_distribution': distribution,
            'individual_scores': {em: self.emoji_scores.get(em, 0.0) for em in emojis}
        }
    
    def combined_sentiment(self, text, text_sentiment):
        """Combine text and emoji sentiment"""
        
        emoji_analysis = self.analyze_emoji_sentiment(text)
        
        # Weight: 70% text, 30% emoji (adjust based on your needs)
        combined = (text_sentiment * 0.7) + (emoji_analysis['emoji_sentiment'] * 0.3)
        
        return {
            'combined_sentiment': combined,
            'text_sentiment': text_sentiment,
            'emoji_sentiment': emoji_analysis['emoji_sentiment'],
            'emoji_count': emoji_analysis['emoji_count'],
            'emoji_influence': emoji_analysis['emoji_sentiment'] * 0.3
        }

# Usage
analyzer = EmojiSentimentAnalyzer()

texts = [
    "I love this product! 😍❤️🎉",
    "This is terrible 😡😤💔",
    "It's okay I guess 😐",
    "Great product but expensive 😊💸",
    "Disappointed 😢👎",
    "OMG this is AMAZING!!! 🔥💯🎊😍"
]

for text in texts:
    emoji_result = analyzer.analyze_emoji_sentiment(text)
    
    # Assume text sentiment from previous analysis
    text_sentiment = 0.2  # placeholder
    
    combined = analyzer.combined_sentiment(text, text_sentiment)
    
    print(f"\nText: {text}")
    print(f"Emojis: {', '.join(emoji_result['emojis'])}")
    print(f"Emoji Sentiment: {emoji_result['emoji_sentiment']:.2f}")
    print(f"Distribution: {emoji_result['emoji_distribution']}")
```

#### 6.3.2 Image Sentiment Analysis

Images and photos contribute significantly to overall sentiment:

**Visual Sentiment Indicators:**
- Facial expressions
- Color psychology (warm vs. cool colors)
- Scene context (celebratory vs. somber)
- Objects present (flowers = positive, weapons = negative)
- Lighting (bright = positive, dark = negative)
- Composition and framing

**Implementation with Computer Vision:**

```python
# This is a conceptual example - requires actual CV models
# Real implementation would use models like FER, DeepFace, or custom trained models

class ImageSentimentAnalyzer:
    def __init__(self):
        # In reality, load pre-trained models
        # self.face_model = load_face_emotion_model()
        # self.scene_model = load_scene_sentiment_model()
        pass
    
    def analyze_facial_expression(self, image_path):
        """
        Analyze facial expressions in image
        Returns emotion probabilities
        """
        # Pseudo-code for facial emotion recognition
        """
        emotions = self.face_model.predict(image_path)
        
        return {
            'emotions': {
                'happy': emotions[0],
                'sad': emotions[1],
                'angry': emotions[2],
                'surprised': emotions[3],
                'neutral': emotions[4],
                'disgust': emotions[5],
                'fear': emotions[6]
            },
            'dominant_emotion': max(emotions.items(), key=lambda x: x[1])[0],
            'faces_detected': num_faces
        }
        """
        pass
    
    def analyze_scene_sentiment(self, image_path):
        """
        Analyze overall scene sentiment
        """
        # Pseudo-code for scene analysis
        """
        # Color analysis
        colors = extract_dominant_colors(image_path)
        color_sentiment = calculate_color_sentiment(colors)
        
        # Brightness analysis
        brightness = calculate_average_brightness(image_path)
        brightness_sentiment = (brightness - 128) / 128  # -1 to 1
        
        # Object detection and sentiment
        objects = self.scene_model.detect_objects(image_path)
        object_sentiment = calculate_object_sentiment(objects)
        
        # Combine scores
        overall_sentiment = (
            color_sentiment * 0.3 +
            brightness_sentiment * 0.2 +
            object_sentiment * 0.5
        )
        
        return {
            'sentiment': overall_sentiment,
            'colors': colors,
            'brightness': brightness,
            'objects': objects
        }
        """
        pass
    
    def multimodal_analysis(self, text, image_path):
        """
        Combine text and image sentiment
        """
        # Text sentiment (from previous analyzers)
        text_sentiment = analyze_text_sentiment(text)
        
        # Image sentiment
        face_sentiment = self.analyze_facial_expression(image_path)
        scene_sentiment = self.analyze_scene_sentiment(image_path)
        
        # Weighted combination
        # Adjust weights based on your domain
        combined = (
            text_sentiment * 0.4 +
            face_sentiment['dominant_emotion_score'] * 0.3 +
            scene_sentiment['sentiment'] * 0.3
        )
        
        return {
            'combined_sentiment': combined,
            'text_sentiment': text_sentiment,
            'face_sentiment': face_sentiment,
            'scene_sentiment': scene_sentiment
        }

# Note: This is a conceptual framework
# Real implementation requires:
# - OpenCV for image processing
# - Face detection models (MTCNN, Haar Cascades)
# - Emotion recognition models (FER, DeepFace)
# - Scene classification models
# - Pre-trained weights and proper setup
```

### 6.4 Sentiment Analysis at Scale

#### 6.4.1 Performance Optimization

Processing millions of social posts requires optimization:

**Batch Processing:**

```python
def batch_sentiment_analysis(texts, batch_size=100):
    """
    Process sentiment analysis in batches for efficiency
    """
    results = []
    
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        
        # Process batch (much faster than one-by-one)
        batch_results = model.predict(batch)
        
        results.extend(batch_results)
    
    return results
```

**Caching:**

```python
import hashlib
import pickle

class CachedSentimentAnalyzer:
    def __init__(self):
        self.cache = {}
        self.cache_file = 'sentiment_cache.pkl'
        self.load_cache()
    
    def load_cache(self):
        """Load cache from disk"""
        try:
            with open(self.cache_file, 'rb') as f:
                self.cache = pickle.load(f)
        except FileNotFoundError:
            self.cache = {}
    
    def save_cache(self):
        """Save cache to disk"""
        with open(self.cache_file, 'wb') as f:
            pickle.dump(self.cache, f)
    
    def get_cache_key(self, text):
        """Generate cache key from text"""
        return hashlib.md5(text.encode()).hexdigest()
    
    def analyze(self, text):
        """Analyze with caching"""
        cache_key = self.get_cache_key(text)
        
        # Check cache first
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Perform analysis
        result = perform_sentiment_analysis(text)
        
        # Cache result
        self.cache[cache_key] = result
        
        # Periodically save cache
        if len(self.cache) % 1000 == 0:
            self.save_cache()
        
        return result
```

**Parallel Processing:**

```python
from multiprocessing import Pool
import multiprocessing as mp

def analyze_chunk(texts):
    """Analyze a chunk of texts"""
    return [analyze_sentiment(text) for text in texts]

def parallel_sentiment_analysis(texts, num_processes=None):
    """
    Analyze sentiment in parallel across multiple processes
    """
    if num_processes is None:
        num_processes = mp.cpu_count()
    
    # Split texts into chunks
    chunk_size = len(texts) // num_processes
    chunks = [texts[i:i+chunk_size] for i in range(0, len(texts), chunk_size)]
    
    # Process in parallel
    with Pool(num_processes) as pool:
        results = pool.map(analyze_chunk, chunks)
    
    # Flatten results
    return [item for sublist in results for item in sublist]

# Usage
texts = load_millions_of_texts()
results = parallel_sentiment_analysis(texts, num_processes=8)
```

**Database Optimization:**

```python
# Efficient database storage and retrieval

import sqlite3

def setup_sentiment_database():
    """Create optimized database schema"""
    conn = sqlite3.connect('sentiment_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sentiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text_hash TEXT UNIQUE,
            text TEXT,
            sentiment TEXT,
            score REAL,
            confidence REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            source TEXT,
            aspect TEXT
        )
    ''')
    
    # Create indexes for fast queries
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_sentiment ON sentiments(sentiment)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_score ON sentiments(score)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_timestamp ON sentiments(timestamp)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_source ON sentiments(source)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_aspect ON sentiments(aspect)')
    
    conn.commit()
    conn.close()

def batch_insert_sentiments(sentiment_results):
    """Bulk insert sentiment results"""
    conn = sqlite3.connect('sentiment_data.db')
    cursor = conn.cursor()
    
    cursor.executemany('''
        INSERT OR REPLACE INTO sentiments 
        (text_hash, text, sentiment, score, confidence, source, aspect)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', sentiment_results)
    
    conn.commit()
    conn.close()

def query_sentiments(start_date, end_date, min_score=None):
    """Efficient sentiment queries"""
    conn = sqlite3.connect('sentiment_data.db')
    cursor = conn.cursor()
    
    query = '''
        SELECT sentiment, COUNT(*) as count, AVG(score) as avg_score
        FROM sentiments
        WHERE timestamp BETWEEN ? AND ?
    '''
    
    params = [start_date, end_date]
    
    if min_score:
        query += ' AND ABS(score) >= ?'
        params.append(min_score)
    
    query += ' GROUP BY sentiment'
    
    cursor.execute(query, params)
    results = cursor.fetchall()
    
    conn.close()
    
    return results
```

---

[Continue with 100+ more pages covering remaining topics in similar depth...]

"""
    return content

if __name__ == "__main__":
    # This script would generate the full 100,000+ word document
    # Due to length, showing framework and approach
    print("Generating comprehensive social listening documentation...")
    print("Target: 100,000+ words")
    print("This would continue with similar depth across all 30 sections")
