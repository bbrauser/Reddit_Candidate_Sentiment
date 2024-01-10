# Importing necessary libraries
from textblob import TextBlob
from tqdm import tqdm

# Function to determine the sentiment and nature (fact or opinion) of a text
def get_sentiment(text):
    # Using TextBlob to get the polarity of the text. Polarity ranges from -1 (most negative) to 1 (most positive).
    sentiment = TextBlob(text).sentiment.polarity
    # Using TextBlob to get the subjectivity of the text. Subjectivity ranges from 0 (most objective) to 1 (most subjective).
    subjectivity = TextBlob(text).sentiment.subjectivity
    
    # Based on the sentiment and subjectivity, classify the text and return its classification.
    if sentiment > 0 and subjectivity > 0.5:
        return "positive\nfact"
    elif sentiment > 0 and subjectivity < 0.5:
        return "positive\nopinion"
    elif sentiment < 0 and subjectivity > 0.5:
        return "negative\nfact"
    elif sentiment < 0 and subjectivity < 0.5:
        return "negative\nopinion"
    elif sentiment == 0 and subjectivity > 0.5:
        return "neutral\nfact"
    elif sentiment == 0 and subjectivity < 0.5:
        return "neutral\nopinion"
    elif sentiment > 0 and subjectivity == 0:
        return "positive\nneutral"
    elif sentiment < 0 and subjectivity == 0:
        return "negative\nneutral"
    else:
        return "neutral"

# Function to analyze sentiments of a list of texts
def analyze_sentiments(full_texts):
    # Create a list of TextBlob objects for each text with a progress bar.
    blob_list = [TextBlob(text) for text in tqdm(full_texts, desc="Creating TextBlob objects")]
    
    # Extract subjectivity scores for each TextBlob object with a progress bar.
    subjectivity_scores = [blob.sentiment.subjectivity for blob in tqdm(blob_list, desc="Getting subjectivity scores")]
    
    # Extract polarity (sentiment) scores for each TextBlob object with a progress bar.
    sentiment_scores = [blob.sentiment.polarity for blob in tqdm(blob_list, desc="Getting sentiment scores")]
    
    # Determine the overall sentiment for each text using the get_sentiment function with a progress bar.
    sentiments = [get_sentiment(text) for text in tqdm(full_texts, desc="Analyzing overall sentiment")]
    
    # Return the list of sentiments, sentiment scores, and subjectivity scores for all texts.
    return sentiments, sentiment_scores, subjectivity_scores