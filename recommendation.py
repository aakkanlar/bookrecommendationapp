import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class BookRecommender:
    def __init__(self, dataset_path):
        self.df = pd.read_csv(dataset_path)
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self._build_tfidf_matrix()
        self.cosine_similarities = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)

    def _build_tfidf_matrix(self):
        content = self.df['description'].fillna('') + " " + self.df['genres'].fillna('')
        return self.tfidf_vectorizer.fit_transform(content)

    def get_recommendations(self, book_id, num_recommendations=5):
        sim_scores = list(enumerate(self.cosine_similarities[book_id]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_books = sim_scores[1:num_recommendations+1]
        book_indices = [i[0] for i in sim_books]
        return self.df['title'].iloc[book_indices].tolist()

recommender = BookRecommender('data.csv')
