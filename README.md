# 🌱 Django ML App — Iris Prediction Demo

A simple Django application that serves predictions from a machine learning model.

---

## 🧠 Project Overview

This project demonstrates how to:

- Train a machine learning model (Random Forest on the Iris dataset)  
- Save the trained model with joblib  
- Build a Django web app that loads the model and serves predictions  
- Provide both a web form and a JSON REST API  
- Write basic unit tests to ensure correctness  

---

## 📁 Project Structure

django-ml-app/  
- mlapp/ (Django project folder)  
  - settings.py  
  - urls.py  
- predictor/ (Django app to handle prediction)  
  - forms.py  
  - services.py  
  - views.py  
  - urls.py  
  - tests.py  
  - model/  
    - iris_rf.joblib  
- templates/  
  - predictor/  
    - predict_form.html  
- train.py  
- requirements.txt  
- manage.py
  
---

## ⚙️ Installation & Setup

1. Clone the repo  
   git clone <your-repo-url>  
   cd django-ml-app  

2. Create virtual environment (recommended)  
   python3 -m venv venv  
   source venv/bin/activate (on Windows: venv\Scripts\activate)  

3. Install dependencies  
   pip install -r requirements.txt  

4. Train the model  
   python train.py  
   This saves the model as predictor/model/iris_rf.joblib  

5. Apply migrations  
   python manage.py migrate  

6. Run the server  
   python manage.py runserver  

Web form available at http://127.0.0.1:8000/  
API endpoint available at http://127.0.0.1:8000/api/predict/  

---

## 🧪 Example API Call

Send a POST request to the API with input features:  

curl -X POST http://127.0.0.1:8000/api/predict/  
-H "Content-Type: application/json"  
-d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'  

Expected JSON response:  

{  
  "class_index": 0,  
  "class_name": "setosa",  
  "probabilities": {  
    "setosa": 1.0,  
    "versicolor": 0.0,  
    "virginica": 0.0  
  }  
}  

---

## ✅ Features

- Django web form interface  
- JSON API for developers  
- Pretrained Random Forest model on Iris dataset  
- Unit tests included  
- Easy to extend for other ML models  

---

## 🚀 Future Improvements

- Add authentication  
- Support for multiple models  
- Dockerize the project  
- Deploy to AWS / Heroku  

---

## 📄 License

Open-source project. Feel free to use and modify.  
Inspired by the KDnuggets: Building Machine Learning Application with Django.  
