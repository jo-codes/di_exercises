from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Todo, Base

engine = create_engine("sqlite:///todos.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

testTodo = Todo(title="Test DB", completed=True)
session.add(testTodo)
session.commit()