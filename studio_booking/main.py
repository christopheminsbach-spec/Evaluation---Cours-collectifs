from database import Base, engine
from seed import seed

# Fonctions d'affichage
from menu import (
    afficher_menu,
    afficher_liste_cours,
    afficher_cours_complets,
    afficher_message
)

# Fonctions CRUD utilisant SQLAlchemy ORM
from crud import (
    create_course,
    get_courses,
    register,
    get_full_courses,
    delete_course
)


def main():

    # Création des tables dans la base si elles n'existent pas
    Base.metadata.create_all(bind=engine)

    # Ajout des cours de démonstration lors du premier lancement
    seed()

    # Boucle principale : le menu reste affiché jusqu'à la fermeture
    while True:

        afficher_menu()

        # Récupère le choix de l'utilisateur
        choix = input("Votre choix : ")

        # =========================
        # 1. Création d'un cours
        # =========================
        if choix == "1":

            print("\n=== Création d'un cours ===")

            nom = input("Nom du cours : ")
            coach = input("Nom du coach : ")

            try:
                # Vérifie que la capacité est un entier positif
                capacite = int(input("Capacité : "))

                if capacite <= 0:
                    afficher_message("La capacité doit être supérieure à 0.")
                    continue

                # Vérifie que le prix est un nombre positif
                prix = float(input("Prix (€) : "))

                if prix < 0:
                    afficher_message("Le prix ne peut pas être négatif.")
                    continue

            except ValueError:
                afficher_message("Veuillez saisir des valeurs numériques.")
                continue

            # Enregistre le cours dans la base de données
            create_course(nom, coach, capacite, prix)

            afficher_message("Cours ajouté avec succès.")

        # =========================
        # 2. Afficher les cours
        # =========================
        elif choix == "2":

            # Récupère tous les cours enregistrés
            courses = get_courses()

            afficher_liste_cours(courses)

        # =========================
        # 3. Inscrire une personne
        # =========================
        elif choix == "3":

            try:
                id_cours = int(input("Identifiant du cours : "))
            except ValueError:
                afficher_message("Identifiant invalide.")
                continue

            # Incrémente le nombre de participants si possible
            success, message = register(id_cours)

            afficher_message(message)

        # =========================
        # 4. Afficher les cours complets
        # =========================
        elif choix == "4":

            courses = get_full_courses()

            afficher_cours_complets(courses)

        # =========================
        # 5. Supprimer un cours
        # =========================
        elif choix == "5":

            try:
                id_cours = int(input("Identifiant du cours à supprimer : "))
            except ValueError:
                afficher_message("Identifiant invalide.")
                continue

            # Suppression du cours sélectionné
            success, message = delete_course(id_cours)

            afficher_message(message)

            # Attend que l'utilisateur appuie sur Entrée
            input("\nAppuyez sur Entrée pour revenir au menu...")

        # =========================
        # 6. Quitter
        # =========================
        elif choix == "6":

            afficher_message("Merci d'avoir utilisé Studio Booking Manager.")
            break

        # Gestion d'un choix incorrect
        else:

            afficher_message("Choix invalide.")


# Point d'entrée du programme
if __name__ == "__main__":
    main()