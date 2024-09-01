from server import app
from controller.control import *

@app.route("/")
def ruta_prueba():
    return function_home_page()

@app.route("/register_page")
def register_page():
    return function_register_page()

@app.route("/consult_page")
def consult_page():
    return function_consult_page()

@app.route("/register_user", methods=["POST"])
def register_user():
    return function_register_user()

@app.route("/consult_user", methods=["POST"])
def consult_user():
    print("Estoy consultando usuarios")
    return function_consult_user()