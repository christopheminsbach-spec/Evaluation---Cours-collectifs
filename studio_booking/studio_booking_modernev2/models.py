"""
models.py
----------
Ce fichier contient les modèles ORM.

Un modèle ORM est une classe Python qui représente une table
dans la base de données.
"""

# Types SQLAlchemy
from sqlalchemy import String, Integer, Float

# Nouveautés SQLAlchemy 2
from sqlalchemy.orm import Mapped, mapped_column

# Classe de base créée dans database.py
from studio_booking.studio_booking_modernev2.database import Base


class Course(Base):
    """
    Représente un cours collectif.

    Chaque objet Course correspond à une ligne de la table 'courses'.
    """

    # Nom de la table SQLite
    __tablename__ = "courses"

    # ----------------------------
    # Colonnes de la table
    # ----------------------------

    # Clé primaire
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    # Nom du cours
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # Nom du coach
    coach: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # Nombre maximum de participants
    capacity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    # Nombre de participants inscrits
    registered_count: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    # Prix du cours
    price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    # ----------------------------
    # Propriétés calculées
    # ----------------------------

    @property
    def remaining_places(self) -> int:
        """
        Calcule automatiquement le nombre
        de places restantes.
        """
        return self.capacity - self.registered_count

    @property
    def current_turnover(self) -> float:
        """
        Calcule le chiffre d'affaires actuel.
        """
        return self.registered_count * self.price

    @property
    def potential_turnover(self) -> float:
        """
        Calcule le chiffre d'affaires maximum
        si toutes les places sont vendues.
        """
        return self.capacity * self.price

    @property
    def is_full(self) -> bool:
        """
        Indique si le cours est complet.
        """
        return self.registered_count >= self.capacity

    # ----------------------------
    # Affichage de l'objet
    # ----------------------------

    def __repr__(self) -> str:
        return (
            f"<Course("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"coach='{self.coach}', "
            f"registered={self.registered_count}/{self.capacity}"
            f")>"
        )