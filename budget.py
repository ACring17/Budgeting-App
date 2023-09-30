import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField#,BooleanField,DateTimeField,RadioField,SelectField,TextAreaField,TextField
from wtforms.validators import DataRequired

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Configuring the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///'+os.path.join(basedir,'data.postgresql')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Connecting the SQL
db = SQLAlchemy(app)

Migrate(app,db)

app.config['SECRET_KEY'] = 'mysecretkey'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


# Connecting the templates
@app.route('/')
def index():
    user_logged_in = True
    return render_template('index.html', user_logged_in=user_logged_in)
