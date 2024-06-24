# code 8.30
import pandas as pd
import matplotlib.pyplot as plt, seaborn as sns
df = pd.read_csv("https://raw.githubusercontent.com/Object-Oriented-Programming-2024/"
                 "Object-Oriented-Programming/main/Chapter8/salary_data.csv"
)
print("\n******* First 5 Rows of the data *******")
print(df.head(5))

#  Displaying basic details about the features
print("\n******* Basic Information about the Data frame *******")
print(df.info())

# Display basic summary statistics for numeric features
print("\n*******Descriptive statistics for numerical columns*******")
print(df.describe())

# Imputate missing values
age = df['Age']
average=age.mean()
print(f"\n Replacing null Age values with Average Age : {average}" )
df['Age'].fillna(average, inplace=True)

gender = df['Gender']
most_frequent = gender.mode()[0]
print(f"\n Replacing null gender values with most frequent occurrence : {most_frequent}")
df['Gender'].fillna(most_frequent, inplace=True)

education = df['Education Level']
most_frequent = education.mode()[0]
print(f"\n Replacing null Education Level with most frequent occurrence : {most_frequent}")
df['Education Level'].fillna(most_frequent, inplace=True)

title = df['Job Title']
most_frequent = title.mode()[0]
print(f"\n Replacing null Job Title  values with most frequent occurrence : {most_frequent}")
df['Job Title'].fillna(most_frequent, inplace=True)

experience = df['Years of Experience']
average=experience.mean()
print(f"\n Replacing null Years of Experience values with Average  : {average}" )
df['Years of Experience'].fillna(average, inplace=True)

min_salary = df['Salary'].min()
df['Salary'].fillna(min_salary, inplace=True)

print("Making sure there are no null values: ")
print(df.isnull().sum())

# code 8.31
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder

# Getting categorical columns
categories = df.select_dtypes(include=['object']).columns

# Displaying categories for each categorical column
for col in categories:
 print(f"Categories for '{col}':")
 print(f"No of unique categories: {df[col].nunique()}")
 print( df[col].unique())
 print()

# Replacing duplicated categories within Education Level
df['Education Level'] = df['Education Level'].replace("Bachelor's Degree","Bachelor's")
df['Education Level'] = df['Education Level'].replace("Master's Degree","Master's")
df['Education Level'] = df['Education Level'].replace("phD","PhD")

# Performing ordinal encoding for Education Level and providing the order
education_levels = ["High School", "Bachelor's", "Master's", "PhD"]

# Initialize the OrdinalEncoder with education levels
ordinal_encoder = OrdinalEncoder(categories=[education_levels])

# Performing ordinal encoding for the 'Education' column
df['Education Level'] = ordinal_encoder.fit_transform(df[['Education Level']])

# Performing Label Encoding for 'Job Title'
label_encoder = LabelEncoder()
df['Job Title'] = label_encoder.fit_transform(df['Job Title'])

# Performing Label Encoding for 'Gender'
df['Gender'] = label_encoder.fit_transform(df['Gender'])

df['Country'] = label_encoder.fit_transform(df['Country'])

df['Race'] = label_encoder.fit_transform(df['Race'])
print(df.head())

# code 8.32
numerical_cols= df.select_dtypes(include=['int', 'float']).columns

# Find the correlation between features
cor_matrix = df[numerical_cols].corr()
print(cor_matrix)
# Using visualizations for an overview of correlation among features
plt.figure(figsize=(6, 6))
sns.heatmap(cor_matrix, annot=True, cmap='BuGn', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

df.info()

# code 8.33
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
age_experience = scaler.fit_transform(df[['Race', 'Country']])

# Combine the normalized features
df['Race_Country'] = (df['Race'] + df['Country'])

# Drop the original 'Age' and 'Years of Experience' columns
df.drop(['Race', 'Country'], axis=1, inplace=True)

# code 8.34
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

feature1 = "Age"
feature2 = "Years of Experience"

# Preprocessing: Normalize the data
X = StandardScaler().fit_transform(df[[feature1, feature2]])

k=4
# Initializing KMeans with k clusters
kmeans = KMeans(n_clusters=k, init="k-means++")

# Fitting the model
kmeans.fit(X)

# Getting the cluster centroids and labels
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Plotting the clusters
plt.figure(figsize=(8, 6))

# Plot data points for each cluster
for i in range(k):
    plt.scatter(X[labels == i, 0], X[labels == i, 1], s=50, label=f'Cluster {i+1}')

# Plot centroids
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='black',
         marker='*', label='Centroids')

plt.title('K-Means Clustering')
plt.legend()
plt.show()

# Adding the cluster labels to the dataframe
df['Age_Experience'] = labels

# code 8.35
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor

# Storing the independent features in X
X = df.drop('Salary', axis=1)


# Target Outcome / dependent feature in Y
y = df['Salary']

# Initializing the StandardScaler
scaler = StandardScaler()

# Fit and transform the features
X_scaled = scaler.fit_transform(X)

# Splitting the dataset into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2,
                                                    random_state=42)

# Further splitting the training set into train and validation sets (80% train, 20% validate)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2,
                                                 random_state=42)

# Initializing the models with default hyperparameters
models = {
 'Linear Regression': Ridge(),
 'Decision Tree Regression': DecisionTreeRegressor(random_state=42),
 'Random Forest Regression': RandomForestRegressor(random_state=42),
 'MLP Regression': MLPRegressor(random_state=42)
}

# Defining hyperparameter dictionary for each model
param_grids = {
 'Linear Regression': {'alpha': [0.01, 0.1, 1.0, 10.0]},
 'Decision Tree Regression': {'max_depth': [None, 5, 10, 15]},
 'Random Forest Regression': {'n_estimators': [100, 200, 300],
                                'max_depth': [None, 5, 10,15]},
 'MLP Regression': {
     'hidden_layer_sizes': [(100, 50)],
     'activation': ['relu'],
     'solver': ['adam'],
     'alpha': [0.001, 0.01],
     'learning_rate': ['constant', 'adaptive'],
     'max_iter': [500, 1000]
 }
}

best_performance_model= [0,None] # Variable to store the best performing model

for name, model in models.items():# Train and evaluate each model using GridSearchCV
 grid_search = GridSearchCV(model, param_grids[name], scoring='neg_mean_absolute_error',
                              cv=5)
 grid_search.fit(X_train, y_train)

 # Saving the best model
 best_model = grid_search.best_estimator_

 # Predicting on the validation set using the best model
 y_val_pred = best_model.predict(X_val)

 # Evaluating the model on the validation set
 val_MAE = mean_absolute_error(y_val, y_val_pred)
 val_MSE = mean_squared_error(y_val, y_val_pred)
 r2 = r2_score(y_val, y_val_pred)

 print(f"********* Validation Results for {name} *********\n")
 print(f'Best Hyperparameters: {grid_search.best_params_}')
 print(f'Mean Absolute Error: {val_MAE:.4f}')
 print(f'Mean Square Error: {val_MSE:.4f}')
 print(f'R Square: {r2:.4f}\n')

 if best_performance_model[0]< r2:
     best_performance_model[0]=r2
     best_performance_model[1]=best_model

print(f"Best Model: {best_performance_model}") # Printing the best performing model

# code 8.36
# Make predictions using the Best Model on the test set
y_test_pred = best_performance_model[1].predict(X_test)

# Evaluate the model on the test set
test_MAE = mean_absolute_error(y_test, y_test_pred)
test_MSE = mean_squared_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)

print("********* Test Results *********\n")
print(f'Mean Absolute Error: {test_MAE:.4f}')
print(f'Mean Square Error: {test_MSE:.4f}')
print(f'R Square: {r2_test:.4f}')

# Visualize the difference between predictions and actual values on the test set
plt.figure()
sns.scatterplot(x=y_test, y=y_test_pred, color='blue')

# Regression line
sns.regplot(x=y_test, y=y_test_pred, scatter=False, color='green')
plt.title('Prediction on Test Set (Random Forest Regression)', fontsize=14)
plt.xlabel('Actual Salary')
plt.ylabel('Predicted Salary')
plt.show()

# Store the best model
import pickle
file= open('best_model.pkl', 'wb')
pickle.dump(best_performance_model[1], file)
