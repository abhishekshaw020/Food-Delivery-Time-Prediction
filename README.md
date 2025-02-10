# Delivery Time Prediction

## 📸 Screenshots
### Enter Details to get Delivery Time:
![image](https://github.com/user-attachments/assets/082d655a-a98a-48bb-a520-066e2508593d)

### Enter Details and Click on Predict
![image](https://github.com/user-attachments/assets/9679fd86-2031-43e2-b681-ee2a5ddc9490)

---

## 📂 Project Structure
```
├── app.py                  # Flask application code  
├── templates/              # HTML templates for UI  
│   └── index.html          
├── static/                 # CSS, JS, images  
├── model/                  
│   └── regression__model.joblib  # Trained ML model  
├── data/                   
│   └── X_train.csv         # Training dataset  
├── ml_helper.py            # Data processing functions  
├── README.md               # Project documentation  
└── requirements.txt        # Required dependencies  
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```sh
git clone https://github.com/yourusername/food-delivery-time-prediction.git
cd delivery-time-prediction
```

### 2️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Flask application
```sh
python app.py
```

### 4️⃣ Open the app in your browser
```
http://127.0.0.1:5000/
```

---

## 📌 Features
- 📊 Predicts delivery time based on input details
- 🛠️ Machine Learning model for regression analysis
- 🌐 Simple UI built with Flask and HTML/CSS
- 📁 Pre-trained model stored using Joblib

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📧 Contact
For any queries, reach out to: [abhishaw020@gmail.com](mailto:abhishaw020@gmail.com)

### 🐳 Docker Image
```sh
docker pull abhishaw020/food_del
```

