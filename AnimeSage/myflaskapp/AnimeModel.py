
from flask import Flask, request, render_template
import joblib
import surprise
from surprise import Dataset, Reader, SVD
import pandas as pd
import random

app = Flask(__name__)

# Load the model
svd = joblib.load('svd_model.pkl')

# Load the names DataFrame
names_df = pd.read_csv('anime_names.csv')

 
@app.route('/')
def home():
    popular_anime = pd.read_csv('popular_anime.csv').to_dict(orient='records')
    return render_template('index.html', popular_anime=popular_anime)


def get_anime_name(mal_id):
    return names_df[names_df['MAL_ID'] == mal_id]['Name'].values[0]


@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Retrieve Ratings from Form
        anime_ids = [int(anime_id) for anime_id in request.form.getlist('anime[]')]
        ratings = [int(rating) for rating in request.form.getlist('rating[]')]

        # Load your dataset
        data = pd.read_csv('anime_ratings_reduced.csv')
        
        # Get the list of all item ids
        all_item_ids = set(data['MAL_ID'].unique())
        
        # Get the list of items that the new user has already rated
        rated_items = set(anime_ids)
        
        # Get the list of items to predict rating for
        items_to_predict = all_item_ids - rated_items
        
        # Make predictions
        predictions = []
        for item_id in items_to_predict:
            # Note: uid=None because the user is new 
            predicted_rating = svd.predict(uid=None, iid=item_id).est
            # Introduce noise
            noise = random.uniform(-0.5, 0.5)  # Adjust as per your requirement
            predicted_rating_noisy = predicted_rating + noise
            
            predictions.append((item_id, predicted_rating_noisy))
          
        
        # Sort the predictions
        predictions.sort(key=lambda x: x[1], reverse=True)
        print(f"Top predictions: {predictions[:10]}")  # Logging top predictions
        
        # Get the top 10 item ids
        recommended_items = [item_id for item_id, _ in predictions[:10]]
        
        # Convert item ids to names and scores using your names dataframe
        recommended_animes = names_df[names_df['MAL_ID'].isin(recommended_items)][['MAL_ID', 'Name']]
        recommended_animes['Score'] = [score for _, score in predictions[:10]]
        recommended_animes = recommended_animes.to_dict(orient='records')
        
        return render_template('recommendations.html', recommendations=recommended_animes)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")
        print(f"anime_ids: {anime_ids}")
        print(f"ratings: {ratings}")
        return render_template('error_page.html', error_message=str(e))
        

if __name__ == "__main__":
    app.run(debug=True)
