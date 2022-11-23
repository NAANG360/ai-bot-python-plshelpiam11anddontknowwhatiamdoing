import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time
import threading
import tkinter as tk
from win10toast import ToastNotifier
import playsound
import plyer

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hi How Can I Assist You')
print("How Can I Assist You")
engine.runAndWait()
try:
    with sr.Microphone() as source:
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'test' in command:
            engine.say('OK Running', command)
            engine.runAndWait()
        if 'hello' in command:
            engine.say('Hello User')
            engine.runAndWait()
            print('Hello User')
        if 'hi' in command:
            engine.say('Hello User')
            engine.runAndWait()
            print('Hello User')
        if 'hey' in command:
            engine.say('Hello User')
            engine.runAndWait()
            print('Hello User')
except:  
    pass

command = listener.recognize_google(voice)
command =  command.lower()
if 'play' in command:
    engine.say('Ok Let Me Search On The INTERNET For It', song)
    engine.runAndWait()
    song = command.replace('play', '')
    pywhatkit.playonyt(song)
if 'time' in command:
    time = datetime.datetime.now().strftime('%I:%M:%S')
    engine.say('The Current Time Is'+ time)
    engine.runAndWait()
    print('The Current Time Is', time)
if 'who is' in command:
    person = command.replace('who is', '')
    info = wikipedia.summary(person, 1)
    print(info)
    engine.say(info)
    engine.runAndWait()
if 'who was' in command:
    person = command.replace('who is', '')
    info = wikipedia.summary(person, 1)
    print(info)
    engine.say(info)
    engine.runAndWait()
if 'what is' in command:
    person = command.replace('what is', '')
    info = wikipedia.summary(person, 1)
    print(info)
    engine.say(info)
    engine.runAndWait()
if 'what was' in command:
    person = command.replace('what was', '')
    info = wikipedia.summary(person, 1)
    print(info)
    engine.say(info)
    engine.runAndWait()
if 'joke' in command:
    engine.say(pyjokes.get_joke())
    engine.runAndWait()
if 'set a reminder for' in command:
    reminder = command.replace('set a reminder for', '')
    print('sorry caant make a timer for', command, 'yet the ai is still in alpha')
    engine.say('sorry caant make a timer yet the ai is still in alpha')
    engine.runAndWait()