def display_header():
    print("=" * 50)
    print("      PARTH'S MOVIE RECOMMENDATION SYSTEM")
    print("=" * 50)

def get_recommendations(movies):
    while True:
        print("\nAvailable Genres:")
        for genre in movies:
            print(f"• {genre.title()}")

        choice = input("\nEnter a genre (or type 'exit' to quit): ").strip().lower()

        if choice == "exit":
            print("\nThank you for using the Movie Recommendation System! Have a great time watching! 🍿")
            break

        if choice in movies:
            print(f"\n--- Top Recommended {choice.title()} Movies ---")
            for number, movie in enumerate(movies[choice], start=1):
                print(f"{number}. {movie}")
            print("-" * 40)
        else:
            print("\n❌ Sorry! That genre is not available.")
            print("Please choose from the listed genres.")

if __name__ == "__main__":
    # Movie database dictionary
    movie_database = {
        "action": ["The Raid", "Nobody", "Baby Driver"],
        "comedy": ["Chup Chup Ke", "Bhagam Bhag", "Welcome"],
        "horror": ["Talk to Me", "Smile", "The Black Phone"],
        "thriller": ["Shutter Island", "Gone Girl", "Prisoners"],
        "sci-fi": ["Interstellar", "Arrival", "Ex Machina"]
    }
    
    display_header()
    get_recommendations(movie_database)