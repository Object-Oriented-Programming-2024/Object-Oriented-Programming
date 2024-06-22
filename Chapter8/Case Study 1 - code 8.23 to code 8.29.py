# code 8.23
import pandas as pd
import matplotlib as plt
df = pd.read_csv(
   "https://raw.githubusercontent.com/Object-Oriented-Programming-2024/" 
   "Object-Oriented-Programming/main/Chapter8/bank_personal_loan.csv"
  )
print("\n******* First 5 Rows of the data *******")
print(df.head(5))

#Displying basic details about the features
print("\n******* Basic Information about the Data frame *******")
print(df.info())

# Display basic summary statistics for numeric features
print("\n*******Descriptive statistics for numerical columns*******")
print(df.describe())

# Displaying number of unique values in Experience column
print(f"No of unique categories: {df['Experience'].nunique()}")
# Displaying all unique values with their frequency
print(df['Experience'].value_counts())
# Replacing unique values with a zero
df['Experience'] = df['Experience'].clip(lower=0)

# code 8.24
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

numerical_cols= ["Age","Experience","Income","CCAvg","Mortgage"]
for column in numerical_cols:
 # Plot the histogram
 fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 6))
 sns.histplot(data=df[column], ax=ax1, kde=True)

 # Plot the Spread using boxplot
 # Calculate the first quartile (Q1) and third quartile (Q3)
 Q1 = df[column].quantile(0.25)
 Q3 = df[column].quantile(0.75)

 # Calculate the interquartile range (IQR)
 IQR = Q3 - Q1

 # Define the lower and upper bounds to identify outliers
 lower_bound = Q1 - 1.5 * IQR
 upper_bound = Q3 + 1.5 * IQR

 # Find outlier indices
 outlier_indices = ((df[column] < lower_bound) | (df[column] > upper_bound))

 sns.boxplot(y=df[column], ax=ax2)
 # Plot the upper and lower bounds as horizontal lines
 plt.axhline(y=lower_bound, color='r', linestyle='--', linewidth=2, label='Lower Bound')
 plt.axhline(y=upper_bound, color='g', linestyle='--', linewidth=2, label='Upper Bound')

 ax1.set_title(f'{column} Histogram')
 ax2.set_title(f'{column} Boxplot')
 plt.show()

 # Replace outliers with the upper bound
 df.loc[outlier_indices, column] = upper_bound

# code 8.25
# Create a figure with 4 rows and 2 columns grid of subplots
fig, axes = plt.subplots(4, 2, figsize=(10, 15))

ax=axes[0,0]
# Mapping of numeric values to labels
mapping = {0: "No", 1: "Yes"}
# Temporarily replacing numeric values with labels in the column
df_temp = df.replace({"Personal Loan": mapping})
sns.countplot(x='Personal Loan', data=df_temp, ax=ax, palette="Set2")
ax.set_title(f"(a) Personal Loan")

ax=axes[0,1]
sns.countplot(x='Family', data=df, ax=ax, palette="Set2")
ax.set_title('(b) Family Distribution')


ax=axes[1,0]
# Mapping of numeric values to labels
mapping = {1: "Undergraduate", 2: "Graduate", 3: "Professional"}
# Temporarily replacing numeric values with labels in the column
df_temp = df.replace({"Education": mapping})
sns.countplot(x='Education', data=df_temp, ax=ax, palette="Set2")
ax.set_title(f"(c) Education Distribution")

ax=axes[1,1]
# Mapping of numeric values to labels
mapping = {0: "No", 1: "Yes"}
# Temporarily replacing numeric values with labels in the column
df_temp = df.replace({"Securities Account": mapping})
sns.countplot(x='Securities Account', data=df_temp, ax=ax, palette="Set2")
ax.set_title(f"(d) Securities Account Distribution")

ax=axes[2,0]
# Mapping of numeric values to labels
mapping = {0: "No", 1: "Yes"}
# Temporarily replacing numeric values with labels in the column
df_temp = df.replace({"CD Account": mapping})
sns.countplot(x='CD Account', data=df_temp, ax=ax, palette="Set2")
ax.set_title(f"(e) CD Account Distribution")

ax=axes[2,1]
# Mapping of numeric values to labels
mapping = {0: "No", 1: "Yes"}
# Temporarily replacing numeric values with labels in the column
df_temp = df.replace({"Online": mapping})
sns.countplot(x='Online', data=df_temp, ax=ax, palette="Set2")
ax.set_title(f"(f) Online Banking Distribution")

ax=axes[3,0]
# Mapping of numeric values to labels
mapping = {0: "No", 1: "Yes"}
# Temporarily replacing numeric values with labels in the column
df_temp = df.replace({"CreditCard": mapping})
sns.countplot(x='CreditCard', data=df_temp, ax=ax, palette="Set2")
ax.set_title(f"(f) Bank's CreditCard")

ax=axes[3,1]
sns.countplot(x='ZIP Code', data=df, ax=ax, palette="Set2")
ax.set_title('(h)  Distribution')

# Adjust spacing between subplots
plt.subplots_adjust(hspace=1)
plt.xticks([])

# Show the plot
plt.show()

# code 8.26
# Plotting the relationship between "Income" and "Personal Loan"
plt.figure(figsize=(6, 6))
sns.boxplot(x='Personal Loan', y='Income', data=df)
plt.title('Relationship between Income and Personal Loan')
plt.xlabel('Personal Loan (0: No, 1: Yes)')
plt.ylabel('Income')
plt.show()

# Plotting the relationship between Credit Card Spending -"CCAvg" and "Personal Loan"
plt.figure(figsize=(8, 6))
sns.boxplot(x='Personal Loan', y='CCAvg', data=df)
plt.title('Relationship between Credit Card Spending and Personal Loan')
plt.xlabel('Personal Loan (0: No, 1: Yes)')
plt.ylabel('Credit Card Spending (CCAvg)')
plt.show()

# Plotting the relationship between "Family" and "Personal Loan"
plt.figure(figsize=(6, 6))
sns.countplot(x='Family', hue='Personal Loan', data=df, palette='Set2')
plt.title('Relationship between Family and Personal Loan')
plt.xlabel('Number of Family Members')
plt.ylabel('Count')
plt.legend(title='Personal Loan', loc='upper right')
plt.show()

# code 8.27
numerical_cols= df.select_dtypes(include=['int64', 'float64']).columns

# Find the correlation between features
cor_matrix = df[numerical_cols].corr()
# Using visualizations for an overview of correlation among features
plt.figure(figsize=(10, 8))
sns.heatmap(cor_matrix, annot=True, cmap='BuGn', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

df.drop('ZIP Code', axis=1, inplace=True)
df['Age_Experience'] = (df['Age'] + df['Experience']) / 2
df.drop('Age', axis=1, inplace=True)
df.drop('Experience', axis=1, inplace=True)

# code 8.28
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score, confusion_matrix, roc_auc_score, roc_curve
from joblib import dump
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import warnings


# Splitting the dataframe into features and target variables
y = df['Personal Loan']
X = df.drop(columns=['Personal Loan'])

# Splitting the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Applying a standard scaler to normalize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Further split the training set into train and validation sets (80% train, 20% validate)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Initialize models and their hyperparameters
models = {
    'Logistic Regression': (LogisticRegression(), {'C': [0.001, 0.01, 0.1, 1, 10, 100]}),
    'Random Forest': (RandomForestClassifier(), {'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, None]}),'SVM': (SVC(probability=True), {'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf']})
}

best_accuracy = 0
best_model = None

# Training the models on all hyper parameter setting combinations
for name, (model, hyperparams) in models.items():
    print(f"Training {name}...")
    grid_search = GridSearchCV(model, hyperparams, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    model = grid_search.best_estimator_
    y_pred = model.predict(X_val)

    # Calculating and printing the accuracy
    accuracy = accuracy_score(y_pred, y_val)
    print(f"Accuracy: {accuracy:.2f}")

    # Calculating and printing the F1 score
    f1 = f1_score(y_pred, y_val)
    print(f"F1 Score: {f1:.2f}")

    # Calculating and printing the confusion matrix
    cm = confusion_matrix(y_val, y_pred)
    print(f"Confusion Matrix:\n{cm}")

    # Predicting probabilities for ROC and AUC
    y_prob = model.predict_proba(X_val)[:, 1]

    # Calculating ROC curve
    fpr, tpr, thresholds = roc_curve(y_val, y_prob)

    # Calculating AUC score
    auc_score = roc_auc_score(y_val, y_prob)

    # Creating the ROC curve chart
    plt.figure(figsize=(6, 4))
    plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {auc_score:.2f})')
    plt.plot([0, 1], [0, 1], 'r--')
    # plt.xlabel('False Positive Rate')
    # plt.ylabel('True Positive Rate')
    plt.title(f'ROC Curve ')
    plt.legend()
    plt.show()

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# code 8.29
# Applying a standard scaler to normalize the features
scaler = StandardScaler()
X_test = scaler.fit_transform(X_test)

# Predicting on the test set using the best model
y_pred_test = best_model.predict(X_test)

# Calculating and printing the accuracy
test_accuracy = accuracy_score(y_pred_test, y_test)
print(f"Accuracy: {test_accuracy:.2f}")

# Calculating and printing the F1 score
f1 = f1_score(y_test, y_pred_test)
print(f"F1 Score: {f1:.2f}")

# Calculating and printing the confusion matrix
cm = confusion_matrix(y_test, y_pred_test)
print(f"Confusion Matrix:\n{cm}")

# Predicting probabilities for ROC and AUC
y_prob = best_model.predict_proba(X_test)[:, 1]

# Calculating ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# Calculating AUC score
auc_score = roc_auc_score(y_test, y_prob)

# Creating the ROC curve chart
plt.figure(figsize=(6, 4))
plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {auc_score:.2f})')
plt.plot([0, 1], [0, 1], 'r--')
plt.title(f'ROC Curve ')
plt.legend()
plt.show()
# Printing and storing the best model
print(f"Best Model: {best_model}")
dump(best_model, "best_model.joblib")
