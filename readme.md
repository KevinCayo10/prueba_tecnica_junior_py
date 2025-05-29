# 🧠 Estrategia de Traducción y Categorización de Interacciones

Este proyecto implementa una estrategia para traducir automáticamente conversaciones estructuradas en formato JSON y categorizar algunas de las interacciones según el rol del actor o el contenido del texto.

---

## 📌 Objetivo

Procesar un archivo `data.json` con una estructura de interacciones tipo árbol, traducir los textos al inglés utilizando `GoogleTranslator`, y categorizar ciertos fragmentos mediante prefijos interpretativos.

---

## ⚙️ Descripción del Script

El script realiza las siguientes operaciones:

### 1. Categorización inicial por prefijo

Se asigna un prefijo simple a cada texto mediante la función `obtener_prefijo`, con base en reglas heurísticas:

- Si el actor contiene la palabra `"usuario"` → `Usuario`
- Si el texto contiene la palabra `"formulario"` → `Consulta`
- En cualquier otro caso → `OTRO`

Estos prefijos permiten una clasificación inicial para análisis posterior.

---

### 2. Traducción automática

Se utiliza la librería `deep_translator.GoogleTranslator` para traducir el texto original al inglés:

- Idioma de origen: detectado automáticamente.
- Idioma de destino: inglés (`en`).
- Se incorpora una pausa de `0.5 segundos` entre solicitudes para evitar restricciones del servicio de traducción.

---

### 3. Procesamiento recursivo

Dado que las interacciones pueden estar anidadas dentro de otras, el script utiliza una función recursiva (`traducir_interacciones`) que recorre cada nivel del árbol conversacional para aplicar la traducción a todos los textos.

---

### 4. Persistencia

Una vez procesados los datos, se genera un nuevo archivo `conversacion_traducida.json` que mantiene la estructura original pero con los textos traducidos.

---

## 🧪 Requisitos

Antes de ejecutar el script, instala la dependencia necesaria:

```bash
pip install deep-translator
