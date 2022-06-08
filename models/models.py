from app import db 
from venv import create
from flask import Flask, request, jsonify # diccionarios de python los convienrte en Json y en response, objeto request
from flask_sqlalchemy import SQLAlchemy # libreria para BBDD - ORM mapeos de objetos a una base Relacional
from flask_cors import CORS # por seguridad Cros Origin
# create Post model

class Foro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Foro %r>' % self.title

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(80), nullable=False)
    foro_id = db.Column(db.Integer, db.ForeignKey('foro.id'), nullable=False)
    foro = db.relationship('Foro', 
    backref=db.backref('subjects', lazy=True))

    def __repr__(self):
        return '<Subject %r>' % self.title

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(80), nullable=False)
    image_url = db.Column(db.String(180), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    subject = db.relationship('Subject', 
    backref=db.backref('posts', lazy=True))


    def __repr__(self):
        return '<Post %r>' % self.title
