# Import necessary modules
from web_scraper import get_presidential_candidates
from reddit_fetcher import fetch_reddit_data
from sentiment_analysis import analyze_sentiments
from data_aggregation import aggregate_and_export

# Fetch a list of presidential candidates
candidates = get_presidential_candidates()

# List of subreddits to search data from
subreddits = ['Conservative', 'Liberal', 'democrats', 'Republican']

# Fetch data from Reddit based on the list of candidates and subreddits
data = fetch_reddit_data(candidates, subreddits)

# Combine the 'Title' and 'Text' of fetched data for each entry into a single string
full_text = [' '.join(t) for t in zip(data['Title'], data['Text'])]

# Analyze the sentiments of the combined text. 
sentiments, sentiment_scores, subjectivity_scores = analyze_sentiments(full_text)

# Aggregate the fetched data, sentiments, and scores, then export them (possibly to a file or database)
aggregate_and_export(data, sentiments, sentiment_scores, subjectivity_scores)
