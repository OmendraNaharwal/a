import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin",
         "BMI", "DiabetesPedigree", "Age", "Outcome"]
df = pd.read_csv(url, names=names)

print(df.shape)
print("Missing values:", df.isnull().sum().sum())

X = df.drop(columns=["Outcome"])
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)



















from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score

svm = SVC()
svm.fit(X_train, y_train)
pred = svm.predict(X_test)

acc_before = accuracy_score(y_test, pred)
f1_before = f1_score(y_test, pred)

print("Before tuning -> Accuracy:", round(acc_before, 4), " F1:", round(f1_before, 4))























from sklearn.model_selection import cross_val_score

scores = cross_val_score(SVC(), X_train, y_train, cv=5)

print("Scores of each fold:", scores.round(4))
print("Mean CV accuracy   :", round(scores.mean(), 4))
























from sklearn.model_selection import GridSearchCV

param_grid = {
    "C": [0.1, 1, 10, 100],
    "kernel": ["linear", "rbf"],
    "gamma": [0.001, 0.01, 0.1, 1],
}

grid = GridSearchCV(SVC(), param_grid, cv=5)
grid.fit(X_train, y_train)

print("Best parameters :", grid.best_params_)
print("Best CV accuracy:", round(grid.best_score_, 4))























best_svm = grid.best_estimator_
pred_best = best_svm.predict(X_test)

acc_after = accuracy_score(y_test, pred_best)
f1_after = f1_score(y_test, pred_best)

print("After tuning -> Accuracy:", round(acc_after, 4), " F1:", round(f1_after, 4))














result = pd.DataFrame({
    "": ["Before (default)", "After (Grid Search)"],
    "CV accuracy": [scores.mean(), grid.best_score_],
    "Test accuracy": [acc_before, acc_after],
    "Test F1": [f1_before, f1_after],
})
print(result.round(4))








