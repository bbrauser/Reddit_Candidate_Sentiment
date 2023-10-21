import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
from alive_progress import alive_bar
from datetime import date
import math

# Read the CSV file
df = pd.read_csv('results.csv')

# Get unique values in the "Name" column
unique_names = sorted(df['Name'].unique(), key=lambda x: x.split()[-1])

colors = {'Score': 'red', 'Subjectivity_Score': 'blue', 'Sentiment_Score': 'green', 
            'Name': "dark orange", 'Subreddit': "light purple", 
            'Overall_Sentiment': "dark yellow", 'Created': "light blue"}

# Create a PDF file
with PdfPages(f'Reports/Candidate Sentiment Analysis (Reddit) - {date.today()}.pdf') as pdf:

    with alive_bar(len(unique_names), title='Generating Charts') as bar:

        # Loop through each unique name
        for name in unique_names:
            
            # Subset the data for the current name
            name_data = df[df['Name'] == name]

            # Create a new page in the PDF file and add color legend
            fig, axs = plt.subplots(nrows=5, ncols=3, figsize=(6.5, 9))
            plt.suptitle(name, fontsize=9, fontstyle="italic", fontweight='bold')

            # Distribution
            # Visualize the distribution of the Reddit post score using a histogram
            sns.histplot(data=name_data, x='Score', kde=True, bins=10, ax=axs[0][0])
            axs[0][0].set_title('Distribution of Reddit Post Score', fontsize=5)
            axs[0][0].set_xticks(np.linspace(0, math.ceil(name_data['Score'].max() / 100) * 100, 11))
            axs[0][0].set_xticklabels(np.linspace(0, math.ceil(name_data['Score'].max() / 100) * 100, 11), fontsize=3.5)
            axs[0][0].set_yticks(np.linspace(0, 600, 7))
            axs[0][0].set_yticklabels(np.linspace(0, 600, 7), fontsize=3.5)
            axs[0][0].set_xlabel('Reddit Post Score', fontsize=5)
            axs[0][0].set_ylabel('Frequency', fontsize=5)
            axs[0][0].tick_params(axis='x', labelsize=3.5)
            axs[0][0].tick_params(axis='y', labelsize=4.5)
            axs[0][0].xaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))
            axs[0][0].yaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))

            # Visualize the distribution of Subjectivity Score using a histogram
            sns.histplot(data=name_data, x='Subjectivity_Score', kde=True, bins=10, ax=axs[0][1])
            axs[0][1].set_title('Distribution of Reddit Post Subjectivity Score', fontsize=5)
            axs[0][1].set_xticks(np.linspace(0, 1, 11))
            axs[0][1].set_xticklabels(np.linspace(0, 1, 11), fontsize=3.5)
            axs[0][1].set_yticks(np.linspace(0, 600, 7))
            axs[0][1].set_yticklabels(np.linspace(0, 600, 7), fontsize=3.5)
            axs[0][1].set_xlabel('Reddit Post Subjectivity Score', fontsize=5)
            axs[0][1].set_ylabel('Frequency', fontsize=5)
            axs[0][1].tick_params(axis='x', labelsize=3.5)
            axs[0][1].tick_params(axis='y', labelsize=4.5)
            axs[0][1].xaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
            axs[0][1].yaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))

            # Visualize the distribution of Sentiment Score using a histogram
            sns.histplot(data=name_data, x='Sentiment_Score', kde=True, bins=10, ax=axs[0][2])
            axs[0][2].set_title('Distribution of Reddit Post Sentiment Score', fontsize=5)
            axs[0][2].set_xticks(np.linspace(-1, 1, 11))
            axs[0][2].set_xticklabels(np.linspace(-1, 1, 11), fontsize=3.5)
            axs[0][2].set_yticks(np.linspace(0, 600, 7))
            axs[0][2].set_yticklabels(np.linspace(0, 600, 7), fontsize=3.5)
            axs[0][2].set_xlabel('Reddit Post Sentiment Score', fontsize=5)
            axs[0][2].set_ylabel('Frequency', fontsize=5)
            axs[0][2].tick_params(axis='x', labelsize=3.5)
            axs[0][2].tick_params(axis='y', labelsize=4.5)
            axs[0][2].xaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
            axs[0][2].yaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))
 
            # Relationship between two numerical variables
            # Visualize the relationship between Reddit Post Score and Subjectivity Score using a scatter plot
            sns.scatterplot(data=name_data, x='Score', y='Subjectivity_Score', ax=axs[1][0])
            axs[1][0].set_xticks(np.linspace(0, math.ceil(name_data['Score'].max() / 100) * 100, 11))
            axs[1][0].set_xticklabels(np.linspace(0, math.ceil(name_data['Score'].max() / 100) * 100, 11), fontsize=3.5)
            axs[1][0].set_yticks(np.linspace(0, 1, 11))
            axs[1][0].set_yticklabels(np.linspace(0, 1, 11), fontsize=3.5)
            axs[1][0].tick_params(axis='x', labelsize=3.5)
            axs[1][0].tick_params(axis='y', labelsize=3.5)
            axs[1][0].set_title('Relationship Between Reddit Post Score\nand Subjectivity Score', fontsize=5)
            axs[1][0].set_xlabel('Reddit Post Score', fontsize=5)
            axs[1][0].set_ylabel('Subjectivity Score', fontsize=5)
            axs[1][0].xaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))
            axs[1][0].yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

            # Visualize the relationship between Reddit Post Score and Sentiment Score using a scatter plot
            sns.scatterplot(data=name_data, x='Score', y='Sentiment_Score', ax=axs[1][1])
            axs[1][1].set_xticks(np.linspace(0, math.ceil(name_data['Score'].max() / 100) * 100, 11))
            axs[1][1].set_xticklabels(np.linspace(0, math.ceil(name_data['Score'].max() / 100) * 100, 11), fontsize=3.5)
            axs[1][1].set_yticks(np.linspace(-1, 1, 11))
            axs[1][1].set_yticklabels(np.linspace(-1, 1, 11), fontsize=3.5)
            axs[1][1].tick_params(axis='x', labelsize=3.5)
            axs[1][1].tick_params(axis='y', labelsize=3.5)
            axs[1][1].set_title('Relationship Between Reddit Post Score\nand Sentiment Score', fontsize=5)
            axs[1][1].set_xlabel('Reddit Post Score', fontsize=5)
            axs[1][1].set_ylabel('Sentiment Score', fontsize=5)
            axs[1][1].xaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))
            axs[1][1].yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

            # Visualize the relationship between Subjectivity Score and Sentiment Score using a scatter plot
            sns.scatterplot(data=name_data, x='Sentiment_Score', y='Subjectivity_Score', ax=axs[1][2])
            axs[1][2].set_xticks(np.linspace(-1, 1, 12))
            axs[1][2].set_xticklabels(np.linspace(-1, 1, 12), fontsize=3.5)
            axs[1][2].set_yticks(np.linspace(0, 1, 11))
            axs[1][2].set_yticklabels(np.linspace(0, 1, 11), fontsize=3.5)
            axs[1][2].tick_params(axis='x', labelsize=3.5)
            axs[1][2].tick_params(axis='y', labelsize=3.5)
            axs[1][2].set_title('Relationship Between Sentiment Score\nand Subjectivity Score', fontsize=5)
            axs[1][2].set_xlabel('Sentiment Score', fontsize=5)
            axs[1][2].set_ylabel('Subjectivity Score', fontsize=5)
            axs[1][2].xaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
            axs[1][2].yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

            # Visualize the relationship between a categorical variable and a numerical variable using a box plot
            sns.boxplot(data=name_data, x='Subreddit', y='Score', ax=axs[2][0], showfliers=False)
            axs[2][0].set_title('Relationship between Subreddit\nand Score', fontsize=5)
            axs[2][0].set_xlabel('Subreddit', fontsize=5)
            axs[2][0].set_yticks(np.linspace(0, math.ceil(name_data['Score'].max() / 100) * 100, 11))
            axs[2][0].set_yticklabels(np.linspace(0, math.ceil(name_data['Score'].max() / 100) * 100, 11), fontsize=3.5)
            axs[2][0].set_ylabel('Score', fontsize=5)
            axs[2][0].yaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))
            axs[2][0].tick_params(axis='x', labelsize = 3.5)
            axs[2][0].tick_params(axis='y', labelsize = 3.5)

            # Visualize the relationship between a categorical variable and a numerical variable using a box plot
            sns.boxplot(data=name_data, x='Subreddit', y='Subjectivity_Score', ax=axs[2][1], showfliers=False)
            axs[2][1].set_title('Relationship between Subreddit\nand Subjectivity Score', fontsize=5)
            axs[2][1].set_xlabel('Subreddit', fontsize=5)
            axs[2][1].set_ylabel('Subjectivity Score', fontsize=5)
            axs[2][1].set_yticks(np.linspace(0, 1, 11))
            axs[2][1].set_yticklabels(np.linspace(0, 1, 11), fontsize=3.5)
            axs[2][1].tick_params(axis='x', labelsize = 3.5)
            axs[2][1].tick_params(axis='y', labelsize = 3.5)
            axs[2][1].yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

            # Visualize the relationship between a categorical variable and a numerical variable using a box plot
            sns.boxplot(data=name_data, x='Subreddit', y='Sentiment_Score', ax=axs[2][2], showfliers=False)
            axs[2][2].set_title('Relationship between Subreddit\nand Sentiment Score', fontsize=5)
            axs[2][2].set_xlabel('Subreddit', fontsize=5)
            axs[2][2].set_ylabel('Sentiment Score', fontsize=5)
            axs[2][2].set_yticks(np.linspace(-1, 1, 12))
            axs[2][2].set_yticklabels(np.linspace(-1, 1, 12), fontsize=3.5)
            axs[2][2].tick_params(axis='x', labelsize = 3.5)
            axs[2][2].tick_params(axis='y', labelsize = 3.5)
            axs[2][2].yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

            # Visualize the relationship between a categorical variable and a numerical variable using a box plot
            sns.boxplot(data=name_data, x='Overall_Sentiment', y='Score', ax=axs[3][0], showfliers=False)
            axs[3][0].set_title('Relationship between Overall Sentiment\nand Score', fontsize=5)
            axs[3][0].set_xlabel('Overall Sentiment', fontsize=5)
            axs[3][0].set_yticks(np.linspace(0, math.ceil(name_data['Score'].max() / 100) * 100, 11))
            axs[3][0].set_yticklabels(np.linspace(0, math.ceil(name_data['Score'].max() / 100) * 100, 11), fontsize=3.5)
            axs[3][0].set_ylabel('Score', fontsize=5)
            axs[3][0].tick_params(axis='x', labelsize = 3.5)
            axs[3][0].tick_params(axis='y', labelsize = 3.5)
            axs[3][0].yaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))

            # Visualize the relationship between a categorical variable and a numerical variable using a box plot
            sns.boxplot(data=name_data, x='Overall_Sentiment', y='Subjectivity_Score', ax=axs[3][1], showfliers=False)
            axs[3][1].set_title('Relationship between Overall Sentiment\nand Subjectivity Score', fontsize=5)
            axs[3][1].set_xlabel('Overall Sentiment', fontsize=5)
            axs[3][1].set_ylabel('Subjectivity Score', fontsize=5)
            axs[3][1].set_yticks(np.linspace(0, 1, 11))
            axs[3][1].set_yticklabels(np.linspace(0, 1, 11), fontsize=3.5)
            axs[3][1].tick_params(axis='x', labelsize = 3.5)
            axs[3][1].tick_params(axis='y', labelsize = 3.5)
            axs[3][1].yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

            # Visualize the relationship between a categorical variable and a numerical variable using a box plot
            sns.boxplot(data=name_data, x='Overall_Sentiment', y='Sentiment_Score', ax=axs[3][2], showfliers=False)
            axs[3][2].set_title('Relationship between Overall Sentiment\nand Sentiment Score', fontsize=5)
            axs[3][2].set_xlabel('Overall Sentiment', fontsize=5)
            axs[3][2].set_ylabel('Sentiment Score', fontsize=5)
            axs[3][2].set_yticks(np.linspace(-1, 1, 12))
            axs[3][2].set_yticklabels(np.linspace(-1, 1, 12), fontsize=3.5)
            axs[3][2].tick_params(axis='x', labelsize = 3.5)
            axs[3][2].tick_params(axis='y', labelsize = 3.5)
            axs[3][2].yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

            # Visualize the relationship between a categorical variable and a numerical variable using a line plot for Score
            sns.lineplot(data=name_data, x='Created', y='Score', errorbar=None, ax=axs[4][0])
            axs[4][0].set_title('Score Year-To-Date', fontsize=5)
            axs[4][0].set_xlabel('Created', fontsize=5)
            axs[4][0].set_ylabel('Score', fontsize=5)
            axs[4][0].set_yticks(np.linspace(0, math.ceil(name_data['Score'].max() / 100) * 100, 11))
            axs[4][0].set_yticklabels(np.linspace(0, math.ceil(name_data['Score'].max() / 100) * 100, 11), fontsize=3.5)
            axs[4][0].tick_params(axis='x', labelsize=3.5)
            axs[4][0].tick_params(axis='y', labelsize=4.5)
            axs[4][0].set_xticks(axs[4][0].get_xticks())
            axs[4][0].set_xticklabels(axs[4][0].get_xticklabels(), rotation=45)
            axs[4][0].yaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))

            # Visualize the relationship between a categorical variable and a numerical variable using a line plot for Subjectivity Score
            sns.lineplot(data=name_data, x='Created', y='Subjectivity_Score', errorbar=None, ax=axs[4][1])
            axs[4][1].set_title('Subjectivity Score Year-To-Date', fontsize=5)
            axs[4][1].set_xlabel('Created', fontsize=5)
            axs[4][1].set_ylabel('Subjectivity Score', fontsize=5)
            axs[4][1].set_yticks(np.linspace(0, 1, 11))
            axs[4][1].set_yticklabels(np.linspace(0, 1, 11), fontsize=3.5)
            axs[4][1].tick_params(axis='x', labelsize=3.5)
            axs[4][1].tick_params(axis='y', labelsize=4.5)
            axs[4][1].set_xticks(axs[4][1].get_xticks())
            axs[4][1].set_xticklabels(axs[4][1].get_xticklabels(), rotation=45)
            axs[4][1].yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

            # Visualize the relationship between a categorical variable and a numerical variable using a line plot for Sentiment Score
            sns.lineplot(data=name_data, x='Created', y='Sentiment_Score', errorbar=None, ax=axs[4][2])
            axs[4][2].set_title('Sentiment Score - Year-To-Date', fontsize=5)
            axs[4][2].set_xlabel('Created', fontsize=5)
            axs[4][2].set_ylabel('Sentiment Score', fontsize=5)
            axs[4][2].set_yticks(np.linspace(-1, 1, 11))
            axs[4][2].set_yticklabels(np.linspace(-1, 1, 11), fontsize=3.5)
            axs[4][2].tick_params(axis='x', labelsize=3.5)
            axs[4][2].tick_params(axis='y', labelsize=4.5)
            axs[4][2].set_xticks(axs[4][2].get_xticks())
            axs[4][2].set_xticklabels(axs[4][2].get_xticklabels(), rotation=45)
            axs[4][2].yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

            # Adjust the layout and save the page to the PDF file
            plt.subplots_adjust(hspace=0.5)
            plt.tight_layout()
            pdf.savefig(fig)

            # Close the figure to free up memory
            plt.close(fig)
            bar()