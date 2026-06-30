# menu.py

# -----------------------------
# Affiche le menu principal
# -----------------------------
def afficher_menu():
    print("\n" + "=" * 40)
    print("      STUDIO BOOKING MANAGER")
    print("=" * 40)
    print("1. Créer un cours")
    print("2. Afficher les cours")
    print("3. Inscrire une personne à un cours")
    print("4. Afficher les cours complets")
    print("5. Supprimer un cours")
    print("6. Quitter")
    print("=" * 40)


# -----------------------------
# Affiche les informations
# d'un seul cours
# -----------------------------
def afficher_cours(course):

    print(f"\nID : {course.id}")
    print(f"Cours : {course.name}")
    print(f"Coach : {course.coach}")
    print(f"Places : {course.registered_count} / {course.capacity}")
    print(f"Places restantes : {course.remaining_places}")
    print(f"Prix : {course.price:.2f} €")
    print(f"CA actuel : {course.current_turnover:.2f} €")
    print(f"CA potentiel : {course.potential_turnover:.2f} €")
    print("-" * 40)


# -----------------------------
# Affiche tous les cours
# -----------------------------
def afficher_liste_cours(courses):

    # Vérifie si la liste est vide
    if not courses:
        print("\nAucun cours enregistré.")
        return

    print("\n===== LISTE DES COURS =====")

    # Parcourt chaque cours et l'affiche
    for course in courses:
        afficher_cours(course)


# -----------------------------
# Affiche uniquement les cours
# dont toutes les places sont prises
# -----------------------------
def afficher_cours_complets(courses):

    if not courses:
        print("\nAucun cours complet.")
        return

    print("\n===== COURS COMPLETS =====")

    for course in courses:
        print(f"\nID : {course.id}")
        print(f"Cours : {course.name}")
        print(f"Coach : {course.coach}")
        print(f"Places : {course.registered_count}/{course.capacity}")
        print("-" * 40)


# -----------------------------
# Affiche un message utilisateur
# (succès, erreur, information)
# -----------------------------
def afficher_message(message):
    print(f"\n{message}")