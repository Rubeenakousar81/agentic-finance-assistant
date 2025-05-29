import whisper
import pyttsx3

def transcribe(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result['text']

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
