# User Defined Transformers
# Two Approaches = Function Approach , Class Approach
'''import numpy as np
from sklearn.preprocessing import FunctionTransformer,StandardScaler
from sklearn.datasets import make_regression
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression


def cube_transform(x):
    return np.power(x,3)

# Create a Custom Transformer
cube_transformer = FunctionTransformer(cube_transform)

# Generate some data
X,y = make_regression(n_samples=100,n_features=2,noise=0.1,random_state=42)

# Use the transformer directly
X_transformed = cube_transformer.transform(X)
LinearRegression().fit(X_transformed,y)
print(X_transformed)
'''
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
class MedianIQRScaler(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.medians_ = None
        self.iqr_ = None

    def fit(self, X, y=None):
        # Calculate medians and interquartile range for each feature
        self.medians_ = np.median(X, axis=0)
        Q1 = np.percentile(X, 25, axis=0)
        Q3 = np.percentile(X, 75, axis=0)
        self.iqr_ = Q3 - Q1

        # Handle case where IQR is 0 to avoid division by zero during transform
        self.iqr_[self.iqr_ == 0] = 1
        return self

    def transform(self, X):
        # Check if fit has been called
        if self.medians_ is None or self.iqr_ is None:
            raise RuntimeError("The transformer has not been fitted yet.")

        # Scale features using median and IQR learned during fit
        return (X - self.medians_) / self.iqr_
from sklearn.datasets import make_blobs

# Generate synthetic data
X, _ = make_blobs(n_samples=100, n_features=2, centers=3, random_state=42)

# Initialize the transformer
scaler = MedianIQRScaler()

# Fit the scaler to the data
scaler.fit(X)

# Transform the data
X_scaled = scaler.transform(X)

# Check the first few rows of the transformed data
print("Transformed data (first 5 rows):")
print(X_scaled[:5])
