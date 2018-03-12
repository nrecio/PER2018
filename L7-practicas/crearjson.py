
import json
data = {
 'name' : 'Noe',
 'edad' : 26,
 'apellido' : "Recio"
}

with open("Datos.json","w") as f:
    f.write(json.dumps(data))
f.close()
