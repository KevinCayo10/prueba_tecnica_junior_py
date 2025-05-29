import json

respuesta = ["respuesta"]
indicacion = ["indicacion"]
consulta = ["consulta"]
otros = ["otros"]

def obtener_categoria(texto):
    texto_lower = texto.lower()
    
    if any(palabra in texto_lower for palabra in respuesta):
        return "RESPUESTA"
    elif any(palabra in texto_lower for palabra in indicacion):
        return "INDICACION"
    elif any(palabra in texto_lower for palabra in consulta):
        return "CONSULTA"
    elif any(palabra in texto_lower for palabra in otros):
        return "OTROS"
    else:
        return "HOLA"

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
        texto_original = item.get("texto", "")
        actor = item.get("actor", "")
        
        prefijo = obtener_prefijo(texto_original, actor)
        primeros_20 = id_original[:20]
        categoria = obtener_categoria(texto_original)
        item["id"] = primeros_20 + categoria
                
        if "interacciones" in item and item["interacciones"]:
            traducir_interacciones(item["interacciones"])

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

traducir_interacciones(data)

with open("conversacion_id.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)