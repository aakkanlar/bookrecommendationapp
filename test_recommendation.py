from recommendation import recommender

book_id = 1
num_recommendations = 5

recommendations = recommender.get_recommendations(book_id, num_recommendations)

print("Önerilen Kitaplar:")
for title in recommendations:
    print(title)