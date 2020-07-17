from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Todo

engine = create_engine("sqlite:///todos.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route("/")
def showTodos():
    todos = session.query(Todo).all()
    return render_template("index.html", todos=todos)


@app.route("/new", methods=["GET", "POST"])
def newTodo():
    if request.method == "POST":
        newTodo = Todo(title=request.form["name"])
        session.add(newTodo)
        session.commit()
        return render_template("index.html", todos=todos)


app.config["DEBUG"] = True
app.run(host="0.0.0.0", port="5000")

