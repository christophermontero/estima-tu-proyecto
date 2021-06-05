from flask import Flask, jsonify, request

from db import db_session, init_db
from model import Proyecto
from sqlalchemy.orm import joinedload

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False



init_db()


@app.route("/proyectos", methods=["POST"])
def create_proyecto():
    data = request.json

    if data["nombreProyecto"] is None:
        return jsonify({"mensaje": "error"}), 400

    proyecto = Proyecto.create(
        data["idProyecto"], data["nombreProyecto"], data["descProyecto"]
    )

    return jsonify({"proyectos": proyecto.toJson()})


@app.route("/proyectos", methods=["GET"])
def get_proyectos():
    proyectos = [proyecto.toJson() for proyecto in Proyecto.query.all()]

    return jsonify({"proyectos": proyectos})


@app.route("/proyectos/<idProyecto>", methods=["GET"])
def get_proyecto(idProyecto):
    proyecto = Proyecto.query.filter_by(idProyecto=idProyecto).first()
    if proyecto is None:
        return jsonify({"message": "El proyecto no existe"}), 404

    return jsonify({"proyecto": proyecto.toJson()})


@app.route("/proyectos/modulos/<idProyecto>", methods=["GET"])
def get_proyecto_y_modulos(idProyecto):
    
    proyecto = Proyecto.query.options(joinedload('modulos')).filter_by(idProyecto=idProyecto).first()

    if proyecto is None:
        return jsonify({"message": "El proyecto no existe"}), 404

    return jsonify({"proyecto": proyecto.toJsonWithModules()})

@app.route("/proyectos/modulos/funciones/<idProyecto>", methods=["GET"])
def get_proyecto_y_modulos_y_funciones(idProyecto):
    
    proyecto = Proyecto.query.options(joinedload('modulos').joinedload('funciones')).filter_by(idProyecto=idProyecto).first()

    if proyecto is None:
        return jsonify({"message": "El proyecto no existe"}), 404

    return jsonify({"proyecto": proyecto.toJsonWithModulesAndFunctions()})

@app.route("/proyectos/<idProyecto>", methods=["DELETE"])
def delete_proyecto(idProyecto):
    proyecto = Proyecto.query.filter_by(idProyecto=idProyecto).first()

    confirmation = Proyecto.delete(proyecto)

    return jsonify({"proyectos": confirmation})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
