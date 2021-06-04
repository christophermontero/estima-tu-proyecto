from flask import Flask, jsonify, request

from db import db_session, init_db
from model import Funcion

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False



init_db()




@app.route("/funciones", methods=["GET"])
def get_funciones():
    funciones = [funcion.toJson() for funcion in Funcion.query.all()]

    return jsonify({"funciones": funciones})





if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
