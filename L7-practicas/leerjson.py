import json

with open("Datos.json") as m:
    data = json.load(m)
    for e in m:
        print(e)
