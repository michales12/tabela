from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

@app.route('/')
def index():
    user={
        user: "Michał"
    }
    return render_template('tekst.html', user=user)
