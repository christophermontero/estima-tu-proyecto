from flask import Flask, jsonify, request

from db import db_session, init_db
from model import Proyecto

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


@app.route("/api/proyectos/<idProyecto>", methods=["GET"])
def get_user(idProyecto):
    proyecto = Proyecto.query.filter_by(idProyecto=idProyecto).first()
    if proyecto is None:
        return jsonify({"message": "El proyecto no existe"}), 404

    return jsonify({"proyecto": proyecto.toJson()})



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
