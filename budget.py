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
