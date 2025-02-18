import pyttsx3
import speech_recognition as sr
import webbrowser
import google.generativeai as genai
from config import api_keypriv
import os
import datetime
import keyboard
genai.configure(api_key=api_keypriv)
#use webdriver to log into your account
def say(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)  # Listen for input
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-IN')  # Recognize using Google Web Speech API
            #query = r.recognize_google(audio,language='gu-IN')  # Recognize using Google Web Speech API
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return "Some error occured"
        except sr.RequestError:
            print("Could not request results, check your internet connection.")
            return "Some error occured"
def useAI(inp):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        system_instruction="You are a Desktop Assistant. Your name is Jarvis."
        chat = model.start_chat(
            history=[
                {"role": "user", "parts": "Hello"},
                {"role": "model", "parts": "Great to meet you. What would you like to know?"},
            ]
        )


        a=chat.send_message(inp)
        print(a.text)

        return a.text
    except UnknownValueError:
        print("Invalid Value")
if __name__ == '__main__':
    say("Hello, I am Jarvis A I")
    while True:
        query = takeCommand()  # Call the function to listen and process the user's command
        print(f"query: {query}")
        #say(query)
        sites=[['Youtube',"https://youtube.com"],["wikipedia","https://wikipedia.com"],["google","https://google.com"]]
        apps=[['Teams',r"C:\Users\Nitya Shah\AppData\Local\Microsoft\WindowsApps\MSTeams_8wekyb3d8bbwe\ms-teams.exe"],['PyCharm',r"C:\Program Files\JetBrains\PyCharm 2023.2.3\bin\pycharm64.exe"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}  ")
                webbrowser.open(site[1])

        if "Play music".lower() in query.lower():
            say("Playing Music: ")
            musicpath=r"C:\Users\Nitya Shah\Downloads\testsong.mps.mp3"
            os.startfile(musicpath)
        if "time".lower() in query.lower():
            tim=datetime.datetime.now().strftime("%H:%M")
            say(f"Time is: {tim}")
            print(f"Time is: {tim}")
        for app in apps:
            if f"open {app[0]}".lower() in query.lower():
                say(f"Opening {app[0]}")
                os.startfile(app[1])
        if keyboard.is_pressed("esc"):
            say("Goodbye!")
            print("Exiting program...")
            break
        if "Use AI".lower() in query.lower():
            ans=useAI(query)
            say(ans)
