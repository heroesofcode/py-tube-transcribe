import os
import ssl
import subprocess
import speech_recognition as sr
from pytube import YouTube

class Transcribe:
    def __init__(self):
        pass
    
    def download_video(self, url):
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
            
            youtube = YouTube(url)
            stream = youtube.streams.get_highest_resolution()
            output_path = os.path.join(os.getcwd(), "videos")
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            video_file = os.path.join(output_path, stream.default_filename)
            stream.download(output_path)
            print("✅ Download video")
            return video_file
        except Exception as e:
            print(f"❌ An error occurred during the download: {e}")
            return None

    def extract_audio(self, video_file):
        try:
            audio_file = video_file[:-4] + ".wav"

            command = ["ffmpeg", "-i", video_file, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", audio_file]
            subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

            print("✅ Extract full audio")
            return audio_file
        except Exception as e:
            print(f"❌ An error occurred while extracting the audio: {e}")
            return None

    def transcribe_audio(self, audio_file):
        try:
            if os.path.exists(audio_file):
                recognizer = sr.Recognizer()

                with sr.AudioFile(audio_file) as source:
                    audio_data = recognizer.record(source)

                text = recognizer.recognize_google(audio_data, language='pt-BR')
                print("✅ Transcription:")

                with open("trancription.txt", "w") as file:
                    file.write(text)

                print("✅ Generated transcription.txt file")
                return text
            else:
                print("❌ Audio file not found")
                return None
        except Exception as e:
            print(f"❌ An error occurred during transcription: {e}")
            return None