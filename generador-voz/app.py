"""
Generador de Voz
================
Convierte texto en audio con voces realistas y GRATUITAS.

Usa edge-tts (las voces neuronales de Microsoft Edge): suenan muy naturales,
no necesitan clave de API y no tienen costo. Solo requiere conexion a internet.

Para ejecutar:
    pip install -r requirements.txt
    python app.py
Luego abre http://localhost:5000 en tu navegador.
"""

import asyncio
import io
import os
import re

import edge_tts
from flask import Flask, jsonify, render_template, request, send_file

app = Flask(__name__)

# Limites de seguridad y validacion.
MAX_CARACTERES = 5000
PATRON_VOZ = re.compile(r"^[a-z]{2}-[A-Z]{2}-[A-Za-z0-9]+Neural$")
PATRON_VELOCIDAD = re.compile(r"^[+-]\d{1,3}%$")

# Voces en espanol recomendadas. Puedes ver la lista completa en /voces.
VOCES_DESTACADAS = [
    {"id": "es-MX-DaliaNeural", "nombre": "Dalia — Mexico (femenina)"},
    {"id": "es-MX-JorgeNeural", "nombre": "Jorge — Mexico (masculina)"},
    {"id": "es-CO-SalomeNeural", "nombre": "Salome — Colombia (femenina)"},
    {"id": "es-CO-GonzaloNeural", "nombre": "Gonzalo — Colombia (masculina)"},
    {"id": "es-ES-ElviraNeural", "nombre": "Elvira — Espana (femenina)"},
    {"id": "es-ES-AlvaroNeural", "nombre": "Alvaro — Espana (masculina)"},
    {"id": "es-AR-ElenaNeural", "nombre": "Elena — Argentina (femenina)"},
    {"id": "es-US-PalomaNeural", "nombre": "Paloma — EE.UU. (femenina)"},
]
IDS_VALIDOS = {v["id"] for v in VOCES_DESTACADAS}
VOZ_POR_DEFECTO = "es-MX-DaliaNeural"


@app.route("/")
def index():
    return render_template("index.html", voces=VOCES_DESTACADAS)


@app.route("/voces")
def listar_voces():
    """Devuelve TODAS las voces disponibles (no solo las destacadas)."""
    try:
        voces = asyncio.run(edge_tts.list_voices())
    except Exception as exc:  # pragma: no cover - depende de la red
        return jsonify({"error": f"No se pudieron obtener las voces: {exc}"}), 502
    resumen = [
        {
            "id": v.get("ShortName"),
            "idioma": v.get("Locale"),
            "genero": v.get("Gender"),
        }
        for v in voces
    ]
    return jsonify(resumen)


@app.route("/hablar", methods=["POST"])
def hablar():
    datos = request.get_json(silent=True) or {}
    texto = (datos.get("texto") or "").strip()
    voz = (datos.get("voz") or VOZ_POR_DEFECTO).strip()
    velocidad = (datos.get("velocidad") or "+0%").strip()

    # Validacion de la entrada.
    if not texto:
        return jsonify({"error": "Escribe algun texto primero."}), 400
    if len(texto) > MAX_CARACTERES:
        return (
            jsonify(
                {"error": f"El texto es muy largo (maximo {MAX_CARACTERES} caracteres)."}
            ),
            400,
        )
    if voz not in IDS_VALIDOS and not PATRON_VOZ.match(voz):
        return jsonify({"error": "La voz seleccionada no es valida."}), 400
    if not PATRON_VELOCIDAD.match(velocidad):
        velocidad = "+0%"

    try:
        audio = asyncio.run(_generar_audio(texto, voz, velocidad))
    except Exception as exc:  # pragma: no cover - depende de la red
        return jsonify({"error": f"No se pudo generar el audio: {exc}"}), 502

    return send_file(
        io.BytesIO(audio),
        mimetype="audio/mpeg",
        as_attachment=False,
        download_name="voz.mp3",
    )


async def _generar_audio(texto: str, voz: str, velocidad: str) -> bytes:
    """Genera el audio en memoria usando edge-tts y lo devuelve como bytes."""
    communicate = edge_tts.Communicate(texto, voz, rate=velocidad)
    buffer = bytearray()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            buffer.extend(chunk["data"])
    if not buffer:
        raise RuntimeError("El servicio no devolvio audio.")
    return bytes(buffer)


if __name__ == "__main__":
    # El modo debug esta APAGADO por defecto (es inseguro: expone una consola
    # que permite ejecutar codigo). Para activarlo solo en desarrollo local,
    # arranca con:  FLASK_DEBUG=1 python app.py
    debug = os.environ.get("FLASK_DEBUG") == "1"
    app.run(host="127.0.0.1", port=5000, debug=debug)
