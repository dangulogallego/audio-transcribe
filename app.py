import whisper
from quart import Quart, request, jsonify
import aiofiles
import os

app = Quart(__name__)

# Cargar el modelo "tiny"
model = whisper.load_model("small")

@app.route('/transcribe', methods=['POST'])
async def transcribe():
    # Obtener el archivo enviado en la solicitud
    files = await request.files
    audio_file = files.get('audio')
    if not audio_file:
        return jsonify({"error": "No audio file provided"}), 400

    # Guardar el archivo temporalmente
    audio_path = os.path.join("/tmp", audio_file.filename)
    async with aiofiles.open(audio_path, 'wb') as f:
        await f.write(audio_file.read())

    # Transcribir el audio
    result = model.transcribe(audio_path)
    transcription_text = result["text"]

    # Eliminar el archivo temporal
    os.remove(audio_path)

    # Retornar la transcripción en formato JSON
    return jsonify({"transcription": transcription_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)