import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# load the dataset
df = pd.read_csv("model training/data.csv")

# split the data and train the model
X = df[['Temperature1', 'Light Intensity1', 'Temperature2', 'Light Intensity2']]  # Features
y = df[['Typing Speed1 (words per minute)', 'Typing Speed2 (words per minute)']]  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# test model performance
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R^2 Score:", r2)
