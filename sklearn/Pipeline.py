import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# Generating a random dataset with 10 rows and 4 columns
np.random.seed(42)
data = np.random.randn(10,4)
# Creating a dataframe and naming the column
df = pd.DataFrame(data,columns=['f1','f2','f3','y'])
print(df)
pipeline = Pipeline([
    ('scaler',StandardScaler()),
    ('pca',PCA())
])
print(pd.DataFrame(pipeline.fit_transform(df),columns=pipeline.get_feature_names_out()))