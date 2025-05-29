import json
from deep_translator import GoogleTranslator
import time

def obtener_prefijo(texto, actor):
    if "usuario" in actor.lower():
        return "Usuario".ljust(20)
    elif "formulario" in texto.lower():
        return "Consulta".ljust(20)
    else:
        return "OTRO".ljust(20)

def traducir_interacciones(interacciones):
    for item in interacciones:
        texto_original = item.get("texto", "")
        actor = item.get("actor", "")
        
        if texto_original and texto_original.strip():
            prefijo = obtener_prefijo(texto_original, actor)
            
            try:
                time.sleep(0.5)
                translator = GoogleTranslator(source='auto', target='en')
                texto_traducido = translator.translate(texto_original)
                item["texto"] = f"{texto_traducido}"
                
            except Exception as e:
                item["texto"] = f"{texto_original}"
        else:
            item["texto"] = ""
        
        if "interacciones" in item and item["interacciones"]:
            traducir_interacciones(item["interacciones"])

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

traducir_interacciones(data)

with open("conversacion_traducida.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)