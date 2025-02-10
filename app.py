from flask import Flask, request, render_template
import joblib
import pandas as pd
from ml_helper import apply_transformer, create_speed

# Load the trained model
model = joblib.load("regression__model.joblib")

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs from the form
        distance = float(request.form['distance'])
        weather = request.form['weather']
        traffic = request.form['traffic']
        time_of_day = request.form['timeofday']
        vehicle_type = request.form['vehicle_type']
        prep_time = int(request.form['pre_time'])

        # Create the input DataFrame
        input_data = pd.DataFrame({
            "Distance_km": [distance],
            "Preparation_Time_min": [prep_time],
            "Weather": [weather],
            "Traffic_Level": [traffic],
            "Time_of_Day": [time_of_day],
            "Vehicle_Type": [vehicle_type]
        })

        # Add the 'Speed_[km/m]' column
        input_data = create_speed(input_data)

        # Transform the input data
        transformed_data = apply_transformer(input_data)

        # Make the prediction
        prediction = model.predict(transformed_data)
        predicted_time = round(float(prediction[0]), 2)

        return render_template('index.html', prediction_text=f'Estimated Delivery Time: {predicted_time} minutes')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)
