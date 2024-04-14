from py_tube_transcribe.transcribe import Transcribe
from py_tube_transcribe.header import Header

if __name__ == "__main__":
    header = Header()
    header.info()

    print("\n")

    transcribe = Transcribe()
    video_url = input("Enter the YouTube video link: ").split('&')[0]
    video_file = transcribe.download_video(video_url)

    if video_file:
        audio_file = transcribe.extract_audio(video_file)
        if audio_file:
            transcribe.transcribe_audio(audio_file)
    else:
        print("❌ The video could not be downloaded.")