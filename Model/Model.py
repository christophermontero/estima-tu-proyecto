from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tasks.db'

db = SQLAlchemy(app)

class Proyecto(db.Model):

    idProyecto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreProyecto = db.Column(db.String(50))
    descProyecto = db.Column(db.String(150))
    modulos = db.relationship('Modulo', backref='proyecto', lazy=True)


class Modulo(db.Model):

    idModulo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreModulo = db.Column(db.String(50))
    descModulo = db.Column(db.String(150))
    proyecto_id = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))
    funciones = db.relationship('Funcion', backref='modulo', lazy=True)

class Funcion(db.Model):

    idFuncion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreFuncion = db.Column(db.String(50))
    numCampos = db.Column(db.Integer)
    numObjetos = db.Column(db.Integer)
    proyecto_id = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))
    modulo_id = db.Column(db.Integer, db.ForeignKey('modulo.idModulo'))