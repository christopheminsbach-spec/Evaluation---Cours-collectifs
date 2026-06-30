from database import Base, engine
from seed import seed

from menu import (
    afficher_menu,
    afficher_liste_cours,
    afficher_cours_complets,
    afficher_message
)

from crud import (
    create_course,
    get_courses,
    register,
    get_full_courses
)

from crud import (
    create_course,
    get_courses,
    register,
    get_full_courses,
    delete_course
)

def main():

    # Création de la base et des tables
    Base.metadata.create_all(bind=engine)

    # Ajout des cours de démonstration
    seed()

    while True:

        afficher_menu()

        choix = input("Votre choix : ")

# Creation d un cours
        if choix == "1":

            print("\n=== Création d'un cours ===")

            nom = input("Nom du cours : ")
            coach = input("Nom du coach : ")

            try:
                capacite = int(input("Capacité : "))

                if capacite <= 0:
                    afficher_message("La capacité doit être supérieure à 0.")
                    continue

                prix = float(input("Prix (€) : "))

                if prix < 0:
                    afficher_message("Le prix ne peut pas être négatif.")
                    continue

            except ValueError:
                afficher_message("Veuillez saisir des valeurs numériques.")
                continue

            create_course(nom, coach, capacite, prix)

            afficher_message("Cours ajouté avec succès.")
# Choisir un cours
        elif choix == "2":

            courses = get_courses()

            afficher_liste_cours(courses)
# Identifiant du cours
        elif choix == "3":

            try:
                id_cours = int(input("Identifiant du cours : "))
            except ValueError:
                afficher_message("Identifiant invalide.")
                continue

            success, message = register(id_cours)

            afficher_message(message)

        elif choix == "4":

            courses = get_full_courses()

            afficher_cours_complets(courses)
# Suprimer un cours
        elif choix == "5":

           try:
               id_cours = int(input("Identifiant du cours à supprimer : "))
           except ValueError:
               afficher_message("Identifiant invalide.")
               continue

           success, message = delete_course(id_cours)

           afficher_message(message)

           input("\nAppuyez sur Entrée pour revenir au menu...")

        elif choix == "6":

           afficher_message("Merci d'avoir utilisé Studio Booking Manager.")
           break

    else:

        afficher_message("Choix invalide.")


if __name__ == "__main__":
    main()