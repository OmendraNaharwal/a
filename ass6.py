import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True)
df = data.frame            # target column is "MedHouseVal"

print(df.shape)
df.head()








print(df.isnull().sum().sum(), "missing values")
df.describe()
















df.hist(bins=30, figsize=(12, 8))
plt.tight_layout()
plt.show()















df.plot(kind="box", subplots=True, layout=(3, 3), figsize=(12, 8))
plt.tight_layout()
plt.show()
















from sklearn.model_selection import train_test_split

X = df.drop(columns=["MedHouseVal"])
y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Train:", X_train.shape, "Test:", X_test.shape)















from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)




















from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

lin = LinearRegression()
lin.fit(X_train_s, y_train)
pred_lin = lin.predict(X_test_s)

lin_mse = mean_squared_error(y_test, pred_lin)
lin_mae = mean_absolute_error(y_test, pred_lin)
lin_r2 = r2_score(y_test, pred_lin)

print("Linear  MSE:", round(lin_mse, 4), " MAE:", round(lin_mae, 4), " R2:", round(lin_r2, 4))




















from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)
X_train_p = poly.fit_transform(X_train_s)
X_test_p = poly.transform(X_test_s)

print("Features before:", X_train_s.shape[1], " after:", X_train_p.shape[1])

pol = LinearRegression()
pol.fit(X_train_p, y_train)
pred_pol = pol.predict(X_test_p)

pol_mse = mean_squared_error(y_test, pred_pol)
pol_mae = mean_absolute_error(y_test, pred_pol)
pol_r2 = r2_score(y_test, pred_pol)

print("Poly    MSE:", round(pol_mse, 4), " MAE:", round(pol_mae, 4), " R2:", round(pol_r2, 4))






















result = pd.DataFrame({
    "Model": ["Linear", "Polynomial (deg 2)"],
    "MSE": [lin_mse, pol_mse],
    "MAE": [lin_mae, pol_mae],
    "R2": [lin_r2, pol_r2],
})
print(result.round(4))















plt.scatter(y_test, pred_lin, alpha=0.3, label="Linear")
plt.scatter(y_test, pred_pol, alpha=0.3, label="Polynomial")
plt.xlabel("Actual price")
plt.ylabel("Predicted price")
plt.legend()
plt.show()