import pandas as pd

print("=== Analyse de données - Projet Amine ===")

# Dataset personnalisé
data = {
    "Nom": ["Amine", "Yacine", "Karim", "Sofia", "Amine", "Lina"],
    "Age": [22, 30, 45, 28, 23, 35],
    "Salaire": [2000, 3200, 4000, 2800, 2100, 3500],
    "Ville": ["Paris", "Lyon", "Marseille", "Paris", "Lyon", "Paris"]
}

df = pd.DataFrame(data)

print("\n=== Données ===")
print(df)

# Statistiques
print("\nSalaire moyen :", df["Salaire"].mean())
print("Age maximum :", df["Age"].max())

# Filtrage personnalisé
print("\nPersonnes gagnant plus de 3000€ :")
print(df[df["Salaire"] > 3000])

# Analyse par ville
print("\nSalaire moyen par ville :")
print(df.groupby("Ville")["Salaire"].mean())

# Analyse spécifique Amine
print("\nDonnées concernant Amine :")
print(df[df["Nom"] == "Amine"])