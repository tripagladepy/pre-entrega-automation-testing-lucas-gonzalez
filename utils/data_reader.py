import json
import os

def load_credentials():  #Devuelve la lista de credenciales desde data/credentials.json
    
    base = os.path.dirname(__file__)               # utils/
    path = os.path.join(base, "..", "data", "credentials.json")
    path = os.path.normpath(path)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
