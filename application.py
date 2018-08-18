import os

from flask import Flask, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
#Log in
# "SELECT * FROM users WHERE (username = 'input_username') AND (password = 'input_password')";
    flights = db.execute("SELECT * FROM flights").fetchall()
#    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("boo.html", flights=flights)


#    for table in dbtables:
#        return "{table.table_name}"
#    return "Project 1: TODO"
