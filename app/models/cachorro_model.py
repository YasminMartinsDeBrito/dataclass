from app.configs.database import db

from sqlalchemy import Column, Integer, String
from dataclasses import dataclass

@dataclass
class CachorroModel(db.Model):
    id : int
    nome : str
    raca : str
    idade : int

    __tablename__ = 'cachorros'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    raca = Column(String, nullable=False)
    idade = Column(Integer)

    