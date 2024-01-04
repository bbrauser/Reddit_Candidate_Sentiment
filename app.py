from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-GUI backend
import matplotlib.pyplot as plt

app = Flask(__name__)

# Define the mapping of visualization names
visualization_name_mapping = {
    'hist_score': 'Histogram of Score',
    'hist_subj_score': 'Histogram of Subjectivity Score',
    'hist_sent_score': 'Histogram of Sentiment Score',
    'box_subr_score': 'Boxplot of Score and Subreddit'
    # Add more mappings for other visualizations
}

def generate_visualizations(selected_candidate):
    # Load data from results.csv
    df = pd.read_csv('results.csv')
    
    # Filter data for the selected candidate
    candidate_data = df[df['Name'] == selected_candidate]

    sns.set(style="whitegrid")

    # Histogram of Score
    plt.figure(figsize=(10, 6))
    sns.histplot(data=candidate_data, x='Score', kde=True, bins=7)
    plt.title(f'Histogram of Score for {selected_candidate}')
    plt.savefig('static/hist_score.png')
    plt.close()

    # Histogram of Subjectivity Score
    plt.figure(figsize=(10, 6))
    sns.histplot(data=candidate_data, x='Subjectivity_Score', kde=True, bins=7)
    plt.title(f'Histogram of Subjectivity Score for {selected_candidate}')
    plt.savefig('static/hist_subj_score.png')
    plt.close()

    # Histogram of Sentiment Score
    plt.figure(figsize=(10, 6))
    sns.histplot(data=candidate_data, x='Sentiment_Score', kde=True, bins=7)
    plt.title(f'Histogram of Sentiment Score for {selected_candidate}')
    plt.savefig('static/hist_sent_score.png')
    plt.close()

    # Boxplot of Score and Subreddit
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=candidate_data, x='Subreddit', y='Score', showfliers=False)
    plt.title('Boxplot of Score and Subreddit')
    plt.savefig('static/box_subr_score.png')
    plt.close()

    return {
        'file_paths': {
            'hist_score': 'hist_score.png', 
            'hist_sub_score': 'hist_subj_score.png', 
            'hist_sent_score': 'hist_sent_score.png', 
            'box_subr_score': 'box_subr_score.png'
        },
        'candidate': selected_candidate,
        'visualization_name_mapping': visualization_name_mapping
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    df = pd.read_csv('results.csv')
    if request.method == 'POST':
        selected_candidate = request.form['candidate']

        # Redirect to the visualization page for the selected candidate
        return redirect(url_for('visualizations', candidate=selected_candidate))

    # Assuming 'candidates' is a list of candidate names
    candidates = df['Name'].unique().tolist()
    return render_template('index.html', candidates=candidates)

@app.route('/visualizations/<candidate>')
def visualizations(candidate):
    # Generate visualizations and get the data for rendering the template
    data = generate_visualizations(candidate)

    return render_template('visualizations.html', **data)

if __name__ == '__main__':
    app.run(debug=True)
