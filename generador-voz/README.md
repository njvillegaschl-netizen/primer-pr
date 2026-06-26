# 🔊 Generador de Voz

Una app web sencilla para convertir **texto en audio** con voces realistas y
**gratuitas**, en español (y muchos otros idiomas).

Usa [`edge-tts`](https://github.com/rany2/edge-tts), que aprovecha las voces
neuronales de Microsoft Edge: suenan muy naturales, **no necesitan clave de API
y no tienen costo**. Solo hace falta conexión a internet.

---

## ✅ Requisitos

- **Python 3.9 o superior** instalado. Para comprobarlo, abre una terminal y escribe:
  ```bash
  python --version
  ```
  (En algunos sistemas el comando es `python3`.)

---

## 🚀 Cómo ejecutarla (paso a paso)

1. **Abre una terminal** y entra a la carpeta de la app:
   ```bash
   cd generador-voz
   ```

2. **(Recomendado) Crea un entorno virtual** para no mezclar dependencias:
   ```bash
   python -m venv venv
   ```
   Actívalo:
   - **Windows:** `venv\Scripts\activate`
   - **Mac / Linux:** `source venv/bin/activate`

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicia la app:**
   ```bash
   python app.py
   ```

5. **Abre tu navegador** en 👉 <http://localhost:5000>

6. Escribe tu texto, elige una voz y velocidad, y pulsa **«Generar voz»**.
   Podrás escucharlo y descargarlo como archivo MP3.

Para detener la app, vuelve a la terminal y pulsa `Ctrl + C`.

---

## 🎙️ Voces disponibles

La app trae varias voces destacadas en español (México, Colombia, Venezuela,
Perú, Chile, España, Argentina, EE.UU.). Si quieres ver **todas** las voces
disponibles (cientos, en muchos idiomas), abre <http://localhost:5000/voces>
mientras la app está corriendo. Cada voz tiene un identificador como
`es-MX-DaliaNeural`.

### 🎚️ Control de gravedad (tono)

Además de la velocidad, puedes ajustar el **tono** de la voz con el control
«Gravedad / tono»: muévelo hacia la izquierda para que suene **más grave**
(profunda) o hacia la derecha para **más aguda**. Es útil, por ejemplo, para
darle un tono de narrador más profundo a una voz masculina.

---

## ❓ Problemas comunes

- **`python` no se reconoce:** prueba con `python3` en lugar de `python`.
- **No genera audio / error de red:** `edge-tts` necesita internet para
  conectarse al servicio de voz de Microsoft. Revisa tu conexión.
- **El puerto 5000 está ocupado:** cambia el número en la última línea de
  `app.py` (por ejemplo, `port=5001`).

---

Hecho como proyecto de práctica. ¡Disfrútalo! 🎉
