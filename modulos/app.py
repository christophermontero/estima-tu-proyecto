from flask import Flask, jsonify, request

from db import db_session, init_db
from model import Modulo 


app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False

init_db()


@app.route("/modulos", methods=["POST"])
def create_modulos():
    data = request.json
    
    if data["nombreModulo"] is None:
        return jsonify({"mensaje": "error"}), 400

    modulo = Modulo.create(
        data["idModulo"], data["nombreModulo"], data["descModulo"], data["proyecto_id"]
    )

    return jsonify({"modulos": modulo.toJson()})
    
    
@app.route("/modulos/<moduloId>", methods=["DELETE"])
def delete_modulo(moduloId):
    modulo = Modulo.query.filter_by(idModulo=moduloId).first()

    confirmation = Modulo.delete(modulo)

    return jsonify({"modulos": confirmation})
    


@app.route("/modulos/<proyectoId>", methods=["GET"])
def get_user(proyectoId):

    m = [modulo.toJson() for modulo in Modulo.query.filter_by(proyecto_id=proyectoId).all()]

    return jsonify({"modulos": m})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
