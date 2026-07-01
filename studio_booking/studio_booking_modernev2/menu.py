"""
Demarer l application de gestion de réservation de cours.
"""
def start(self):
    """
    Démarre l'application.
    """

    while True:
        self.afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            self.creer_cours()
        elif choix == "2":
            self.afficher_cours()
        elif choix == "3":
            self.inscrire_personne()
        elif choix == "4":
            self.afficher_cours_complets()
        elif choix == "5":
            self.supprimer_cours()
        elif choix == "6":
            print("\nMerci d'avoir utilisé Studio Booking Manager !")
            break
        else:
            print("\nOption invalide. Veuillez réessayer.")

"""
menu.py
--------
Fonctions d'affichage de l'application.

Ce fichier ne communique pas avec la base de données.
Il affiche uniquement les menus, les cours et les messages.
"""

def afficher_menu():
    """
    Affiche le menu principal.
    """

    print("\n" + "=" * 45)
    print("        STUDIO BOOKING MANAGER")
    print("=" * 45)
    print("1. Créer un cours")
    print("2. Afficher les cours")
    print("3. Inscrire une personne à un cours")
    print("4. Afficher les cours complets")
    print("5. Supprimer un cours")
    print("6. Quitter")
    print("=" * 45)


def afficher_cours(course):
    """
    Affiche les informations d'un seul cours.
    """

    print(f"\nID : {course.id}")
    print(f"Cours : {course.name}")
    print(f"Coach : {course.coach}")
    print(f"Places : {course.registered_count} / {course.capacity}")
    print(f"Places restantes : {course.remaining_places}")
    print(f"Prix : {course.price:.2f} €")
    print(f"CA actuel : {course.current_turnover:.2f} €")
    print(f"CA potentiel : {course.potential_turnover:.2f} €")
    print("-" * 45)


def afficher_liste_cours(courses):
    """
    Affiche la liste de tous les cours.
    """

    if not courses:
        print("\nAucun cours enregistré.")
        return

    print("\n========== LISTE DES COURS ==========")

    for course in courses:
        afficher_cours(course)


def afficher_cours_complets(courses):
    """
    Affiche uniquement les cours complets.
    """

    if not courses:
        print("\nAucun cours complet.")
        return

    print("\n========== COURS COMPLETS ==========")

    for course in courses:

        print(f"\nID : {course.id}")
        print(f"Cours : {course.name}")
        print(f"Coach : {course.coach}")
        print(f"Places : {course.registered_count} / {course.capacity}")
        print("-" * 45)

def afficher_message(message):
    """
    Affiche un message destiné à l'utilisateur.
    """

    print(f"\n{message}")