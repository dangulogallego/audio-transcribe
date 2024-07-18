import whisper
from flask import Flask, request, jsonify
import os
import tempfile

app = Flask(__name__)

# Cargar el modelo "tiny"
model = whisper.load_model("small")

@app.route('/transcribe', methods=['POST'])
def transcribe():
    # Obtener el archivo enviado en la solicitud
    audio_file = request.files.get('audio')
    if not audio_file:
        return jsonify({"error": "No audio file provided"}), 400

    # Guardar el archivo temporalmente
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        audio_path = tmp.name
        audio_file.save(audio_path)

    # Transcribir el audio
    result = model.transcribe(audio_path)
    transcription_text = result["text"]

    # Eliminar el archivo temporal
    os.remove(audio_path)

    # Retornar la transcripción en formato JSON
    return jsonify({"transcription": transcription_text})

if __name__ == '__main__':
    app.run()
