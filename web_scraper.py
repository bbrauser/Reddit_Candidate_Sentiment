# Importing required libraries
import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm

def get_presidential_candidates():
    # Defining the URL of the webpage to scrape
    url1 = 'https://ballotpedia.org/List_of_registered_2024_presidential_candidates'

    # Sending a GET request to the webpage and storing the response
    response = requests.get(url1)

    # Parsing the content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Finding the 'div' element with class 'SingleDropdown' which contains the list of candidates
    table = soup.find('div', {'class': 'SingleDropdown'})

    # Extracting all the 'option' elements inside the 'div', which represent individual candidates
    rows = table.find_all('option')

    return [re.sub(r'\([^)]*\)', '', row.text.strip()) for row in tqdm(rows[1:], desc="Cleaning candidates")]