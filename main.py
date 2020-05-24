import os
os.system('pip install external_dependencies/PyAudio-0.2.11-cp36-cp36m-win_amd64.whl')
os.system('pip install SpeechRecognition==3.8.1')
import speech_recognition as sr
os.system('pip install pyttsx3==2.71')
import pyttsx3
import commands
os.system('pip install boto3==1.13.16')

speech = sr.Recognizer()
try:
    engine = pyttsx3.init()
except ImportError:
    print('Driver not found :(')
except RuntimeError:
    print('Driver failed to initialize :(')

voices = engine.getProperty('voices')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

rate = engine.getProperty('rate')
engine.setProperty('rate', rate)

def speak_text_cmd(cmd):
    print(cmd)
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
    voice_text = ''
    print('Listening...')
    with sr.Microphone() as source:
        audio = speech.listen(source=source, timeout=0, phrase_time_limit=5)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        speak_text_cmd('Unknown command')
    except sr.RequestError as e:
        speak_text_cmd('Network error, please check your internet settings and try again')
    return voice_text

if __name__ == '__main__':
    commands.welcome_message()
    commands.all_commands()