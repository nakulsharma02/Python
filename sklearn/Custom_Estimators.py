from sklearn.base import BaseEstimator,ClassifierMixin
import numpy as np
from sklearn.utils import check_X_y
from sklearn.metrics import accuracy_score
class MostFrequentClassClassifier(BaseEstimator,ClassifierMixin):
    def __init__(self):
        self.most_frequent_ = None
    def fit(self,X,y):
        # Validate input X and target vector y
        X,y = check_X_y(X,y)
        # Ensure y is 1D
        y = np.ravel(y)
        # manually compute the most frequent class
        unique_classes,counts = np.unique(y,return_counts=True)
        self.most_frequent_ = unique_classes[np.argmax(counts)]
        return self.most_frequent_
    def predict(self,X):
        if self.most_frequent_ is None:
            raise ValueError("This Classifier instance is not fitted yet")
        # Predict the most frequent class for each input sample
        return np.full(shape=(X.shape[0]),fill_value=self.most_frequent_)
    def score(self,X,y):
        """ Return the mean accuracy on the given test data and labels."""
        # Ensure y is 1D
        y = np.ravel(y)
        predictions = self.predict(X)
        return accuracy_score(y,predictions)

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
# Load data
iris = load_iris()
X,y = iris.data,iris.target
# This ensures both sets have roughly 33% of each class
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.5, random_state=42, stratify=y
# )
# Simplify to a binary classification problem
is_class_0_or_1 = y < 2
X_bin = X[is_class_0_or_1]
y_bin = y[is_class_0_or_1]
# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_bin, y_bin, test_size=0.2, random_state=42)
# Iniatialize and fit the custom estimators
classifier = MostFrequentClassClassifier()
classifier.fit(X_train,y_train)
# Make Predictions 
Predictions = classifier.predict(X_test)
# Evaluate the custom estimators
print(f"Predicted Class for all test instances : {Predictions[0]}")
print(classifier.most_frequent_)
score = classifier.score(X_test, y_test)
print(f"Accuracy of the MostFrequentClassClassifier: {score}")