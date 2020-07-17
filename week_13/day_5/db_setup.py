import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    completed = Column(Boolean(), default=False)


engine = create_engine("sqlite:///todos.db")

Base.metadata.create_all(engine)
