from database import SessionLocal
from models import Course

def seed():
    session = SessionLocal()

    if session.query(Course).count() == 0:

        courses = [
            Course(name="Yoga", coach="Emma", capacity=12, price=30),
            Course(name="Pilates", coach="Nora", capacity=10, price=35),
            Course(name="Cross Training", coach="Lucas", capacity=15, price=40),
            Course(name="Cardio Boxing", coach="Sarah", capacity=20, price=45),
            Course(name="Stretching", coach="Chloé", capacity=8, price=20),
        ]

        session.add_all(courses)
        session.commit()

    session.close()