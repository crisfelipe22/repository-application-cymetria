from flask import render_template, request
from database.db import *
from controller.s3_administrator import conecction_s3, save_file, update_file

def function_ruta_prueba():
    return "Hola soy el user infraestructura"

def function_register_page():
    return render_template("register.html")

def function_register_user():
    data_user = request.form
    data_file = request.files
    id, name, lastname, birthday = request.form["id"], request.form["name"], request.form["lastname"], request.form["birthday"]
    photo = data_file["photo"]
    # insert_register_database(id, name, lastname, birthday)
    session_s3 = conecction_s3()
    photo_path = save_file(id, photo)
    update_file(session_s3, photo, photo_path, id)
    return "Register user"