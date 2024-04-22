from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import pandas as pd

# Load data from JSON file into DataFrame
data_file = "D:/IRProject/course_project/crawler/applerecords.json"
df = pd.read_json(data_file)

# Extract paragraphs from DataFrame
paragraphs = df['paragraphs'].tolist()

# Initialize TF-IDF vectorizer and fit on paragraphs
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(paragraphs)

# Calculate cosine similarities between documents
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Serialize TF-IDF vectorizer and matrix
tfidf_file = 'D:/IRProject/course_project/crawler/Apple_crawler/tfidf.pkl'
with open(tfidf_file, 'wb') as f:
    pickle.dump((tfidf_vectorizer, tfidf_matrix), f)

# Serialize cosine similarities matrix
cosine_sim_file = 'D:/IRProject/course_project/crawler/Apple_crawler/cosine_similarity.pkl'
with open(cosine_sim_file, 'wb') as f:
    pickle.dump(cosine_similarities, f)
