# Define the mapping of visualization names
import math
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

visualization_name_mapping = {
    'hist_score': 'Histogram of Score',
    'hist_subj_score': 'Histogram of Subjectivity Score',
    'hist_sent_score': 'Histogram of Sentiment Score',
    'scatter_score_subj_score': 'Scatterplot of Score and Subjectivity Score',
    'scatter_score_sent_score': 'Scatterplot of Score and Sentiment Score',
    'scatter_subj_score_sent_score': 'Scatterplot of Subjectivity Score and Sentiment Score',
    'box_subr_score': 'Boxplot of Score and Subreddit',
    'box_subr_subj_score': 'Boxplot of Subjectivity Score and Subreddit',
    'box_subr_sent_score': 'Boxplot of Sentiment Score and Subreddit',
    'box_over_score': 'Boxplot of Score and Overall Sentiment',
    'box_over_subj_score': 'Boxplot of Subjectivity Score and Overall Sentiment',
    'box_over_sent_score': 'Boxplot of Sentiment Score and Overall Sentiment',
    'count_subr_over': 'Count of Subreddit and Overall Sentiment',
    'count_subr_name': 'Count of Subreddit and Name',
    'count_over_name': 'Count of Overall Sentiment and Name',
    'line_score': 'Score Year-To-Date',
    'line_subj': 'Subjectivity Score Year-To-Date',
    'line_sent': 'Sentiment Score Year-To-Date',
}

def generate_visualizations(selected_candidates):
    # Load data from results.csv
    df = pd.read_csv('results.csv')
    
    # Filter data for the selected candidate
    candidate_data = df[df['Name'].isin(selected_candidates)]
    sns.set(style="whitegrid")
    
    # Define a color palette for the subreddits
    unique_subreddits = candidate_data['Subreddit'].unique()
    unique_overall= candidate_data['Overall_Sentiment'].unique()
    palette_subr = sns.color_palette("muted", len(unique_subreddits))
    palette_over = sns.color_palette("muted", len(unique_overall))
    color_dict_subr = dict(zip(unique_subreddits, palette_subr))
    color_dict_over = dict(zip(unique_overall, palette_over))

    # Histogram of Score
    plt.figure(figsize=(12, 6))
    sns.histplot(data=candidate_data, x='Score', kde=False, bins=10, hue='Name', alpha=0.8)
    plt.title('Histogram of Score')
    plt.xticks(np.arange(0, candidate_data['Score'].max(), 1000))
    plt.xticks(np.linspace(0, math.ceil(candidate_data['Score'].max() / 100) * 100, 11))
    plt.savefig('static/hist_score.png', bbox_inches='tight')
    plt.close()

    # Histogram of Subjectivity Score
    plt.figure(figsize=(12, 6))
    sns.histplot(data=candidate_data, x='Subjectivity_Score', kde=False, bins=np.arange(0, 1.01, 0.1), hue='Name', alpha=0.8)
    plt.title('Histogram of Subjectivity Score')
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.savefig('static/hist_subj_score.png', bbox_inches='tight')
    plt.close()

    # Histogram of Sentiment Score
    plt.figure(figsize=(12, 8))
    sns.histplot(data=candidate_data, x='Sentiment_Score', kde=False, bins=np.arange(-1, 1.01, 0.2), hue='Name', alpha=0.8)
    plt.title('Histogram of Sentiment Score')
    plt.xticks(np.arange(-1, 1.2, 0.2))  # x-ticks at the bin edges
    plt.savefig('static/hist_sent_score.png', bbox_inches='tight')
    plt.close()
    
    # Scatterplot of Score and Subjectivity Score
    plt.figure(figsize=(12, 10))
    sns.scatterplot(data=candidate_data, x='Score', y='Subjectivity_Score', hue='Name', alpha=0.8)
    plt.title('Scatterplot of Score and Subjectivity Score')
    plt.xticks(np.arange(0, candidate_data['Score'].max(), 1000))
    plt.xticks(np.linspace(0, math.ceil(candidate_data['Score'].max() / 100) * 100, 11))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.savefig('static/scatter_score_subj_score.png', bbox_inches='tight')
    plt.close()

    # Scatterplot of Score and Sentiment Score
    plt.figure(figsize=(12, 10))
    sns.scatterplot(data=candidate_data, x='Score', y='Sentiment_Score', hue='Name', alpha=0.8)
    plt.title('Scatterplot of Score and Sentiment Score')
    plt.xticks(np.arange(0, candidate_data['Score'].max(), 1000))
    plt.xticks(np.linspace(0, math.ceil(candidate_data['Score'].max() / 100) * 100, 11))
    plt.yticks(np.arange(-1, 1.2, 0.2))
    plt.savefig('static/scatter_score_sent_score.png', bbox_inches='tight')
    plt.close()

    # Scatterplot of Subjectivity Score and Sentiment Score
    plt.figure(figsize=(12, 10))
    sns.scatterplot(data=candidate_data, x='Subjectivity_Score', y='Sentiment_Score', hue='Name', alpha=0.8)
    plt.title('Scatterplot of Subjectivity Score and Sentiment Score')
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.yticks(np.arange(-1, 1.2, 0.2))
    plt.savefig('static/scatter_subj_score_sent_score.png', bbox_inches='tight')
    plt.close()

    # Boxplot of Score and Subreddit    
    plt.figure(figsize=(12, 10))
    sns.boxplot(data=candidate_data, x='Subreddit', y='Score', showfliers = False, palette=color_dict_subr)
    plt.title('Boxplot of Subreddit and Score')
    plt.savefig('static/box_subr_score.png', bbox_inches='tight')
    plt.close()
    
    # Boxplot of Subjectivity Score and Subreddit
    plt.figure(figsize=(12, 10))
    sns.boxplot(data=candidate_data, x='Subreddit', y='Subjectivity_Score', showfliers=False, palette=color_dict_subr)
    plt.title('Boxplot of Subjectivity Score and Subreddit')
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.savefig('static/box_subr_subj_score.png', bbox_inches='tight')
    plt.close()
    
    # Boxplot of Sentiment Score and Subreddit
    plt.figure(figsize=(12, 10))
    sns.boxplot(data=candidate_data, x='Subreddit', y='Sentiment_Score', showfliers=False, palette=color_dict_subr)
    plt.title('Boxplot of Sentiment Score and Subreddit')
    plt.yticks(np.arange(-1, 1.2, 0.2))
    plt.savefig('static/box_subr_sent_score.png', bbox_inches='tight')
    plt.close()

    # Boxplot of Score and Overall_Sentiment    
    plt.figure(figsize=(12, 10))
    sns.boxplot(data=candidate_data, x='Overall_Sentiment', y='Score', showfliers = False, palette=color_dict_over)
    plt.title('Boxplot of Score and Overall Sentiment')
    plt.savefig('static/box_over_score.png', bbox_inches='tight')
    plt.close()
    
    # Boxplot of Subjectivity Score and Overall_Sentiment
    plt.figure(figsize=(12, 10))
    sns.boxplot(data=candidate_data, x='Overall_Sentiment', y='Subjectivity_Score', showfliers=False, palette=color_dict_over)
    plt.title('Boxplot of Subjectivity Score and Overall Sentiment')
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.savefig('static/box_over_subj_score.png', bbox_inches='tight')
    plt.close()
    
    # Boxplot of Sentiment Score and Overall_Sentiment
    plt.figure(figsize=(12, 10))
    sns.boxplot(data=candidate_data, x='Overall_Sentiment', y='Sentiment_Score', showfliers=False, palette=color_dict_over)
    plt.title('Boxplot of Sentiment Score and Overall Sentiment')
    plt.yticks(np.arange(-1, 1.2, 0.2))
    plt.savefig('static/box_over_sent_score.png', bbox_inches='tight')
    plt.close()
    
    # Lineplot of Score over time
    plt.figure(figsize=(12, 10))
    sns.lineplot(data=candidate_data, x='Created', y='Score', hue = 'Name', errorbar = None)
    plt.title('Score Year-To-Date')
    plt.savefig('static/line_score.png', bbox_inches='tight')
    plt.close()
    
    # Lineplot of Subjectivity Score over Time
    plt.figure(figsize=(12, 10))
    sns.lineplot(data=candidate_data, x='Created', y='Subjectivity_Score', hue = 'Name', errorbar = None)
    plt.title('Subjectivity Score Year-To-Date')
    plt.savefig('static/line_subj.png', bbox_inches='tight')
    plt.close()
    
    # Lineplot of Sentiment Score over time
    plt.figure(figsize=(12, 10))
    sns.lineplot(data=candidate_data, x='Created', y='Sentiment_Score', hue = 'Name', errorbar = None)
    plt.title('Sentiment Score Year-To-Date')
    plt.savefig('static/line_sent.png', bbox_inches='tight')
    plt.close()
    
    # Count of Subreddit and Overall Sentiment
    plt.figure(figsize=(12, 10))
    sns.countplot(data=candidate_data, x='Subreddit', hue='Overall_Sentiment', alpha=0.8)
    plt.title('Countplot of Subreddit and Overall Sentiment')
    plt.savefig('static/count_subr_over.png', bbox_inches='tight')
    plt.close()
    
    # Count of Subreddit and Name
    plt.figure(figsize=(12,10))
    sns.countplot(data=candidate_data, x='Subreddit', hue='Name', alpha=0.8)
    plt.title('Countplot of Subreddit and Name')
    plt.savefig('static/count_subr_name.png', bbox_inches='tight')
    plt.close()
    
    # Count of Overall Sentiment and Name
    plt.figure(figsize=(12, 10))
    sns.countplot(data=candidate_data, x='Overall_Sentiment', hue='Name', alpha=0.8)
    plt.title('Countplot of Overall Sentiment and Name')
    plt.savefig('static/count_over_name.png', bbox_inches='tight')
    plt.close()   
    
    return {
        'file_paths': {
            'hist_score': 'hist_score.png', 
            'hist_sub_score': 'hist_subj_score.png', 
            'hist_sent_score': 'hist_sent_score.png',
            'scatter_score_subj_score': 'scatter_score_subj_score.png',
            'scatter_score_sent_score': 'scatter_score_sent_score.png',
            'scatter_subj_score_sent_score': 'scatter_subj_score_sent_score.png',
            'box_subr_score': 'box_subr_score.png',
            'box_subr_subj_score': 'box_subr_subj_score.png',
            'box_subr_sent_score': 'box_subr_sent_score.png',
            'box_over_score': 'box_over_score.png',
            'box_over_subj_score': 'box_over_subj_score.png',
            'box_over_sent_score': 'box_over_sent_score.png',
            'count_subr_over': 'count_subr_over.png',
            'count_subr_name': 'count_subr_name.png',
            'count_over_name': 'count_over_name.png',
            'line_score': 'line_score.png',
            'line_subj': 'line_subj.png',
            'line_sent': 'line_sent.png'
        },
        'candidate': selected_candidates,
        'visualization_name_mapping': visualization_name_mapping
    }
    

