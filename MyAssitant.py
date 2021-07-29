import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia as wiki
import tkinter as tk





engine =pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def myWindow():
    m=tk.Tk(screenName='Desktop Assitant')
    button = tk.Button(m, text='SPEAK', width=25, command=takeCommand) 
    button.pack()
    m.title("Desktop Assitant")
    m.mainloop()

def wishme(name):
# datetime object containing current date and time
    now = int(datetime.datetime.now().hour)
    if(now>=12 and now<16):
        speak("Good Afternoon!"+name)
        speak("Have a good day")
    elif(now>=16 and now<20):
       speak("Good Evening!"+name)
       speak("I hope you are having a good day")
    elif((now>=20 and now<=23) or (now>=0 and now<4 ) ):
       speak("Good Night!"+name)
       speak("I hope you had a great day")
    else:
       speak("Good Moring!"+name)
       speak("I hope you have a good day")
    speak("I am your assistant. Tell me How can I help you?")

def takeCommand():
    #take microphone input and returns text output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising......")
        query= r.recognize_google(audio,language='en-in')
        print("User said:"+ query)
    except Exception as e:    #if any error occur 
        speak("Sorry!!!I didn't hear that. Can you say it again?")
        return "None"
    return query

if __name__ == "__main__":
    wishme("Bro")
    #myWindow()
    while True:
        query=takeCommand().lower()
        if(("wikipedia" in query)) :
            if("wikipedia"in query):
                query.replace("wikipedia","")
                res=wiki.summary(query,sentences=2)
            elif("tell me about" in query):
                query.replace("tell me about","")
                res=wiki.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(res)
            speak(res)
        if("open youtube" in query):
            webbrowser.open("youtube.com")
        if("open google" in query):
            webbrowser.open("google.com")
        if("bye" in query):
            speak("Okay!! bye Have a good day")
            break
        



