
"""
database.py
------------
Configuration de SQLAlchemy 2.

Ce fichier contient :

- la connexion à SQLite
- le moteur SQLAlchemy
- la création des sessions
- la classe Base utilisée par les modèles ORM
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

# ---------------------------------------------------
# Adresse de la base SQLite
# ---------------------------------------------------

DATABASE_URL = "sqlite:///studio_booking.db"

# ---------------------------------------------------
# Création du moteur SQLAlchemy
#
# Le moteur permet de communiquer avec la base.
#
# echo=False :
#   n'affiche pas les requêtes SQL.
#
# echo=True :
#   affiche toutes les requêtes SQL
#   (pratique pendant le développement).
# ---------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    echo=False
)

# ---------------------------------------------------
# Classe de base ORM
#
# Tous les modèles hériteront de Base.
# ---------------------------------------------------

class Base(DeclarativeBase):
    pass

# ---------------------------------------------------
# Fabrique de sessions
#
# Une session permet :
#
# - de lire des données
# - d'ajouter des données
# - de modifier des données
# - de supprimer des données
#
# Chaque opération CRUD ouvrira une session.
# ---------------------------------------------------

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)