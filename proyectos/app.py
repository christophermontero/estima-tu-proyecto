from flask import Flask, app, jsonify
from flask.globals import request
from db import db_session, init_db
from model import TestTable, Proyecto, db


def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

def create_app(enviroment):
    main = Flask(__name__)

    main.config.from_object(enviroment)

    with main.app_context():
        db.init_app(main)
        db.create_all()

    return main


init_db()

@app.route('/api/proyectos/', methods=['POST'])
def create_proyecto():
    json = request.get_json(force=True)

    if json.get('nombreProyecto') is None:
        return jsonify({'mensaje': 'Bad request'}), 400

    proyecto = Proyecto.create(json['nombreProyecto'])

    return jsonify({'proyecto': proyecto.json() })


@app.route('/api/proyectos', methods=['GET'])
def get_proyectos():
    proyectos = [ Proyecto.json() for proyecto in Proyecto.query.all() ] 
    return jsonify({'proyectos': proyectos })


@app.route('/api/proyectos/<idProyecto>', methods=['GET'])
def get_user(idProyecto):
    proyecto = Proyecto.query.filter_by(idProyecto=idProyecto).first()
    if proyecto is None:
        return jsonify({'message': 'El proyecto no existe'}), 404

    return jsonify({'proyecto': proyecto.json() })

def json(self):
        return {
            'idProyecto': self.idProyecto,
            'nombreProyecto': self.nombreProyecto,
            'descProyecto': self.descProyecto
        }

if __name__ == '__main__':
    app.run(debug=True)