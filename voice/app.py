# ос  windows 10
# ставим пакеты
# pip install pipwin pyttsx3 pypiwin32
# pip install pyaudio
# pip install speech_recognition
import pyttsx3
import speech_recognition as sr
import os
import sys
import webbrowser

#def talk(words):
#    print(words)
#    os.system("say " + words)
#talk("Привет спроси у меня что-либо!")

def talk(words):
    print(words)
    os.system("say " + words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


talk("Привет спроси у меня что-либо!")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1 # ждем одну секунду
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + zadanie)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        zadanie = command()
    return zadanie


def makeSomething(zadanie):
    if 'открой сайт' in zadanie:
        talk("Уже открываю")
        url = 'https://b14esh.com'
        webbrowser.open(url)
    elif 'стоп' in zadanie:
        talk("Да конечно без проблем")
        sys.exit()

while True:
    makeSomething(command())




