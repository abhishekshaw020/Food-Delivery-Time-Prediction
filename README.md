Screenshots:
![image](https://github.com/user-attachments/assets/082d655a-a98a-48bb-a520-066e2508593d)

Enter Details and Click on Predict:
![image](https://github.com/user-attachments/assets/9679fd86-2031-43e2-b681-ee2a5ddc9490)

Project Structure:
├── app.py                  # Flask application code  
├── templates/              # HTML templates for UI  
│   └── index.html           
├── static/                 # CSS, JS, images  
├── model/                  
│   └── regression_model.joblib  # Trained ML model  
├── data/                   
│   └── X_train.csv          # Training dataset  
├── ml_helper.py             # Data processing functions  
├── README.md                # Project documentation  
└── requirements.txt         # Required dependencies  

🚀 How to Run the Project
Clone the repository:

git clone https://github.com/yourusername/delivery-time-prediction.git
cd delivery-time-prediction
Install dependencies:

pip install -r requirements.txt
Run the Flask application:

python app.py
Open the app in your browser:

http://127.0.0.1:5000/
