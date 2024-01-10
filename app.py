from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-GUI backend
from visuals import generate_visualizations

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    df = pd.read_csv('results.csv')
    if request.method == 'POST':
        selected_candidates = request.form.getlist('candidate')  # Get a list of selected candidates

        # Redirect to the visualization page for the selected candidates
        return redirect(url_for('visualizations', candidates=','.join(selected_candidates)))

    candidates = df['Name'].unique().tolist()
    return render_template('index.html', candidates=candidates)

@app.route('/visualizations/<candidates>')
def visualizations(candidates):
    selected_candidates = candidates.split(',')  # Split the string back into a list
    data = generate_visualizations(selected_candidates)  # Pass the list to the function

    return render_template('visualizations.html', **data)

if __name__ == '__main__':
    app.run(debug=True)

