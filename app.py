from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

import src.models
import src.login
import src.registrar_asistencia
import src.listado
import src.consultar
import src.informe

if __name__ == "__main__":
    app.run()