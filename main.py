from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
from PlaySongs import play_songs


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.record(source, duration=4)
        said = ""

        try:
            said = r.recognize_google(audio)

        except Exception as e:
            print("Exception: " + str(e))

    return said

while True:
    print("listening...")
    text = get_audio()

    if (text.count("electron") == 1):
        speak("I am ready")
        message = get_audio()
        message.lower()
        
        if(message[0:4] == 'play'):
            song = message[5:]
            speak("playing {song}".format(song=song))

            try:
                play_songs(song)

            except Exception as e:
                print(e)
                speak("cannot play requested song")

        else:
            speak("i didn't understand you")

