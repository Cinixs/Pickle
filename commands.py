import os
import random
import main
os.system('pip install playsound==1.2.2')
from playsound import playsound

def random_response(responses):
    pick_random = random.choice(responses)
    main.speak_text_cmd(pick_random)

def welcome_message():
    responses = [
        'Hello Sir, I am Pickle',
        'Hello Friend, I am Pickle',
        'Hello Sir, I am Pickle, your digital assistant',
        'Hello Sir, how may I help you?',
        'Hello Friend, I am your digital assistant',
        'Hey Sir, Nice to meet you'
    ]

    playsound('tone.mp3')
    random_response(responses)

def hello():
    responses = [
        'Hello Sir, what can I do for you?',
        'Hello Friend, what can I do for you?',
        'Hey Sir, ask a question'
    ]

    random_response(responses)

def bye():
    responses = [
        'Bye Sir',
        'See you soon'
    ]

    random_response()

def open(voice_note):
    if voice_note.strip('open') == ' ':
        main.speak_text_cmd('Error, please specify what I should open')
    else:
        os.system('start' + voice_note.strip('open'))

def shutdown(voice_note):
    if voice_note.strip('shutdown') == ' ':
        main.speak_text_cmd('Error, please specify -r or -s')
    elif voice_note != 'shutdown -r' or 'shutdown -s':
        main.speak_text_cmd('Error, please specify -r or -s')
    elif voice_note == 'shutdown -r':
        main.speak_text_cmd('Restarting in 30s')
        os.system('shutdown -r -t 30')
    elif voice_note == 'shutdown -s':
        main.speak_text_cmd('Shutting down in 30s')
        os.system('shutdown -s -t 30')

def all_commands():

    voice_note = main.read_voice_cmd()

    print(voice_note)

    while True:

        if ('hello' or 'hi') in voice_note:
            hello()
            continue

        if ('goodbye' or 'bye') in voice_note:
            bye()
            continue

        if 'open' in voice_note:
            open(voice_note)
            continue

        if 'shutdown' in voice_note:
            shutdown(voice_note)