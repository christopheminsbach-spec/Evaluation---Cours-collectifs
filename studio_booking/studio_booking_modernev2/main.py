"""
main.py
--------
Point d'entrée de l'application.

Ce fichier :
- crée la base de données ;
- ajoute des cours de démonstration ;
- affiche le menu ;
- appelle les fonctions CRUD selon le choix de l'utilisateur.
"""

# Création de la base de données
from studio_booking.studio_booking_modernev2.database import Base, engine

# Fonction de remplissage automatique
from studio_booking.studio_booking_modernev2.seed import seed

# Fonctions d'affichage
from studio_booking.studio_booking_modernev2.menu import (
    afficher_menu,
    afficher_liste_cours,
    afficher_cours_complets,
    afficher_message
)

# Fonctions CRUD
from studio_booking.studio_booking_modernev2.crud import (
    create_course,
    get_courses,
    register,
    get_full_courses,
    delete_course
)


def main():
    
    """
    Fonction principale de l'application.
    """

    # Création des tables dans SQLite si elles n'existent pas
    Base.metadata.create_all(bind=engine)

    # Ajout des cours de démonstration
    seed()

    # Boucle principale
    while True:

        afficher_menu()

        choix = input("Votre choix : ")

        # -------------------------------------------------
        # 1. Créer un cours
        # -------------------------------------------------
        if choix == "1":

            print("\n=== Création d'un cours ===")

            nom = input("Nom du cours : ")
            coach = input("Nom du coach : ")

            try:
                capacite = int(input("Capacité : "))

                if capacite <= 0:
                    afficher_message(
                        "La capacité doit être supérieure à 0."
                    )
                    input("\nAppuyez sur Entrée pour continuer...")
                    continue

                prix = float(input("Prix (€) : "))

                if prix < 0:
                    afficher_message(
                        "Le prix ne peut pas être négatif."
                    )
                    input("\nAppuyez sur Entrée pour continuer...")
                    continue

            except ValueError:
                afficher_message(
                    "Veuillez saisir des valeurs numériques."
                )
                input("\nAppuyez sur Entrée pour continuer...")
                continue

            create_course(
                nom,
                coach,
                capacite,
                prix
            )

            afficher_message(
                "Cours ajouté avec succès."
            )

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # -------------------------------------------------
        # 2. Afficher les cours
        # -------------------------------------------------
        elif choix == "2":

            courses = get_courses()

            afficher_liste_cours(courses)

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # -------------------------------------------------
        # 3. Inscrire une personne
        # -------------------------------------------------
        elif choix == "3":

            try:
                id_cours = int(
                    input("Identifiant du cours : ")
                )

            except ValueError:
                afficher_message(
                    "Identifiant invalide."
                )

                input("\nAppuyez sur Entrée pour continuer...")
                continue

            success, message = register(id_cours)

            afficher_message(message)

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # -------------------------------------------------
        # 4. Afficher les cours complets
        # -------------------------------------------------
        elif choix == "4":

            courses = get_full_courses()

            afficher_cours_complets(courses)

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # -------------------------------------------------
        # 5. Supprimer un cours
        # -------------------------------------------------
        elif choix == "5":

            try:
                id_cours = int(
                    input("Identifiant du cours à supprimer : ")
                )

            except ValueError:
                afficher_message(
                    "Identifiant invalide."
                )

                input("\nAppuyez sur Entrée pour continuer...")
                continue

            success, message = delete_course(id_cours)

            afficher_message(message)

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # -------------------------------------------------
        # 6. Quitter
        # -------------------------------------------------
        elif choix == "6":

            afficher_message(
                "Merci d'avoir utilisé Studio Booking Manager."
            )

            break

        # -------------------------------------------------
        # Choix invalide
        # -------------------------------------------------
        else:

            afficher_message(
                "Choix invalide."
            )

            input("\nAppuyez sur Entrée pour continuer...")


# Lance le programme uniquement si ce fichier est exécuté
if __name__ == "__main__":
    main()