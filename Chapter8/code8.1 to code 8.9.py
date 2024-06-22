# Code 8.1
# Import the Pandas library with the acronym 'pd'
import pandas as pd
# Import the Numpy library with the acronym 'np'
import numpy as np

# Ignore warning given by libraries
import warnings
warnings.simplefilter('ignore')

# Read the data from the csv file into a pandas dataframe
df1 = pd.read_csv (
    "https://raw.githubusercontent.com/Object-Oriented-Programming-2024/" \
    "Object-Oriented-Programming/main/Chapter8/housing.csv"
)

print("\n******* First 5 Rows of the data *******")
print(df1.head(5))

print("\n******* Last 10 Rows of the data *******")
print(df1.tail(10))

# The info method provide details about the features
print("\n******* Basic Information about the Data frame *******")
print(df1.info())

# Display basic summary statistics for numeric features
print("\n*******Descriptive statistics for numerical columns*******")
print(df1.describe())

# Code 8.2
# Imputate missing values
area = df1['Area']
average=area.mean()
print(f"Replacing null Area with Average Area : {average}" )
df1['Area'].fillna(average, inplace=True)

bathrooms = df1['Bathrooms']
most_frequent = bathrooms.mode()[0]
print(f"\nReplacing null bathrooms values with most frequent occurrence: {most_frequent}")
df1['Bathrooms'].fillna(most_frequent, inplace=True)

print("Making sure no null values: ")
print(df1.isnull().sum())

# Check for duplicates
print("\n******* Checking for duplicates *******")
print(df1.duplicated().sum())
df1.drop_duplicates(inplace=True)
print(f"Check rows after removing duplicates: {df1.shape}")

# Code 8.3
import matplotlib.pyplot as plt
import seaborn as sns
# Plot the distribution of target outcome 'Price'
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 6))
sns.histplot(df1['Price'], ax=ax1)
# Plot the Spread using boxplot
# Calculate the first quartile (Q1) and third quartile (Q3)
Q1 = df1['Price'].quantile(0.25)
Q3 = df1['Price'].quantile(0.75)

# Calculate the interquartile range (IQR)
IQR = Q3 - Q1
# Define the lower and upper bounds to identify outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
sns.boxplot(df1['Price'], ax=ax2)
# Plot the upper and lower bounds as horizontal lines
plt.axhline(y=lower_bound, color='r', linestyle='--', linewidth=2, label='Lower Bound')
plt.axhline(y=upper_bound, color='g', linestyle='--', linewidth=2, label='Upper Bound')

ax1.set_title('House Prices Histogram')
ax2.set_title("House Price Boxplot")
plt.show()

# Find outlier indices
outlier_indices = (df1["Price"] > upper_bound)
# Replace outliers with the upper bound
df1.loc[outlier_indices,"Price"] = upper_bound

# Code 8.4
# Find the correlation between features
cor_matrix = df1[['Price','Bedrooms','Bathrooms','Parking']].corr()
print(cor_matrix)
# Using visualizations for an overview of correlation among features
plt.figure(figsize=(6, 6))  # Set the figure size
sns.heatmap(cor_matrix, annot=True, cmap='BuGn', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Check for correlation between target outcome Price with Area
plt.figure(figsize=(6, 6))
plt.scatter(x = df1['Area'], y = df1['Price'])
plt.ylabel('Price', fontsize=12)
plt.xlabel('Area', fontsize=12)
plt.show()

# Code 8.5
# Create a figure with a 2 rows and 2 columns grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(8, 6), gridspec_kw={'hspace': 0.4})

# At column 0 and row 0 of the plot
ax=axes[0,0]
# Calculate the frequency of bedrooms per category
df1['Bedrooms'].value_counts().plot(kind="bar", ax=ax)
ax.set_title('(a) Bedrooms Distribution')
ax.set_ylabel("Count")

ax=axes[0,1]
# Calculate the frequency of Bathrooms per category
df1['Bathrooms'].value_counts().plot(kind="bar", ax=ax)
ax.set_title('(b) Bathrooms Distribution')
ax.set_ylabel("Count")

ax=axes[1,0]
# Calculate the frequency of Parking per category
df1['Parking'].value_counts().plot(kind="bar", ax=ax)
ax.set_title('(c) Parking Distribution')
ax.set_ylabel("Count")

ax=axes[1,1]
# Calculate the frequency of Yes or No in the Basement
df1['Basement'].value_counts().plot(kind="bar", ax=ax)
ax.set_title('(d) Basement Distribution')
ax.set_ylabel("Count")

# Show the plot
plt.show()

# Code 8.6
# Apply the log transformation to normalize the spread of the data
df1['price'] = np.log(df1['Price']/1000000)

# Converting categorical boolean feature to one hot encoding
temp = pd.get_dummies(df1['Basement'], drop_first = True, prefix='Basement').astype(int)
df1 = pd.concat([df1, temp], axis = 1)
df1.drop(['Basement'], axis = 1, inplace = True)
df1.rename(columns={'Basement_yes': 'Basement'}, inplace=True)
df1.head(5)

# Code 8.7
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Removing the target variable from the dataset
X = df1.drop("Price", axis=1)
# Target Outcome
y = df1['Price']

# Split the dataset into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Further split the training set into train and validation sets (80% train, 20% validate)
X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.2, random_state=42
)

# Initialize the linear regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the validation set
y_val_pred = model.predict(X_val)

# Evaluate the model on the validation set using  R-sqaured
r2 = r2_score(y_val, y_val_pred)
print("********* Validation R-sqaured *********\n", r2)

# Make predictions on the test set
y_test_pred = model.predict(X_test)
# Evaluate the model on the test set using  R-sqaured
test_mse = mean_squared_error(y_test, y_test_pred)
print("********* Test  R-sqaured: *********  \n", test_mse)

# Visualize the difference between predictions and actual values
sns.scatterplot(x=y_test, y=y_test_pred, color='blue')
# Regression line
sns.regplot(x=y_test, y=y_test_pred, scatter=False, color='green')
plt.title('Prediction on Test Set', fontsize=14)
plt.show()

# code 8.8
import pickle

# Saving the model to model.pkl file
file= open('model.pkl', 'wb')
pickle.dump(model, file)

# Loading the model from model.pkl file
file=open('model.pkl', 'rb')
model = pickle.load(file)

# code 8.9
from joblib import dump, load

# Store the model in model.joblib file
dump(model, 'model.joblib')

# Load the model from model.joblib file
loaded_model = load('model.joblib')



