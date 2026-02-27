from sklearn.base import BaseEstimator,TransformerMixin
import numpy as np
from sklearn.datasets import make_blobs
class MedianIQRScaler(BaseEstimator,TransformerMixin):
    def __init__(self):
        self.median = None
        self.iqr = None
    def fit(self,X,y=None):
        # Calculate medians and interquartile range for each feature
        self.medians = np.median(X,axis=0)
        Q1 = np.percentile(X,25,axis=0)
        Q3 =np.percentile(X,75,axis=0)
        self.iqr = Q3-Q1
        # Handle case where IQR is 0 tp avoid division by zero during transform
        self.iqr[self.iqr==0]=1
        return self
    def transform(self,X):
        # Check If fit has been called 
        if (self.medians is None or self.iqr is None) :
            raise RuntimeError("The transform has not been fitted yet.")
        # Scale Features using median & Iqr learned during fit
        return (X-self.medians)/self.iqr
# Generate Synthetic Data
X , _ = make_blobs(n_samples=100,n_features=2,centers=3,random_state=42)
# Initialize the Transform
scaler = MedianIQRScaler()
# Fit the scaler to the data
scaler.fit(X)
# Transform the Data
X_scaled = scaler.transform(X)
# Check the first few rows of the transformed data
print('Transformed data (first 5 rows)')
print(X_scaled[:5])
