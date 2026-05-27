import requests

def consumir_clases():
    url = "http://localhost:8080/clases"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos