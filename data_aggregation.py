# Importing necessary modules.
import pandas as pd
from calendar import month_abbr
from datetime import datetime, timedelta, date

# Function to aggregate data and export it as a CSV file.
def aggregate_and_export(data, sentiments, sentiment_scores, subjectivity_scores):
    # Update the data dictionary with new key-value pairs.
    data.update({
        'Overall_Sentiment': sentiments, 
        'Full_Text': [' '.join(t) for t in zip(data['Title'], data['Text'])], 
        'Score': data['Score'], 
        'Subjectivity_Score': subjectivity_scores, 
        'Sentiment_Score': sentiment_scores 
    })

    # Convert the data dictionary to a pandas DataFrame.
    df = pd.DataFrame(data)

    # Filter the DataFrame to only include rows where the 'Created' column is within the last 365 days.
    start_date = datetime.now().date() - timedelta(days=365)
    
    # Convert the 'Created' column to datetime
    df['Created'] = pd.to_datetime(df['Created'])

    # Extract the date component
    df['Created'] = df['Created'].apply(lambda x: x.date())

    # Now, filter the dataframe
    df = df[df['Created'] >= start_date]

    # Convert all datetime.datetime objects in 'Created' column to datetime.date.
    df['Created'] = df['Created'].apply(lambda x: x.date() if isinstance(x, datetime) else x)

    # Convert 'Created' to datetime format
    df['Created'] = pd.to_datetime(df['Created'])

    # Sort by 'Created' in chronological order
    df = df.sort_values(by='Created')

    # Format the 'Created' column to show month abbreviation and year (e.g., 'Jan 23').
    df['Created'] = df['Created'].apply(lambda x: x.strftime('%b %Y'))

    # Export the DataFrame to a CSV file named 'results.csv' without row indices.
    df.to_csv('results.csv', index=False)
