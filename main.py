from flask import Flask, request
from flask.helpers import url_for
from flask_cors import CORS
from werkzeug.utils import redirect
import json
from grammar import Analizar
app = Flask(__name__)
CORS(app) #Permite hacer consultas
instru=""
@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        entrada = request.data.decode("utf-8")
        entrada = json.loads(entrada)
        codigo = entrada["msg"]
        print("Mandado desde Angular:  ", str(codigo))
        global instru
        instru=Analizar(str(codigo))
    
        return redirect(url_for("saludo"))

@app.route('/saludo', methods = ["GET"])
def saludo():
    print(instru)
    return {'msg':instru}

if __name__ == '__main__':
    app.run(debug = True, port=6200)