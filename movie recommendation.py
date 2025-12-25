movies = [
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "mood": "intense"},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "mood": "emotional"},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0, "mood": "serious"},
    {"title": "Gladiator", "genre": "Action", "rating": 8.5, "mood": "intense"},
    {"title": "Avengers: Endgame", "genre": "Action", "rating": 8.4, "mood": "exciting"},
    {"title": "Forrest Gump", "genre": "Drama", "rating": 8.8, "mood": "happy"},
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3, "mood": "hopeful"},
    {"title": "Titanic", "genre": "Romance", "rating": 7.9, "mood": "sad"},
    {"title": "The Notebook", "genre": "Romance", "rating": 7.8, "mood": "emotional"},
    {"title": "The Hangover", "genre": "Comedy", "rating": 7.7, "mood": "fun"},
    {"title": "Jumanji", "genre": "Comedy", "rating": 6.9, "mood": "exciting"}
]


def get_unique_genres(data):
    genres=[]
    for movie in data:
        if movie["genre"] not in genres:
            genres.append(movie["genre"])
    return genres
    
def recommend_movies(genre, mood, rating):
    result=[]
    for movie in movies:
        if movie["genre"].lower() == genre.lower():
            if movie["rating"] >= rating:
                if mood.lower() in movie["mood"].lower():
                    result.append(movie)
    return result

def main():
    print("Movie Recommendation System")

    name = input("Name: ").strip()
    print("Genres:",",".join(get_unique_genres(movies)))

    genre = input("Genre: ").strip()
    mood = input("Mood: ").strip()
    rating = float(input("Min Rating: ").strip())

    data =  recommend_movies(genre, mood, rating)

    print(f"\n{name} Recommendations:\n")

    if not data:
        print("No match")
        return

    for i, m in enumerate(data, 1):
        print(f"{i}. {m['title']}|{m['rating']}")

if __name__ == "__main__":
    main()