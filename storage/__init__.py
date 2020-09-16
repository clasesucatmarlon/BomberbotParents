
existing_structs = ["client", "developer", "proy"]

#   en saved se guardaran todos los objetos guardados con:
#
#   .reload
#   .save
#
#   Sera el json que se maneje para utilizar mongo db   
saved = []

# Comprobante de que el json ya fue previamente cargado (evitar sobrecarga)
json_loaded = False
### Estructuras base

client = {
    "_id": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "freelancer_id" : "",
    "password": "",
    "created_at": "",
    "type_obj": "client"
}

freelancer = {
    "_id": "",
    "active_pro": {},
    "first_name": "",
    "last_name": "",
    "email": "",
    "client_id" : "",
    "password": "",
    "created_at": "",
    "type_obj": "freelancer"
}

proy = {
    "_id": "",
    "title": "",
    "resumen": "",
    "type_proyect": "",
    "fecha_inicio": "",
    "fecha_limite": "",
    "clientes_ids": [],
    "freelancers_id": [],
    "type_obj": "proy"
}
