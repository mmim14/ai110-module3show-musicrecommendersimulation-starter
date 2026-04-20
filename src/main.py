"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # print(len(songs))  # in-line test to see songs are loaded correctly 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8, "likes_acoustic":True}

    profiles = [
        # Starter example profile
        {"genre": "pop",    "mood": "happy",   "energy": 0.8,  "likes_acoustic": True},
        # High energy rock listener who hates acoustic
        {"genre": "rock",   "mood": "intense", "energy": 0.9,  "likes_acoustic": False},
        # Edge case: lofi genre but dislikes acoustic
        {"genre": "lofi",   "mood": "focused", "energy": 0.4,  "likes_acoustic": False},
        # Chill ambient listener who loves acoustic
        {"genre": "ambient","mood": "chill",   "energy": 0.25, "likes_acoustic": True},
    ]
    for i, profile in enumerate(profiles):
        recommendations = recommend_songs(profile, songs, k=5)

        print(f"\nTop recommendations for profile {i+1}:\n")
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()

if __name__ == "__main__":
    main()
