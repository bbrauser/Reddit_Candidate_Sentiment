# Import necessary modules
from config_utils import get_reddit
from tqdm import tqdm
from datetime import datetime

def fetch_reddit_data(candidates, subreddits):
    # sourcery skip: extract-method, use-dict-items
    # Initialize a Reddit instance using the function from config_utils
    reddit = get_reddit()

    # Initialize a dictionary to store the aggregated data for all candidates
    data = {
        'Name': [],
        'Subreddit': [],
        'Title': [],
        'Text': [],
        'Score': [],
        'Created': []
    }

    # Loop over each combination of candidate and subreddit.
    for candidate, subreddit in tqdm([(c, s) for c in candidates for s in subreddits], desc="Searching subreddits", unit="combination"):
        
        # Temporary dictionary to store data for each candidate during the loop.
        temp_data = {
            'Name': [],
            'Subreddit': [],
            'Title': [],
            'Text': [],
            'Score': [],
            'Created': []
        }

        # Search the given subreddit for posts containing the candidate's name.
        posts = reddit.subreddit(subreddit).search(candidate, sort='new', limit=1000)
        
        # For each post fetched in the search
        for post in posts:
            temp_data['Name'].append(candidate)
            temp_data['Subreddit'].append(post.subreddit)
            temp_data['Title'].append(post.title)
            temp_data['Text'].append(post.selftext)
            temp_data['Score'].append(post.score)
            temp_data['Created'].append(datetime.fromtimestamp(post.created_utc).date())

        # Check if the total number of posts for the current candidate exceeds 25
        if len(temp_data['Name']) >= 25:
            # If it does, append the temporary data of this candidate to the main data dictionary
            for key in data:
                data[key].extend(temp_data[key])

    # Return the main data dictionary containing information about all valid candidates
    return data