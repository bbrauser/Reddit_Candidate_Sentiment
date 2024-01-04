from flask import Flask, render_template, request, redirect, url_for
from web_scraper import get_presidential_candidates
from app_visuals import generate_visualizations, visualization_name_mapping

app = Flask(__name__)

candidates = get_presidential_candidates()
subreddits = ['Conservative', 'Liberal', 'democrats', 'Republican', 'Libertarian', 'Progressive', 'Republicanism']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_candidate = request.form['candidate']
        selected_subreddit = request.form['subreddit']

        # Redirect to the visualization page for the selected candidate
        return redirect(url_for('visualizations', candidate=selected_candidate, subreddit=selected_subreddit))

    return render_template('index.html', candidates=candidates, subreddits=subreddits)

@app.route('/visualizations/<candidate>/<subreddit>')
def visualizations(candidate, subreddit):
    # Generate visualizations for the selected candidate
    visualizations_data = generate_visualizations(candidate)

    return render_template('visualizations.html', candidate=candidate, subreddit=subreddit, visualizations=visualizations_data, visualization_name_mapping=visualization_name_mapping)

if __name__ == '__main__':
    app.run(debug=True)
