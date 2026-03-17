import pandas as pd

print("=== Système de recommandation - Projet Amine ===")

# Dataset personnalisé
films = {
    "Film": ["Inception", "Titanic", "Avengers", "Interstellar", "Joker"],
    "Genre": ["Sci-Fi", "Romance", "Action", "Sci-Fi", "Drama"],
    "Note": [9, 8, 7, 9, 8]
}

df = pd.DataFrame(films)

print("\nFilms disponibles :")
print(df)

# Choix utilisateur
genre_utilisateur = input("\nQuel genre de film préfères-tu ? ")

# Filtrage
recommandations = df[df["Genre"].str.lower() == genre_utilisateur.lower()]

if not recommandations.empty:
    print("\n🎬 Recommandations pour toi :")
    print(recommandations.sort_values(by="Note", ascending=False))
else:
    print("\nAucune recommandation trouvée.")