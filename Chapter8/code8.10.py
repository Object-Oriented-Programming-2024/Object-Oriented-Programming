import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, roc_curve,roc_auc_score
from joblib import dump
# Code to avoid the display of warnings from the libraries used
import warnings
warnings.simplefilter('ignore')

# Loading the Diabetes dataset
df1 = pd.read_csv (
        "https://raw.githubusercontent.com/Object-Oriented-Programming-2024/" \
        "Object-Oriented-Programming/main/Chapter8/diabetes.csv"
    )

# Spliting the DataFrame into features and target varaibles
y = df1["Outcome"]
X = df1.drop(columns=['Outcome'])

# Splitting the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Applying a standard scaler to normalize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Further split the training set into train and validation sets (80% train, 20% validate)
X_train,X_val,y_train, y_val = train_test_split(X_train, y_train, test_size=0.2,random_state=42)

# Applying the logistic regression
from sklearn.svm import SVC
model=SVC(probability=True)
# Various Hyperparameter settings for Support Vector Classifier
hyperparams = {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'kernel': ['linear', 'rbf', 'polynomial']}


# Initialize GridSearchCV with 5 folds and find the best hyperparameter settings
grid_search = GridSearchCV(model, hyperparams, cv=5, scoring='accuracy')

print(f"Training the model…")
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
plt.title(f'ROC Curve ')
plt.legend()
plt.show()

# Printing and storing the best model
print(model)
dump(model, f"best_model.joblib")
