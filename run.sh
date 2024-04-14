#!/bin/bash

if [[ "$(uname)" == "Linux" ]]; then
    echo "Operational system: Linux"
    if ! command -v ffmpeg &> /dev/null; then
        echo "FFmpeg não encontrado. Instalando..."
        sudo apt-get update
        sudo apt-get install ffmpeg -y
        python3 -m py_tube_transcribe
    else
        python3 -m py_tube_transcribe
    fi
elif [[ "$(uname)" == "Darwin" ]]; then
    echo "Operational system:  macOS"
    if ! command -v ffmpeg &> /dev/null; then
        brew install ffmpeg
        python3 -m py_tube_transcribe
    else
        python3 -m py_tube_transcribe
    fi
elif [[ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]]; then
    echo "Operational system: Windows"
    if ! command -v ffmpeg &> /dev/null; then
        echo "FFmpeg not found. Download and install manually from: https://ffmpeg.org/download.html"
        exit 1
    else
        python3 -m py_tube_transcribe
    fi
else
    echo "Operating system not supported."
    exit 1
fi
