from flask import Flask, render_template, request
from web_scraper import get_presidential_candidates  # Ensure this matches your project structure

app = Flask(__name__)

# Sample list of subreddits - replace with actual subreddits from your project
subreddits = ['Conservative', 'Liberal', 'democrats', 'Republican']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_candidates = request.form.getlist('candidates')
        selected_subreddits = request.form.getlist('subreddits')

        # Now you can call fetch_reddit_data or any other function with selected candidates and subreddits
        # Example: results = fetch_reddit_data(selected_candidates, selected_subreddits)
        # Handle and display the results as needed
    else:
        selected_candidates = []
        selected_subreddits = []

    candidates = get_presidential_candidates()
    return render_template('index.html', 
                           candidates=candidates, 
                           selected_candidates=selected_candidates, 
                           selected_subreddits=selected_subreddits, 
                           subreddits=subreddits)

if __name__ == '__main__':
    app.run(debug=True)
