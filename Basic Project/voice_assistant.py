import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    period = datetime.datetime.now().hour
    if period >= 6 and period < 12:
        speak("Good Morning Sir")
    elif period >= 12 and period < 18:
        speak("Good Afternoon Sir")
    elif period >= 18 and period < 22:
        speak("Good Evening")
    else:
        speak("Good night")
    speak("Martin at your service, How can I help you ?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        querry = r.recognize_google(audio,language='en-in')
        print(querry)
    except Exception as e:
        print(e)
        speak("Cannot recognise what you said, pleases say that again")
        return None
    return querry

def send_email(to,msg):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls
    server.login("sumedhthecool@gmail.com",password='')
    server.sendmail("sumedhthecool@gmail.com",to,msg)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        querry = take_command().lower()
        if "time and date" in querry:
            time()
            date()
        elif "time"in querry:
            time()
        elif "date" in querry:
            date()
        elif "go to hell" in querry:
            speak("show some respect sir")
        elif "wikipedia" in querry:
            speak("Searching...")
            querry = querry.replace("wikipedia","")
            querry = querry.replace("search","")
            result = wikipedia.summary(querry,sentences = 2)
            print(result)
            speak(result)
        elif "email" in querry:
            try:
                speak("What is your message ?")
                msg = take_command()
                to = "sumedhkadam@outlook.com"
                send_email(to,msg)
                speak("Your email has been succesfully sent.")
            except Exception as e:
                print(e)
                speak("Email not sent.")
        elif "google" in querry:
            speak("What do you want to search ?")
            edgepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            search = take_command().lower()
            wb.get(edgepath).open_new_tab(search)
            
        elif "offline" in querry:
            print("Shutting Down...")
            speak("Shutting Down")
            quit()
