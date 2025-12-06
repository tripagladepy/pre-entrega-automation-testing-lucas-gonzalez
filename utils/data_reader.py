import json
import os

def load_json(filename):   #Carga un archivo JSON desde la carpeta data y devuelve su contenido
    base = os.path.dirname(__file__)
    path = os.path.normpath(os.path.join(base, "..", "data", filename))
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def load_credentials():  #Devuelve la lista de credenciales desde data/credentials.json
    return load_json("credentials.json")


def load_products():   #Devuelve la lista de productos desde data/products.json
    return load_json("products.json")