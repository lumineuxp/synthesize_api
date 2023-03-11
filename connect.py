from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()

class Tales(db.Model):
    __tablename__ = "tales"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    story = db.Column(db.String, nullable=False) 
    cover_img = db.Column(db.String, nullable=False)