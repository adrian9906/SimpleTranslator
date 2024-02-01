from gtts import gTTS
import pyttsx3

def textToAudio(text):
    
    engine = pyttsx3.init()
    
    engine.say(text)
    
    engine.runAndWait()
    