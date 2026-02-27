from sklearn.datasets import make_regression
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
# Generate some data 
X , y = make_regression(n_samples=100,n_features=2,noise=0.1,random_state=42)
# # Use the transformer directly
# X_transformed = StandardScaler().fit_transform(X)
# LinearRegression().fit(X_transformed,y)
# Define the pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

# Fit everything in one go
pipe.fit(X, y)

# When you predict, the pipe automatically scales the new data first!
# Wrap your features in a 2D array (1 row, 2 columns)
predictions = pipe.predict([[0.2, 0.5]]) 
print(predictions)