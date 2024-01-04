import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend
import matplotlib.pyplot as plt
import numpy as np
import math

# Load data from results.csv
df = pd.read_csv('results.csv')

# Define the mapping of visualization names
visualization_name_mapping = {
    'hist_score': 'Histogram of Score',
    'hist_subj_score': 'Histogram of Subjectivity Score',
    'hist_sent_score': 'Histogram of Sentiment Score',
    'box_subr_score': 'Boxplot of Score and Subreddit'
    # Add more mappings for other visualizations
}

def generate_visualizations(selected_candidate):
    
    # Filter data for the selected candidate
    candidate_data = df[df['Name'] == selected_candidate]

    visualizations_data = {
        'hist_score': 'hist_score.png',
        'hist_sub_score': 'hist_sub_score.png',
        'hist_sent_score': 'hist_sent_score.png',
        'box_subr_score': 'box_subr_score.png',
        # Add more visualization data entries
    }

    # Create and save the visualizations
    sns.set(style="whitegrid")

    # Histograms
    plt.figure(figsize=(10, 6))
    sns.histplot(data=candidate_data, x='Score', kde=True, bins=7)
    plt.title(f'Histogram of Score for {selected_candidate}')
    plt.savefig('static/hist_score.png')

    plt.figure(figsize=(10, 6))
    sns.histplot(data=candidate_data, x='Subjectivity_Score', kde=True, bins=7)
    plt.title(f'Histogram of Subjectivity_Score for {selected_candidate}')
    plt.savefig('static/hist_subj_score.png')

    plt.figure(figsize=(10, 6))
    sns.histplot(data=candidate_data, x='Sentiment_Score', kde=True, bins=7)
    plt.title(f'Histogram of Sentiment_Score for {selected_candidate}')
    plt.savefig('static/hist_sent_score.png')

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=candidate_data, x='Subreddit', y='Score', showfliers=False)
    plt.title('Boxplot of Score and Subreddit')
    plt.savefig('static/box_subr_score.png')

    return {'hist_score': 'hist_score.png', 
            'hist_sub_score': 'hist_sub_score.png', 
            'hist_sent_score': 'hist_sent_score.png', 
            'box_subr_score': 'box_subr_score.png'}

if __name__ == '__main__':
    # Example usage for testing
    selected_candidate = 'Candidate 1'  # Replace with the candidate chosen by the user
    selected_subreddit = 'Subreddit 1'
    visuals = generate_visualizations(selected_candidate)
    print("Visualizations generated:", visuals)    
    