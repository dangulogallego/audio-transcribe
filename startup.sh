#!/bin/bash

# Descarga y extrae FFmpeg
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
tar xvf ffmpeg-release-amd64-static.tar.xz
mv ffmpeg-*-amd64-static/ffmpeg /usr/local/bin/

# Instala las dependencias de Python (asumiendo que ya tienes un entorno virtual activado)
pip install -r requirements.txt

# Define el comando para iniciar Quart con Gunicorn
gunicorn --bind 0.0.0.0:8000 quart.app:app
