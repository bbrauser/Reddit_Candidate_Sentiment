import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Load data from results.csv
df = pd.read_csv('results.csv')

# Define the mapping of visualization names
visualization_name_mapping = {
    'hist_score': 'Histogram of Score',
    'hist_sub_score': 'Histogram of Subjectivity Score',
    'hist_sent_score': 'Histogram of Sentiment Score'
    # Add more mappings for other visualizations
}

def generate_visualizations(selected_candidate):
    # Filter data for the selected candidate
    candidate_data = df[df['Name'] == selected_candidate]

    visualizations_data = {
        'hist_score': 'hist_score.png',
        'hist_sub_score': 'hist_sub_score.png',
        'hist_sent_score': 'hist_sebt_score.png'
        # Add more visualization data entries
    }
    
    # Create and save the visualizations
    sns.set(style="whitegrid")

    # Histograms
    plt.figure(figsize=(10, 6))
    sns.histplot(data=candidate_data, x='Score', kde=True)
    plt.title(f'Histogram of Score for {selected_candidate}')
    plt.savefig('static/visualizations/hist_score.png')
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data=candidate_data, x='Subjectivity_Score', kde=True)
    plt.title(f'Histogram of Subjectivity_Score for {selected_candidate}')
    plt.savefig('static/visualizations/hist_sub_score.png')
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data=candidate_data, x='Sentiment_Score', kde=True)
    plt.title(f'Histogram of Sentiment_Score for {selected_candidate}')
    plt.savefig('static/visualizations/hist_sent_score.png')

    return {'hist_score': 'hist_score.jpeg'}

if __name__ == '__main__':
    # Example usage for testing
    selected_candidate = 'Candidate 1'  # Replace with the candidate chosen by the user
    visuals = generate_visualizations(selected_candidate)
    print("Visualizations generated:", visuals)
