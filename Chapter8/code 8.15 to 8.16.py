# code 8.15
import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
df = pd.read_csv(
   "https://raw.githubusercontent.com/Object-Oriented-Programming-2024/" \
   "Object-Oriented-Programming/main/Chapter8/advertising_budget_sales.csv"
)

# Storing the independent features in X
X = df.drop('Sales', axis=1)
# Target Outcome / dependent feature in Y
y = df['Sales']

# Splitting the dataset into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Further splitting the training set into train and validation sets (80% train, 20% validate)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Initializing the linear regression model
model = LinearRegression()

# Training the model
model.fit(X_train, y_train)

# Making predictions on the validation set
y_val_pred = model.predict(X_val)

# Evaluate the model on the validation set
val_MAE = mean_absolute_error(y_val, y_val_pred)
val_MSE = mean_squared_error(y_val, y_val_pred)
r2 = r2_score(y_val, y_val_pred)
print("********* Validation Results *********\n")
print(f"Mean Absolute Error: {val_MAE:.4f}")
print(f"Mean Square Error: {val_MSE:.4f}")
print(f"R Square: {r2:.4f}")

# Visualize the difference between predictions and actual values
sns.scatterplot(x=y_val, y=y_val_pred, color='blue')
# Regression line
sns.regplot(x=y_val, y=y_val_pred, scatter=False, color='green')
plt.title('Prediction on Validation Set', fontsize=14)
plt.show()

# Make predictions on the test set
y_test_pred = model.predict(X_test)

# Evaluate the model on the test set
test_MAE = mean_absolute_error(y_test, y_test_pred)
test_MSE = mean_squared_error(y_test, y_test_pred)
test_r2 = r2_score(y_test, y_test_pred)
print("********* Test Results *********\n")
print(f"Mean Absolute Error:{test_MAE:.4f}")
print(f"Mean Square Error:{test_MSE:.4f}")
print(f"R Square:{test_r2:.4f}")

# Visualize the difference between predictions and actual values
sns.scatterplot(x=y_test, y=y_test_pred, color='blue')
# Regression line
sns.regplot(x=y_test, y=y_test_pred, scatter=False, color='green')
plt.title('Prediction on Test Set', fontsize=14)
plt.show()

#code 8.16
# Extract coefficients
coef_values = model.coef_
feature_names = X.columns

# Print coefficients and corresponding feature names
for i in range(len(feature_names)):
 print(f"{feature_names[i]}: {coef_values[i]:.4f}")
