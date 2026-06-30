from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Nom de la base de données SQLite
DATABASE_URL = "sqlite:///studio_booking.db"

"Création du moteur SQLAlchemy"
engine = create_engine(
    DATABASE_URL,
    echo=False # Mettre true pour afficher les requête SQL
)

# Création de la session ORM
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Classe de base pour les modéles ORM
Base = declarative_base()