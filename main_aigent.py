import pyttsx3 #global variable
import speech_recognition
import pyautogui
import pywhatkit
import random as rm
from datetime import datetime
from io import StringIO

engine = pyttsx3.init("sapi5") #this is used to change the voice
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",200) #Setting the Rate

def speak(audio): # this Function is Used to speak
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source: 
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source,0,4)
    try:
        print("Understanding....")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said:{query}\n")
    except Exception as e:
        speak("sorry sir, i can't catch it can you say it again")
        print("sorry sir, i can't catch it can you say it again")
        return "None"
    return query

def aigent_ex():
    while True:
        query = takeCommand()
        if "wake up" in query:
            from GreetME import greetme
            greetme()
            while True:
                query = takeCommand()

                if 'jarvis' in query:
                    speak("i know you know my real name. don't be silly, MY real name is AIGENT")

                elif "hello" in query:
                    speak("Hello Sir, How are You?")

                elif "i am fine" in query or 'ok' in query:
                    speak("That's great Sir")

                elif "who are you" in query or "hu r u" in query:
                    speak('''Now me to introduce myself, im AIGENT. The Virtual Artificial Intelligence, and i'm here you to assist you 
                        the varity of task the best i can . 24 hours the day, 7 days of week. importing all preferences to hub interface, the system is now
                        Fully operational''')

                elif "how are you" in query:
                    speak("Perfect sir like you")

                elif "great" in query:
                    speak("my pleasure")

                elif "Detect face" in query:
                    from face_detection import detect_face
                    detect_face()

                elif "thank you" in query:
                    speak("Your Welcome sir")

                elif "Google" in query:
                    from search_now import searchGoogle
                    searchGoogle(query)
                    
                elif "youtube" in query or "YouTube" in query:
                    from search_now import searchyoutube
                    searchyoutube(query)

                elif 'time' in query:
                    current_time =datetime.now().strftime('%H:%M %p')
                    speak("current time is:"+ current_time)

                elif "play game with me" in query:
                    f1=0
                    speak("Yes Sir")
                    random_no= rm.uniform(1,50)
                    random_no = int(random_no)
                    speak("Let's Play guess the number game, the range of number is 1 to 50")
                    speak("let's start,for playing this game you have to type number, in terminal")
                    print(random_no)
                    while(f1==0):
                        query = int(input("Enter Number:"))
                        no=int(query)
                        if no==random_no:
                            speak("Yes you are right!, Great sir, your playing absolutly good")
                            f1=1
                        elif no<=random_no:
                            speak("Guess the small Number")
                        elif no>=random_no:
                            speak("Too Big")
                            speak("Enter Smaller Number")
                    
                elif 'play' in query:
                    song_name = query.replace('play','')
                    speak('Sure sir. Playing' +song_name+ 'in Youtube')
                    pywhatkit.playonyt(song_name)

                elif 'change window' in query:
                    pyautogui.hotkey('alt','tab')
                
                elif 'switch tab' in query:
                    pyautogui.hotkey('ctrl','tab')

                elif 'close tab' in query:
                    pyautogui.hotkey('ctrl','w')

                elif "open" in query:
                    app_name = query.replace('open','')
                    speak("opening" + app_name)
                    pyautogui.press('super')
                    pyautogui.typewrite(app_name)
                    pyautogui.sleep(0.7)
                    pyautogui.press('enter')

                elif "close" in query:
                    pyautogui.hotkey('alt','f4')
                    speak("Done Sir!")

                elif "go to chat mode" in query:
                    f1=0
                    speak("Initializing Chat mode")
                    speak("How can i help you sir")
                    while f1 == 0:
                        if "stop" in query:
                            f1=1
                            speak("Ok sir.")
                            break
                        else:
                            from gemini import chat
                            chat()
                elif "hand gestures" in query:
                    speak("Sure! Please Show Your Sign in window when it will Appear")
                    from handges import detect
                    detect()
                    break

                elif "detect face" in query:
                    speak("Sure! Please Wait until Window is appearing")
                    from face_detection import detect_face
                    detect_face()
                    
                elif "generate image" in query:
                    speak("Sure Sir!")
                    speak("I Will Provide a Prompt , just Simply typed the text on it.")
                    speak("After Creating a Image I'ii provide link,  just click on that And You Will See the Magic!")
                    from Gen_img import gen_image
                    gen_image() 
                elif "go to sleep" in query:
                    speak("Ok sir, i am going to sleep but you can call me at any time, just say wake up and i'll be there for you")
                    sleep_mode = True
                    while sleep_mode == True:
                        query = takeCommand().lower()
                        if 'wake up' in query:
                            speak("i am awake now.how can i help you sir")
                        sleep_mode = False
aigent_ex()