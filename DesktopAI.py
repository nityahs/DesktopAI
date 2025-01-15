import pyttsx3
import speech_recognition as sr
import webbrowser
import openai
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

if __name__ == '__main__':
    say("Hello, I am Jarvis A I")
    while True:
        query = takeCommand()  # Call the function to listen and process the user's command
        print(f"query: {query}")
        #say(query)
        if "Open YouTube".lower() in query.lower():
          say(f"Opening YouTube  ")
          webbrowser.open("https://youtube.com")




