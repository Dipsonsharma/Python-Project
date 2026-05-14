import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib
import weblibrary

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processcommand(com):
    c = com.lower()
    print(f"Did you say : {c}?")

    if c.startswith("open"):
        w = c.split(" ")[1]
        webbrowser.open(weblibrary.web.get(w))
       
    elif c.startswith("play"):
        song = c.split(" ")[1] #play ra song_name lai split garerw song_name lai song ma store garxa
        webbrowser.open(musiclib.music.get(song))
   
if __name__ == "__main__":
    speak("Initializing jarvis...") 

    while True:
        r = sr.Recognizer()
        try:
            #obtain audio from microphone
            with sr.Microphone() as source:
                print("Listining...")
                audio = r.listen(source,timeout=4, phrase_time_limit=2)

            com = r.recognize_google(audio)
            command = com.lower()
            print("Recognizing...")
            a = "jarvis"

            if a in command:
                speak("Yes, how may i help you?")
                with sr.Microphone() as newsource:
                    print("Jarvis is listning...")
                    newaudio = r.listen(newsource, timeout=2)
                rec = r.recognize_google(newaudio)
                processcommand(rec)
       
        except Exception as e:
            print(f"Error occured; {e}")