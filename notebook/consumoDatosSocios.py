import requests

def consumir_socios():
    url = "http://localhost:8080/socios"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos