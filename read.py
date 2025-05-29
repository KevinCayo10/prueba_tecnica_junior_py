import json

respuesta = ["respuesta"]
indicacion = ["indicacion"]
consulta = ["consulta"]
otros = ["otros"]

def obtener_prefijo(texto, actor):
    if "usuario" in actor.lower():
        return "Usuario".ljust(20)
    elif "formulario" in texto.lower():
        return "Consulta".ljust(20)
    else:
        return "OTRO".ljust(20)

def traducir_interacciones(interacciones):
    for item in interacciones:
        id_original = item.get("id", "")
        prefijo = obtener_prefijo(texto_original, actor)
        primeros_20 = id_original[20:]
        item["id"] = primeros_20 + "HOLA"
        
        if "interacciones" in item and item["interacciones"]:
            traducir_interacciones(item["interacciones"])

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

traducir_interacciones(data)

with open("conversacion_id.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Modificación completada. Archivo generado: conversacion_id.json")