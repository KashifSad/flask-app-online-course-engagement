from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
from preprocess import preprocess_input

app = Flask(__name__)

# Load the trained model
with open('model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from the form
    input_data = {
        'CourseCategory': [request.form['CourseCategory']],
        'TimeSpentOnCourse': [float(request.form['TimeSpentOnCourse'])],
        'NumberOfVideosWatched': [int(request.form['NumberOfVideosWatched'])],
        'NumberOfQuizzesTaken': [int(request.form['NumberOfQuizzesTaken'])],
        'QuizScores': [float(request.form['QuizScores'])],
        'CompletionRate': [float(request.form['CompletionRate'])],
        'DeviceType': [int(request.form['DeviceType'])]
    }
    
    # Create a DataFrame
    input_df = pd.DataFrame(input_data)
    
    # Preprocess the input data
    input_df = preprocess_input(input_df)
    
    # Predict using the loaded model
    prediction = model.predict(input_df)[0]
    
    # Convert the prediction to a native Python data type
    prediction = int(prediction)
    
    return jsonify({'CourseCompletion': prediction})

if __name__ == '__main__':
    app.run(debug=True)
