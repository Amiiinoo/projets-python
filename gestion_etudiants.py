print("=== Gestionnaire d'étudiants - Projet Amine ===")

etudiants = []

while True:
    print("\n1. Ajouter étudiant")
    print("2. Afficher étudiants")
    print("3. Rechercher étudiant")
    print("4. Quitter")

    choix = input("Choix : ")

    if choix == "1":
        nom = input("Nom : ")
        age = int(input("Age : "))
        filiere = input("Filière : ")

        etudiant = {
            "nom": nom,
            "age": age,
            "filiere": filiere
        }

        etudiants.append(etudiant)
        print("Étudiant ajouté ✅")

    elif choix == "2":
        print("\nListe des étudiants :")
        for e in etudiants:
            print(e)

    elif choix == "3":
        nom_recherche = input("Nom à rechercher : ")
        for e in etudiants:
            if e["nom"].lower() == nom_recherche.lower():
                print("Trouvé :", e)

    elif choix == "4":
        print("Au revoir 👋")
        break