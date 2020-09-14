"""
#####   mision y vision  #####
 Cada diccionario tendra un id statico a la hora de agregar nuevos valores
 No pueden haber id repetidas, o no se podra guardar en la lista
 cada implementacion debe recibir la estructura que va a manejar
"""
import uuid
import datetime
import os.path
import json
from storage import *

"""
 new_id : me retorna un nuevo id para una copia de alguna estructura
 @struct: structura base a inicializar
 Return: Nueva copia de alguna estructura base con id unica
"""
def new_id(struct):
    if struct["type_obj"] in existing_structs:
        struct = struct.copy()
        struct["id"] = str(uuid.uuid1())
        struct["created_at"] = datetime.datetime.now()
        return struct
"""
 pushear datos a una structura
 Esta implementacion agrega o actualiza valores
 Es obligatorio que los valores a agregar coincidan con alguna estructura base
"""
def push_data(struct, **args):
    skip = ["id", "type_obj"]
    for key in args.keys():
        if key not in struct.keys():
            print(f"El dato a modificar {key} no es valido para la estructura {struct['type_obj']}")
            return struct
        if key in skip:
            del args[key]
    args["created_at"] = datetime.datetime.now()
    struct.update(args)


"""
    save guarda la estrucura que se la pasa en la lista global saved.
    saved es una lista en __init__ se encargara de recolectar todas las estructuras

"""
def save(struct):
    if "type_obj" not in struct.keys():
        print("Esta estructura debe contener type_obj")
        return
    if struct["type_obj"] not in existing_structs:
        print("El tipo de type_obj no es valido")
        return
    for st in saved:
        if st["id"] == struct["id"]:
            print("Estructura ya existente, omitiendo carga")
            return
    else:
        saved.append(struct)

"""
    commit - Los datos guardados en saved se pueden commitear directamente a una coleccion de mongo
    o bien se pueden guardar en json segun la necesidad
"""
def commit(type_storage, *args):
    if type_storage == "mongo" and args:
        return "en construccion"
    
    if type_storage == "jsonfile":
        if saved:
            # Convertir todos las clases datetime en strings primero.
            for struct in saved:
                if type(struct["created_at"]) not in [str]:
                    struct["created_at"] = struct["created_at"].strftime('%Y-%m-%dT%H:%M:%S.%f')
            

            # Guardo en el archivo json todos los datos existentes en saved
            with open("data.json", "w") as file:
                json.dump(saved, file, indent=4, sort_keys=True, default=str)
                print("Datos guardados en archivo json")

"""
    get_json_data - Devuelve todos los datos de data.json mientras exista.
    sirve para cargar de datos la variable saved en caso de que se necesite
"""
def get_json_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as file_loaded:
           return json.loads(file_loaded.read())


def idx(_id):
    for i in range(len(saved)):
        if saved[i]["id"] == _id:
            return i
