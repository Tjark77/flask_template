# Wird von der Datenbank generiert
# Objekte als Repräsentation der Datenbank
from sqlalchemy import Column, ForeignKey, String, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class Example(Base):
    __tablename__ = 'foo'
    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(80), nullable=False)