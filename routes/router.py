from server import app
from controller.control import *

@app.route("/")
def ruta_prueba():
    return function_ruta_prueba()

@app.route("/register_page")
def register_page():
    return function_register_page()

@app.route("/register_user", methods=["POST"])
def register_user():
    return function_register_user()