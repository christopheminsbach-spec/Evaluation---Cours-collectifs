from sqlalchemy import Column, Integer, String, Float
from database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # Informations du cours

    name = Column(String(100), nullable=False)
    coach = Column(String(100), nullable=False)


    # Nombres de places
    capacity = Column(Integer, nullable=False)
    registered_count = Column(Integer, default=0)

    # prix du cours

    price = Column(Float, nullable=False)

    #-------------- Propriétés --------------

    @property
    def remaining_places (self):
        """Nombre de places restantes."""
        return self.capacity - self.registered_count
    
    @property
    def current_turnover(self):
        """Chiffre d' affaires actuel."""
        return self.registered_count * self.price
    
    @property
    def potential_turnover(self):
        """Chiffre d'affaires potentiel."""
        return self.registered_count >= self.capacity
    
    @property
    def is_full(self):
        return self.registered_count >= self.capacity
    
    # ---------------- Affichage ----------------

    def __repr__(self):
        return (
            f"<Course(id={self.id}) , "
            f"name='{self.name}', "
            f"coach='{self.coach}', "
            f"places={self.registered_count}/{self.capacity})>"
        )
