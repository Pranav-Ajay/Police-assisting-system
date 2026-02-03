# 1. Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


# 2. Load dataset
# Example CSV file: data.csv
# Columns: Feature(s) | Target
data = pd.read_csv("DELHI_MASTER_CRIME_DATASET_FINAL_CLEAN.csv")
print("Dataset Preview:")
print(data.head())


# 3. Separate independent and dependent variables
X = data.iloc[:, :-1].values   # features
y = data.iloc[:, -1].values    # target


# 4. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 5. Create Linear Regression model
model = LinearRegression()


# 6. Train the model
model.fit(X_train, y_train)


# 7. Display model parameters
print("\nModel Parameters:")
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)


# 8. Predict on test data
y_pred = model.predict(X_test)


# 9. Evaluate the model
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared (R²):", r2)


# 10. Visualize regression results (for single feature)
plt.scatter(X_test, y_test, label="Actual Data")
plt.plot(X_test, y_pred, label="Regression Line")
plt.xlabel("Input Feature")
plt.ylabel("Target Value")
plt.title("Linear Regression Model")
plt.legend()
plt.show()