import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate=160
engine.setProperty('rate', newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is") 
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date= int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
 
def wishme():
    speak("welcome back sir")
    hour=datetime.datetime.now().hour
    if hour >= 6 and hour <=12:
        speak ("good morning ")
    elif hour >= 12 and hour <=17:
        speak ("good afternoon ")
    elif hour >= 17 and hour <=24:
        speak ("good evening ")
    else:
        speak ("good night ")
    speak(" bubb,at your service")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language='eng-in')
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please")
    
        return "None"

    return query

if __name__== "__main__":
    
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query , sentences =1)
            speak(result)