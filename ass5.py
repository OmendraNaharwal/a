import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.shape)
df.head()



df.info()












print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()

df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])
df.head()
















print(df.isnull().sum())



df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print(df.isnull().sum())

















df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

df = pd.get_dummies(df, columns=["Embarked"], dtype=int)
df.head()
















from sklearn.preprocessing import StandardScaler, MinMaxScaler

cols = ["Age", "Fare"]

df_std = df.copy()
df_std[cols] = StandardScaler().fit_transform(df[cols])

df_mm = df.copy()
df_mm[cols] = MinMaxScaler().fit_transform(df[cols])

print("Standardized:")
print(df_std[cols].describe().loc[["mean", "std", "min", "max"]])
print()
print("Min-Max:")
print(df_mm[cols].describe().loc[["mean", "std", "min", "max"]])








print(df.describe())
     

print("Mean Age   :", df["Age"].mean())
print("Median Age :", df["Age"].median())
print("Mode Age   :", df["Age"].mode()[0])
print("Std of Fare:", df["Fare"].std())
print("Skewness of Fare:", df["Fare"].skew())
     

# Survival rate by group
print(df.groupby("Sex")["Survived"].mean())
print()
print(df.groupby("Pclass")["Survived"].mean())
     
Correlation: values near +1 or -1 mean a strong relationship.


corr = df.corr()
print(corr["Survived"].sort_values())
     

df["Age"].plot(kind="hist", bins=20, title="Age distribution")
plt.show()

df.groupby("Sex")["Survived"].mean().plot(kind="bar", title="Survival rate by Sex (0=male, 1=female)")
plt.show()



