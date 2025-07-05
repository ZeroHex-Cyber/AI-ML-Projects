# Week 2 – Student Performance Prediction using Logistic Regression

This project focuses on predicting student pass/fail outcomes using the **Logistic Regression** algorithm.
It's a part of my AI/ML internship weekly submission.
---

##  Objective

Build a binary classification model to predict whether a student will pass or fail based on:

- **Hours Studied**
- **Attendance Percentage (%)**
---

##  Files Included

- `Student Performance Prediction.ipynb` — Jupyter Notebook with code, visualizations, and model outputs

---

##  Dataset

A manually created dataset with 20 samples based on a logical academic rule:

- Pass (1): Hours Studied ≥ 2 and Attendance ≥ 75
- Fail (0): Otherwise

**Features:**
- Hours_Studied
- Attendance (percentage)
- Pass_Fail (label: 1 = Pass, 0 = Fail)
---

##  How to Run

1. Clone the repo or download this folder
2. Install dependencies:

```bash
pip install pandas scikit-learn matplotlib
```

3. Run the Jupyter notebook:

```bash
jupyter notebook Student Performance Prediction.ipynb
```

---

##  Results

- Model Used: *Logistic Regression*
- Accuracy: *100% (on balanced dataset)*
- Evaluation: *Confusion Matrix, Classification Report*

Prediction: Model predicts correctly for custom test cases like:

- model.predict([[2.5, 85]])  # Predicts Pass
- model.predict([[1.5, 60]])  # Predicts Fail

---

##  License

Free to use for educational purposes.
