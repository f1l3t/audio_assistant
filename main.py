import os
import random
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
from gtts import gTTS


def listen():
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-то:")
        audio = voice_recognizer.listen(source)

    try:
        voice_text = voice_recognizer.recognize_google(audio, language="ru")
        print(f"Вы сказали: {voice_text}")

        return voice_text

    except sr.UnknownValueError:
        return "ошибка разпознания"
    except sr.RequestError:
        return "ошибка запроса"


def handle_command(command):
    command = command.lower()

    if command == "привет":
        say("Привет-привет")
    elif command == "пока":
        stop()
    elif command == "как дела":
        say("Все отлично")
    else:
        say("Не понятно, повторите")


def say(text):
    voice = gTTS(text, lang="ru")
    file_name = f'audio_{random.randint(1, 100000000000)}.mp3'
    print(file_name)
    voice.save(file_name)

    playsound.playsound(file_name)

    # os.remove(file_name)

    print(f"Ассистент: {text}")


def stop():
    say("До скорого")
    exit()


def start():
    print("Запуск ассистента...")

    while True:
        file_name = f"audio_{30120369810}.mp3"
        playsound.playsound(file_name)
        # command = listen()
        # handle_command(command)


start()
