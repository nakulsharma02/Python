import pandas as pd 
import numpy as np
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder , MaxAbsScaler
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest , chi2

# Define the data with numerical labels for sentiments
data = {
    "Social Media Platform": ["Twitter", "Facebook", "Instagram", "Twitter", "Facebook",
                              "Instagram", "Twitter", "Facebook", "Instagram", "Twitter"],
    "Review": ["Love the new update!", "Too many ads now", "Great for sharing photos",
               "Newsfeed algorithm is biased", "Privacy concerns with latest update",
               "Amazing filters!", "Too much spam", "Easy to connect with friends",
               "Stories feature is fantastic", "Customer support lacking"],
    "age": [21, 19, np.nan, 17, 24, np.nan, 30, 19, 16, 31],
    "Sentiment": [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]  # Numeric labels: 1 for Positive, 0 for Negative
}
# Create a Dataframe
df = pd.DataFrame(data)
print(df)
# Create a Function Transformer
def count_words(reviews):
    # Counts no of words in each riview
    # Assume review is a 1d array like of test strings 
    return np.array([len(review.split()) for review in reviews]).reshape(-1,1)
# Create the function Transformer using the count_word function
word_count_transformer = FunctionTransformer(count_words)
feature_union = FeatureUnion([('word_count',word_count_transformer),
                              ('bag_of_words',CountVectorizer())])
column_transformer = ColumnTransformer(transformers=[('age_imputer',SimpleImputer(strategy='mean'),['age']),
                                                     ('platform_ohe',OneHotEncoder(),['Social Media Platform']),
                                                     ('review_processing',feature_union,'Review')],
                                                     remainder='drop')

final_pipeline = Pipeline(steps = [
    ('col_transformer',column_transformer),
    ('scaler',MaxAbsScaler()),
    ('selector',SelectKBest(score_func=chi2,k=10)),
    ('classifier',LogisticRegression())
])

final_pipeline.fit(df.drop(columns=['Sentiment']), df['Sentiment'])
# Sample new data to test
new_data = pd.DataFrame({
    "Social Media Platform": ["Instagram", "Twitter"],
    "Review": ["Best app ever!", "I hate the glitches"],
    "age": [25, 30]
})

# 1. Predict class labels (0 or 1)
predictions = final_pipeline.predict(new_data)
print(f"Predictions: {predictions}") # Output: [1 0]

# 2. Get probability scores (e.g., [Prob(0), Prob(1)])
probs = final_pipeline.predict_proba(new_data)
print(f"Probabilities:\n{probs}")