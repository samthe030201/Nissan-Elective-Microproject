from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('xg_model.sav')

# Define a function to map the prediction to popularity range
def map_prediction_to_popularity(prediction):
    return f'Popularity of Artist and Song is between {prediction*20}-{(prediction+1)*20}'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_features = np.array([[data['popularity'], data['markets'], data['duration_ms'], data['acousticness'],
                                data['danceability'], data['energy'], data['instrumentalness'], data['liveness'],
                                data['loudness'], data['speechiness'], data['tempo'], data['valence'],
                                data['musicalkey'], data['musicalmode'], data['time_signature']]])
    prediction = model.predict(input_features)[0]
    popularity_range = map_prediction_to_popularity(prediction)
    return jsonify({'prediction': popularity_range})

if __name__ == '__main__':
    app.run(debug=True)
