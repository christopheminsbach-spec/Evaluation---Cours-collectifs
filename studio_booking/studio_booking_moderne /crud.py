"""
crud.py
--------
Toutes les opérations CRUD de l'application.

CRUD signifie :

C : Create  -> Ajouter un cours
R : Read    -> Lire les cours
U : Update  -> Inscrire une personne
D : Delete  -> Supprimer un cours
"""

from sqlalchemy import select

from database import SessionLocal
from models import Course


# =====================================================
# CREATE
# =====================================================

def create_course(name: str, coach: str, capacity: int, price: float) -> None:
    """
    Crée un nouveau cours.
    """

    session = SessionLocal()

    course = Course(
        name=name,
        coach=coach,
        capacity=capacity,
        registered_count=0,
        price=price
    )

    session.add(course)

    session.commit()

    session.close()


# =====================================================
# READ
# =====================================================

def get_courses() -> list[Course]:
    """
    Retourne tous les cours.
    """

    session = SessionLocal()

    courses = session.scalars(
        select(Course).order_by(Course.id)
    ).all()

    session.close()

    return courses


# =====================================================
# READ
# =====================================================

def get_course_by_id(course_id: int) -> Course | None:
    """
    Recherche un cours par son identifiant.
    """

    session = SessionLocal()

    course = session.get(Course, course_id)

    session.close()

    return course


# =====================================================
# UPDATE
# =====================================================

def register(course_id: int):
    """
    Inscrit une personne à un cours.
    """

    session = SessionLocal()

    course = session.get(Course, course_id)

    # Vérifie si le cours existe
    if course is None:
        session.close()
        return False, "Cours introuvable."

    # Vérifie si le cours est complet
    if course.is_full:
        session.close()
        return False, "Impossible : ce cours est complet."

    # Ajoute un participant
    course.registered_count += 1

    session.commit()

    session.close()

    return True, "Inscription validée."


# =====================================================
# READ
# =====================================================

def get_full_courses() -> list[Course]:
    """
    Retourne uniquement les cours complets.
    """

    session = SessionLocal()

    courses = session.scalars(
        select(Course).where(
            Course.registered_count == Course.capacity
        )
    ).all()

    session.close()

    return courses


# =====================================================
# DELETE
# =====================================================

def delete_course(course_id: int):
    """
    Supprime un cours.
    """

    session = SessionLocal()

    course = session.get(Course, course_id)

    if course is None:
        session.close()
        return False, "Cours introuvable."

    session.delete(course)

    session.commit()

    session.close()

    return True, "Cours supprimé avec succès."