from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np


app = Flask(__name__)
CORS(app)

model = pickle.load(open('xg_model.sav', 'rb'))

'''print(model.get_booster().feature_names)
example_features = [3, 1, 200000, 0.5, 0.8, 0.7, 0.0, 0.2, -5, 0.3, 120, 0.6, 1, 1, 4]
features_array = np.array([example_features], dtype=np.float32)

# Print the shape of the features array
print("Features array shape:", features_array.shape)

print(features_array)

# Make prediction
try:
    prediction = model.predict(features_array)
    print("Prediction:", prediction)
except ValueError as e:
    print("ValueError:", e)'''

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    features = [int(data['markets']), int(data['duration_ms']), float(data['acousticness']), 
                float(data['danceability']), float(data['energy']), float(data['instrumentalness']), float(data['liveness']), 
                float(data['loudness']), float(data['speechiness']), float(data['tempo']),float(data['valence']), 
                int(data['musicalkey']), int(data['musicalmode']), int(data['time_signature']),int(data['count'])]
    
    #print(features)
    
    features_array = np.array([features], dtype=np.float32)

    #print(features_array)
   
    prediction = model.predict(features_array)

    
    mapping = {
        0: 'Popularity of Artist and Song is between 0-20',
        1: 'Popularity of Artist and Song is between 21-40',
        2: 'Popularity of Artist and Song is between 41-60',
        3: 'Popularity of Artist and Song is between 61-80',
        4: 'Popularity of Artist and Song is between 81-100'
    }
    result = mapping[prediction[0]]
    #result = 1
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
