
# las structuras que pueden manejar las funciones
existing_structs = ["client", "developer"]

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
    "id": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "developer_id" : "",
    "password": "",
    "created_at": "",
    "type_obj": "client"
}

developer = {
    "id": "",
    "active_pro": {},
    "first_name": "",
    "last_name": "",
    "email": "",
    "client_id" : "",
    "password": "",
    "created_at": "",
    "type_obj": "developer"
}
