# Importing the necessary modules.
import os
from dotenv.main import load_dotenv
import praw

# Load the environment variables from a .env file.
load_dotenv()

# Set up the Reddit instance using the PRAW library and the environment variables.
reddit = praw.Reddit(
    client_id=os.environ['CLIENT_ID'], 
    client_secret=os.environ['CLIENT_SECRET'], 
    user_agent=os.environ['USER_AGENT'], 
    username=os.environ['USERNAME'], 
    password=os.environ['PASSWORD']
)

# Function to return the configured Reddit instance.
def get_reddit():
    return reddit