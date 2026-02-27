import numpy as np
import pandas as pd
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
# Generating a random dataset with 10 rows and 4 columns
np.random.seed(42)
data = np.random.randn(10,4)
# Generating the dataframe and naming the columns
df = pd.DataFrame(data,columns=['f1','f2','f3','y'])
print(df)
# Define Feature Union
feature_union = FeatureUnion([
    ('scaler',StandardScaler()),
    ('pca',PCA(n_components=2))
    # Apply PCA Return to 2 components 
])
X_transformed = feature_union.fit_transform(df.drop(columns=['y']))
print(pd.DataFrame(X_transformed,columns = feature_union.get_feature_names_out()))
