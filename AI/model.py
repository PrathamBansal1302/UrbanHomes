import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load the dataset
data = pd.read_csv("property_data.csv")

# Combine relevant features for recommendation
data['Features'] = data['Location'] + " " + data['Type'] + " " + data['Description']

# Vectorize the features
vectorizer = CountVectorizer()
feature_matrix = vectorizer.fit_transform(data['Features'])

# Compute similarity scores
similarity_matrix = cosine_similarity(feature_matrix)

# Function to recommend properties based on PropertyID
def recommend_properties(property_id, top_n=3):
    idx = data[data['PropertyID'] == property_id].index[0]
    similarity_scores = list(enumerate(similarity_matrix[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommended_indices = [i[0] for i in similarity_scores[1:top_n + 1]]
    return data.iloc[recommended_indices][['PropertyID', 'Title', 'Price', 'Location']]

if __name__ == "__main__":
    recommendations = recommend_properties(1)
    print(recommendations)
