# 🏥 Health Insurance Premium Prediction

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-green)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20Cloud-brightgreen)

---

## 📌 Project Overview

This project builds a Machine Learning system to estimate health insurance premiums based on age, BMI, smoking habits, medical history, and insurance plan type.

Dataset size: **50,000 records**

---

## 🚀 Key Highlights

✔ Large dataset (50K records)  
✔ Outlier detection using box plots  
✔ Feature engineering & encoding  
✔ Multicollinearity handled using VIF  
✔ Error-analysis driven improvements  
✔ Age-based model segmentation  
✔ Hybrid modeling (Linear Regression + XGBoost)  
✔ End-to-end deployment with Streamlit  

---

## 🧠 Modeling Strategy

After error analysis, customers were segmented based on age:

- **Linear Regression** → General age group  
- **XGB Regressor** → Young age group  

This segmentation improved predictive performance.

---

## 🔄 Workflow

1. Data Cleaning  
2. Outlier Treatment  
3. EDA  
4. Feature Engineering  
5. Encoding  
6. VIF Check  
7. Model Training  
8. Error Analysis  
9. Model Segmentation  
10. Deployment  

---

## 🛠 Tech Stack

Frontend: Streamlit  
Backend: Python, Pandas, NumPy  
ML Libraries: Scikit-learn, XGBoost  
Deployment: Streamlit Cloud  

---

## 🌐 Live Demo

🔗 https://your-streamlit-app-link.streamlit.app

---

## 💻 Run Locally

```bash
git clone https://github.com/AditiPatil31/HealthCare-Premium-Prediction-Project.git
cd HealthCare-Premium-Prediction-Project
pip install -r requirements.txt
streamlit run app.py
