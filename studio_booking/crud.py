# crud.py

from database import SessionLocal
from models import Course


def create_course(name, coach, capacity, price):
    """Créer un nouveau cours."""

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


def get_courses():
    """Retourne tous les cours."""

    session = SessionLocal()

    courses = session.query(Course).order_by(Course.id).all()

    session.close()

    return courses


def get_course_by_id(course_id):
    """Recherche un cours par identifiant."""

    session = SessionLocal()

    course = session.query(Course).filter_by(id=course_id).first()

    session.close()

    return course


def register(course_id):
    """Inscrit une personne à un cours."""

    session = SessionLocal()

    course = session.query(Course).filter_by(id=course_id).first()

    # Vérifie si le cours existe
    if course is None:
        session.close()
        return False, "Cours introuvable."

    # Vérifie si le cours est complet
    if course.registered_count >= course.capacity:
        session.close()
        return False, "Impossible : ce cours est complet."

    # Inscription
    course.registered_count += 1

    session.commit()
    session.close()

    return True, "Inscription validée."


def get_full_courses():
    """Retourne uniquement les cours complets."""

    session = SessionLocal()

    courses = session.query(Course).filter(
        Course.registered_count == Course.capacity
    ).all()

    session.close()

    return courses

def delete_course(course_id):
    """Supprime un cours."""

    session = SessionLocal()

    course = session.query(Course).filter_by(id=course_id).first()

    if course is None:
        session.close()
        return False, "Cours introuvable."

    session.delete(course)
    session.commit()
    session.close()

    return True, "Cours supprimé avec succès."