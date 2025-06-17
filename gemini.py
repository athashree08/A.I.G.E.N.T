import google.generativeai as genai
import speech_recognition as sr 
import webbrowser
import requests
import warnings
import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def chat():
    genai.configure(api_key="AIzaSyA4TIHZ_ezXBTJ8s9VFzWpHH4S8zv5JGlE")

    r = sr.Recognizer() 

# Set up the model
    generation_config = {"temperature": 0.9,"top_p": 1,"top_k": 1,"max_output_tokens": 1000,}

    safety_settings = [{
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },]


    model = genai.GenerativeModel(model_name="gemini-1.0-pro" ,generation_config=generation_config,safety_settings=safety_settings)
#******************************************************************************************

#********************************************************************
    convo = model.start_chat(history=[])

    def SpeakText(command):
    # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command) 
        engine.runAndWait()
# Loop infinitely for user to
# speak
    while(1):    
    # Exception handling to handle
    # exceptions at the runtime
        try:
        # use the microphone as source for input.
            with sr.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
                r.adjust_for_ambient_noise(source2, duration=0.2)
            #listens for the user's input 
                print("Speak Your Queary Now:")
                audio2 = r.listen(source2)
            # Using google to recognize audio
                Q = r.recognize_google(audio2)
                Q = Q.lower()
                print("You Say:",Q)
                if "stop" in Q:
                    speak("Ok Sir!")
                    break
                else:
                    convo.send_message(Q)
                    speak(convo.last.text)
                    print((convo.last.text))
        except sr.RequestError as e:
            speak("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            speak("Sorry Sir i can't catch it can you say it again")
chat()