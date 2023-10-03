from flask import Flask, jsonify
from recommendation import recommender

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Book Recommendation API!"

@app.route('/recommendations/<int:book_id>', methods=['GET'])
def get_recommendations(book_id):
    num_recommendations = 5  
    recommended_books = recommender.get_recommendations(book_id, num_recommendations)
    data = recommended_books[['bookId', 'title']].to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
