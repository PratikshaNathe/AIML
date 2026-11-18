import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


df=pd.read_csv("heart.csv")
print(df.head())


df=df.drop_duplicates()

for col in df.columns:
    if df[col].isnull().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col]=df[col].fillna(df[col].mean())
        else:
            df[col]=df[col].fillna(df[col].mode()[0])



print("\n missing values: ")
print(df.isnull().sum())


print(df.describe())

x=df.drop("target", axis=1)
y=df["target"]

x=pd.get_dummies(x, drop_first=True, dtype=int)

x_train, x_test, y_train, y_test=train_test_split(
    x, y, test_size=0.2, random_state=42
)

scaler=StandardScaler()

x_train=scaler.fit_transform(x_train)
x_teat=scaler.transform(x_test)

print("Training Data : ",x_train.shape)
print("Teating_Data : ",x_teat.shape)


plt.figure(figsize=(10,5))
plt.hist(df["age"].dropna(), bins=20, edgecolor="black")
plt.title("Histogram of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(10,5))
plt.hist(df["chol"].dropna(), bins=20, edgecolor="black")
plt.title("Histogram of Cholesterol")
plt.xlabel("cholesterol")
plt.ylabel("frequency")
plt.show()

plt.figure(figsize=(10,5))
sns.boxplot(x=df["age"])
plt.title("boxplot of age")
plt.xlabel("Age")
plt.show()


plt.figure(figsize=(10,5))
sns.boxplot(x=df["chol"])
plt.title("boxplot of age")
plt.xlabel("cholesterol")
plt.show()