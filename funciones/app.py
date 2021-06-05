from flask import Flask, jsonify, request

from db import db_session, init_db
from model import Funcion

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False



init_db()

@app.route("/funciones", methods=["POST"])
def create_funcion():
    data = request.json

    if data["nombreFuncion"] is None:
        return jsonify({"mensaje": "error"}), 400

    funcion = Funcion.create(
        data["idFuncion"], data["nombreFuncion"], data["numCampos"], data["numObjetos"], 
        data["complejidad"], data["modulo_id"],
    )

    return jsonify({"funcion": funcion.toJson()})



@app.route("/funciones", methods=["GET"])
def get_funciones():
    funciones = [funcion.toJson() for funcion in Funcion.query.all()]

    return jsonify({"funciones": funciones})


@app.route("/funciones/<idFuncion>", methods=["GET"])
def get_funcion(idFuncion):
    funcion = Funcion.query.filter_by(idFuncion=idFuncion).first()
    if funcion is None:
        return jsonify({"message": "La función no existe"}), 404

    return jsonify({"funcion": funcion.toJson()})


@app.route("/funciones/porModulo/<idModule>", methods=["GET"])
def get_funcion_byModule(idModule):

    m = [function.toJson() for function in Funcion.query.filter_by(modulo_id=idModule).all()]

    return jsonify({"funcion": m})


@app.route("/funciones/<idFuncion>", methods=["DELETE"])
def delete_funcion(idFuncion):
    function = Funcion.query.filter_by(idFuncion=idFuncion).first()

    confirmation = Funcion.delete(function)

    return jsonify({"modulos": confirmation})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
