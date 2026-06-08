# Student Performance Prediction - End-to-End Machine Learning Project

## Overview

This project is an End-to-End Machine Learning application that predicts a student's **Math Score** using demographic information and academic performance indicators. The project covers the complete ML lifecycle, including data ingestion, preprocessing, model training, model selection, and deployment through a Flask web application.

---

## Problem Statement

Student academic performance is influenced by various factors such as:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

The objective of this project is to build a machine learning model that accurately predicts a student's **Math Score** based on these features.

---

## Dataset

The dataset contains the following features:

| Feature                     | Description               |
| --------------------------- | ------------------------- |
| gender                      | Student gender            |
| race_ethnicity              | Ethnicity group           |
| parental_level_of_education | Parent education level    |
| lunch                       | Lunch type                |
| test_preparation_course     | Test preparation status   |
| reading_score               | Reading examination score |
| writing_score               | Writing examination score |
| math_score                  | Target variable           |

---

## Project Structure

```text
ml_proj/
│
├── artifacts/
│   ├── data.csv
│   ├── train.csv
│   ├── test.csv
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── notebook/
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── data/
│       └── stud.csv
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   │
│   ├── logger.py
│   ├── exceptions.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── app.py
├── requirements.txt
└── setup.py
```

---

## Machine Learning Pipeline

### 1. Data Ingestion

* Reads raw dataset.
* Splits data into train and test sets.
* Stores processed files in the `artifacts` folder.

### 2. Data Transformation

* Handles missing values.
* Applies One-Hot Encoding to categorical features.
* Applies Standard Scaling to numerical features.
* Saves preprocessing pipeline using Pickle.

### 3. Model Training

Multiple regression models are trained and evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* AdaBoost Regressor
* XGBoost Regressor
* CatBoost Regressor

The best-performing model is selected automatically based on evaluation metrics and saved for inference.

### 4. Prediction Pipeline

* Loads trained model and preprocessor.
* Transforms incoming user data.
* Generates Math Score predictions.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* CatBoost
* Flask
* Jupyter Notebook

---

## Installation

### Clone Repository

```bash
git clone https://github.com/cherry-achyuth/ml_proj.git
cd ml_proj
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Training Pipeline

```bash
python src/components/data_ingestion.py
```

This will:

* Ingest data
* Transform features
* Train models
* Save the best model

---

## Run Flask Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Web Application Features

* User-friendly interface
* Input student information
* Predict Math Score instantly
* Uses trained machine learning model for inference

---

## Future Improvements

* Deploy on AWS, Azure, or Render
* Add Docker support
* Implement CI/CD pipeline
* Add model monitoring
* Improve UI/UX
* Add feature importance visualization

---

## Author

**Achyuth Cherry**

GitHub: https://github.com/cherry-achyuth

---

## License

This project is intended for educational and learning purposes.
