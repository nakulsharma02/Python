""" Interpolation --> Fill Estimated value in the place of missing value """
# Used for
"""
1. Preserve data Integrity 
2. Smooth Trends
3. Avoid Data Loss
"""
# Types 
"""
Method | Description
linear -> Straight-line filling
time ->	Uses time index difference
index -> Based on index positions
values -> Based on values of another column
nearest -> Nearest available value
polynomial -> Fits polynomial curve
spline -> Smooth spline curve
quadratic -> Polynomial order 2
cubic -> Polynomial order 3
pad	-> Forward fill
backfill -> Backward fill
akima -> Spline variant  
"""
# Linear
import pandas as pd
data = pd.DataFrame({
    "Time" : [1,2,3,4,5],
    "Value" : [10,None,30,None,50]
})
print("Before Interpolation -> ")
print(data)
print("After Interpolation -> ")
data['Value'] = data['Value'].interpolate(method = "linear")
print(data)
