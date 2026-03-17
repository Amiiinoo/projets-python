import pandas as pd

# Création d’un dataset réaliste
data = {
    "Produit": ["PC", "Téléphone", "Tablette", "PC", "Téléphone", "Tablette", "PC"],
    "Prix": [1000, 500, 300, 1200, 700, 350, 900],
    "Quantité": [5, 10, 7, 3, 8, 6, 4],
    "Ville": ["Paris", "Lyon", "Marseille", "Paris", "Lyon", "Marseille", "Paris"]
}

df = pd.DataFrame(data)

print("=== Données ===")
print(df)

# Calcul du chiffre d'affaires
df["Chiffre_Affaires"] = df["Prix"] * df["Quantité"]

print("\n=== Données avec chiffre d'affaires ===")
print(df)

# Analyse par ville
ca_ville = df.groupby("Ville")["Chiffre_Affaires"].sum()
print("\n=== Chiffre d'affaires par ville ===")
print(ca_ville)

# Analyse par produit
ca_produit = df.groupby("Produit")["Chiffre_Affaires"].sum()
print("\n=== Chiffre d'affaires par produit ===")
print(ca_produit)

# Statistiques
print("\n=== Statistiques ===")
print("Total :", df["Chiffre_Affaires"].sum())
print("Moyenne :", df["Chiffre_Affaires"].mean())
print("Max :", df["Chiffre_Affaires"].max())