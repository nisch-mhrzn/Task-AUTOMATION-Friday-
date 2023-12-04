import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import time
import winsound

engine = pyttsx3.init('sapi5') #sapi = Speech API by Microsoft
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id) #voice[1].id = Female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Sir,The current time is")
    speak(Time)
    print("Sir, The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    print("Welcome back sir!!")
    speak("Welcome back sir!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tommorrow")

    speak("Friday at your service sir, please tell me how may I help you.")
    print("Friday at your service sir, please tell me how may I help you.")

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\Users\hp\Pictures\Screenshots\sc.png")

def set_reminder():
    # Ask user for reminder message and duration
    message = input("What would you like to be reminded of? ")
    duration = int(input("How many seconds from now should the reminder go off? "))

    # Calculate reminder time
    now = datetime.datetime.now()
    reminder_time = now + datetime.timedelta(seconds=duration)

    # Wait until reminder time
    while datetime.datetime.now() < reminder_time:
        time.sleep(1)

    # Alert user with message and sound
    print(message)
    duration = 1000  # milliseconds
    frequency = 440  # Hz
    winsound.Beep(frequency, duration)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
        print(query)

    except Exception as e:
        print(e)
        speak("Sir, Can you say that again?")
        return "Try Again"

    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I am Friday. Please tell me how may I help you?")
            print("I am Friday. Please tell me how may I help you?.")

        elif "how are you" in query:
            speak("I'm fine sir. What about you?")
            print("I'm fine sir. What about you?")

        elif "fine" in query or "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")


        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")
        
        elif "open youtube" in query:
            wb.open("youtube.com") 

        elif "open google" in query:
            wb.open("google.com") 
   
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "C:\Users\hp\Desktop\Javascript\Spotify\songs"
            songs = os.listdir(music_dir)
            print(songs)
            x = len(songs)
            y = random.randint(0,x)
            os.startfile(os.path.join(music_dir, songs[y]))

        elif "open chrome" in query:
            chromePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                speak("Sure what do you want to search?")
                print("Sure what do you want to search?")
                chromePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")
            
        
        elif "remember that" in query:
            speak("What should I remember?")
            data = takecommand()
            speak("You told me to remember " + data)
            print("You told me to remember  " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember " + remember.read())
            print("You told me to remember " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")

        elif "Set reminder " in query:
            set_reminder()

           
        elif "offline" in query:
            quit()
