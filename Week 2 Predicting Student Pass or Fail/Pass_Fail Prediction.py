import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    'Hours_Studied': [2.5, 3, 2.1, 4, 2.7, 2.2, 3.5, 2.9, 2.3, 2.8, 1.5, 1.8, 1.2, 0.5, 1.9, 1.7, 0.8, 1.6, 1.1, 0.6],
    'Attendance':    [85, 90, 78, 88, 80, 76, 92, 79, 75, 82, 60, 70, 65, 68, 74, 60, 72, 69, 71, 69], #Larger Datasets will provide more stability.
    'Pass_Fail':     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}


df = pd.DataFrame(data)

print("Dataset:")
print(df)

X = df[['Hours_Studied', 'Attendance']]
y = df['Pass_Fail']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, zero_division=0))
print(X_train.shape)
print(X_test.shape)

plt.scatter(df['Hours_Studied'], df['Attendance'], c=df['Pass_Fail'], cmap='bwr', edgecolors='k')
plt.xlabel("Hours Studied")
plt.ylabel("Attendance (%)")
plt.title("Pass/Fail Distribution")
plt.grid(True)
plt.show()
