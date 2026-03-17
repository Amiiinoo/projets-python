import os
import shutil

print("=== Script d'organisation de fichiers - Amine ===")

# Dossier personnalisé
dossier = "dossier_amine"
os.makedirs(dossier, exist_ok=True)

# Types de fichiers
types = {
    "Images_Amine": [".png", ".jpg"],
    "Documents_Amine": [".pdf", ".txt"],
    "Code_Amine": [".py", ".js"]
}

# Création des dossiers
for categorie in types:
    os.makedirs(os.path.join(dossier, categorie), exist_ok=True)

# Création de fichiers test personnalisés
open(os.path.join(dossier, "photo_amine.png"), "w").close()
open(os.path.join(dossier, "cv_amine.pdf"), "w").close()
open(os.path.join(dossier, "script_amine.py"), "w").close()

# Tri des fichiers
for fichier in os.listdir(dossier):
    chemin = os.path.join(dossier, fichier)

    if os.path.isfile(chemin):
        for categorie, extensions in types.items():
            if any(fichier.endswith(ext) for ext in extensions):
                destination = os.path.join(dossier, categorie, fichier)
                shutil.move(chemin, destination)
                print(f"Fichier déplacé : {fichier} → {categorie}")
                break

print("Organisation terminée avec succès 🚀")