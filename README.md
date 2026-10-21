# house-price-prediction
House Price Prediction using Random Forest Regression
# 🏠 House Price Prediction Using Machine Learning

## 📌 Project Overview
This project predicts house prices using Machine Learning. It uses the Housing Dataset and a Random Forest Regressor to estimate house prices based on different property features.

## 🎯 Objectives
- Analyze and preprocess housing data.
- Train a Machine Learning regression model.
- Evaluate model performance.
- Save the trained model.
- Create a Flask API for house price predictions.

## 🛠️ Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Random Forest Regressor
- Flask
- Joblib

## 📊 Dataset
The project uses a Housing Dataset containing 545 rows and 13 columns. The target variable is `price`.

## ⚙️ Project Workflow
1. Load and explore the dataset.
2. Check missing values and duplicates.
3. Encode categorical variables.
4. Split data into training and testing sets.
5. Train the Random Forest Regressor.
6. Evaluate using MAE, RMSE, and R² Score.
7. Save the trained model.
8. Build a Flask API for predictions.

## 📁 Project Files
- `app.py` — Flask API.
- `house_price_model.joblib` — Trained Machine Learning model.
- `model_info.json` — Model configuration and evaluation details.
- `requirements.txt` — Required Python libraries.

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the API
```bash
python app.py
```

### 3. Open the API
Visit `http://127.0.0.1:5000/` in your browser.

## 📈 Model Evaluation
The model is evaluated using:
- **MAE:** Mean Absolute Error
- **RMSE:** Root Mean Squared Error
- **R² Score:** Coefficient of Determination

Actual evaluation results can be added here after training the model.

## 👩‍💻 Project Type
AI/ML Internship — Week 4 Final Project

---
Created as a Machine Learning project using Python and Scikit-learn.
