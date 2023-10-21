# Reddit Sentiment Analysis on Presidential Candidates

This project aims to fetch data from Reddit regarding registered presidential candidates for the year 2024, analyze sentiments in their mentions, and aggregate the data for analysis.

## Files and Descriptions:

__config_utils.py__:

• Contains configurations for the Reddit PRAW library.\n
• Loads necessary environment variables from a .env file.\n
• Provides the configured Reddit instance.\n

__data_aggregation.py__:

• Contains functions to aggregate data and export it as a CSV.\n
• Processes data to filter out entries older than 365 days.\n
• Formats data for cleaner representation.\n

__reddit_fetcher.py__:

• Uses the PRAW library to fetch Reddit posts mentioning the presidential candidates from specified subreddits.\n
• Aggregates data in a dictionary format for each candidate.\n
• Onlt candidates with 25 or more posts are gathered.\n

__sentiment_analysis.py__:

• Contains functions for sentiment analysis using the TextBlob library.\n
• Provides functions to classify sentiments into categories like "positive", "negative", or "neutral" and further into "fact", "opinion", or "neutral".\n

__web_scraper.py__:

• Contains a web scraping function to fetch a list of registered presidential candidates for the year 2024 from Ballotpedia.\n
• Uses the BeautifulSoup library for parsing the website's HTML.\n

__visuals.py__:

• Creates a PDF containing visualizations of data for the noteworthy 2024 presidential candidates according to ballotpedia.com.\n
• Subjectivity is on a scale of 0 (opinion) to 1 (fact).\n
• Sentiment is on a scale of -1 (negative) to 1 (positive).\n

## Prerequisites:

Install the necessary libraries with:

```bash
pip install praw pandas textblob tqdm requests beautifulsoup4 python-dotenv
```
