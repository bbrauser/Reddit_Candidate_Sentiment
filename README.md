# Reddit Sentiment Analysis on Presidential Candidates

This project aims to fetch data from Reddit regarding registered presidential candidates for the year 2024, analyze sentiments in their mentions, and aggregate the data for analysis.

## Files and Descriptions:

__config_utils.py__:

• Contains configurations for the Reddit PRAW library.
• Loads necessary environment variables from a .env file.
• Provides the configured Reddit instance.

__data_aggregation.py__:

• Contains functions to aggregate data and export it as a CSV.
• Processes data to filter out entries older than 365 days.
• Formats data for cleaner representation.

__reddit_fetcher.py__:

• Uses the PRAW library to fetch Reddit posts mentioning the presidential candidates from specified subreddits.
• Aggregates data in a dictionary format for each candidate.

__sentiment_analysis.py__:

• Contains functions for sentiment analysis using the TextBlob library.
• Provides functions to classify sentiments into categories like "positive", "negative", or "neutral" and further into "fact", "opinion", or "neutral".

__web_scraper.py__:

• Contains a web scraping function to fetch a list of registered presidential candidates for the year 2024 from Ballotpedia.
• Uses the BeautifulSoup library for parsing the website's HTML.

## Prerequisites:

Install the necessary libraries with:

```bash
pip install praw pandas textblob tqdm requests beautifulsoup4 python-dotenv
```