import flask_sqlalchemy, app
from datetime import datetime
import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm



# URI scheme: postgresql://<username>:<password>@<hostname>:<port>/<database-name>
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://elias:lakers32@localhost/postgres'  
db = flask_sqlalchemy.SQLAlchemy(app)

class user(db.Model):
    userID = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(120))
    imgLink = db.Column(db.String(300))
    userMessages = db.relationship('message', backref=db.backref('user',lazy='joined'),lazy='dynamic')
    
    def __init__(self, username, imgLink):
        self.username = username
        self.imgLink = imgLink
        
    # @property
    # def serialize(self):
    #     return {'userID': self.userID, 'link': self.imgLink}


    def __repr__(self):
        return '<User: {name: %r, imgLink:  %r>' %(self.username,self.imgLink)