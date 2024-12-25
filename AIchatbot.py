<<<<<<< HEAD:AI Chatbot/AIchatbot.py
import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import openai
import os
import webbrowser
from pygame import mixer
import random
import pywhatkit
# import imutils
import cv2

openai.api_key=os.environ.get("OPENAI_API_KEY")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    '''
    This function  is used to speak the argument audio in system voice.
    '''
    print("AI Bot is speaking...")
    engine.say(audio)
    engine.runAndWait()

def wishme():
    '''
    This function is used to wish according to time.
    '''
    hour=int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")
    elif hour>12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")

def lisening_user():
    '''
    This function is used to listen the user's speech.
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=0.5
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User: {query}")
    except Exception as e:
        # print(e)
        print("say that again please!")
        return "None"
    return query


def wiki(query):
    '''
    Function for searching on wikipedia
    '''
    query=query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=2)
    return results

def gpt_searching(ask):
    '''
    This function is used to search the query using openai.
    '''
    ask=ask.replace("gpt","")
    response=openai.Completion.create(
        engine="text-davinci-003",
        prompt=ask
    )
    answer=response.choices[0].text
    return answer

def browser_search(search):
    '''
    This function is used to open browser according to user need.
    '''
    search= search.replace("open","")     # we will get search as " youtube in browser"
    search=search.replace ("in browser","")       # we will get search as " youtube "
    search=search[1:len(search)-1]      # we will get query as "youtube"
    opening=f"www.{search}.com"        # youtube will open in browser as "www.youtube.com"
    return opening

class play_music:
    '''
    This class is used to play the music for user from the music directory.
    '''
    # playing music using os module but it shows an error in system
    # music_dir="C:\\Users\\vp587\\Music"
    # songs=os.listdir(music_dir)
    # print(songs[0])
    # return os.startfile(os.path.join(music_dir,songs[0]))

    # playing music using mixer module
    def current_song():
        music_dir="C:\\Users\\vp587\\Music"
        os.chdir(music_dir)
        music=random.choice(os.listdir())
        mixer.init()
        speak(f"plying {music}")
        mixer.music.load(music)
        mixer.music.play()
    def next_song():
        music=random.choice(os.listdir())
        mixer.music.load(music)
        return mixer.music.play()
    def pause_song():
        return mixer.music.pause()
    def stop_song():
        return mixer.music.stop()


if __name__=='__main__':
    # os.startfile("jarvis.mp4")
    # img=cv2.imread("jarvis.png")
    # img_rez=imutils.resize(img,width=2000)
    # cv2.imshow("Jarvis",img_rez)
    speak("Welcome back sir, How can I assist you?")
    while True:
        query=lisening_user().lower()
        # speak(query)

        # logic for executing task based on query
        if query=="wish me":
            wishme()
        elif "wikipedia" in query:
            speak("Sure sir wait a while.")
            try:
                results=wiki(query)
                print(results)
                speak("according to wikipedia")
                speak(results)
            except Exception:
                speak("can't find it on wikipedia!")
            
        elif "jarvis" in query:
            speak("Sure sir wait a while.")
            results=gpt_searching(query)
            print(results)
            speak(results)
        elif "exit" in query:
            speak("Goodbye sir.")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            exit()
        elif "in browser" in query:
            url=browser_search(query)
            webbrowser.open(url)
        elif "play song" in query:
           speak("Playing the song")
           play_music.current_song()
        elif "play next song" in query:
            play_music.next_song()
        elif "pause song" in query:
            play_music.pause_song()
        elif "stop song" in query:
            play_music.stop_song()
            os.chdir("C:\\Users\\vp587\\Desktop\\Python\\Projects")
        elif "time" in query:
            strTime=datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
        elif "open vs code" in  query:
            app_path="C:\\Users\\vp587\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(app_path)
        elif "browser" in query:
            app_path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk"
            os.startfile(app_path)
        elif "open command prompt" in query:
            app_path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Git\\Git Bash.lnk"
            os.startfile(app_path)
        elif "open file manager" in query:
            app_path="C:\\Users\\vp587\\Desktop"
            os.startfile(app_path)
        elif "whatsapp" in query:
            pywhatkit.sendwhatmsg("+916362374373","Hello there, This side vp587",int(datetime.now().hour),int(datetime.now().minute),True,2)
        else:
            results=gpt_searching(query)
            print(results)
=======
import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import openai
import os
import webbrowser
from pygame import mixer
import random
import pywhatkit
# import imutils
import cv2

# openai.api_key=os.environ.get("OPENAI_API_KEY")
openai.api_key = "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"

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    '''
    This function  is used to speak the argument audio in system voice.
    '''
    print("AI Bot is speaking...")
    engine.say(audio)
    engine.runAndWait()

def wishme():
    '''
    This function is used to wish according to time.
    '''
    hour=int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")
    elif hour>12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")

def lisening_user():
    '''
    This function is used to listen the user's speech.
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=0.5
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User: {query}")
    except Exception as e:
        # print(e)
        print("say that again please!")
        return "None"
    return query


def wiki(query):
    '''
    Function for searching on wikipedia
    '''
    query=query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=2)
    return results

def gpt_searching(ask):
    '''
    This function is used to search the query using openai.
    '''
    ask=ask.replace("gpt","")
    response=openai.Completion.create(
        engine="text-davinci-003",
        prompt=ask
    )
    answer=response.choices[0].text
    return answer

def browser_search(search):
    '''
    This function is used to open browser according to user need.
    '''
    search= search.replace("open","")     # we will get search as " youtube in browser"
    search=search.replace ("in browser","")       # we will get search as " youtube "
    search=search[1:len(search)-1]      # we will get query as "youtube"
    opening=f"www.{search}.com"        # youtube will open in browser as "www.youtube.com"
    return opening

class play_music:
    '''
    This class is used to play the music for user from the music directory.
    '''
    # playing music using os module but it shows an error in system
    # music_dir="C:\\Users\\vp587\\Music"
    # songs=os.listdir(music_dir)
    # print(songs[0])
    # return os.startfile(os.path.join(music_dir,songs[0]))

    # playing music using mixer module
    def current_song():
        music_dir="C:\\Users\\vp587\\Music"
        os.chdir(music_dir)
        music=random.choice(os.listdir())
        mixer.init()
        speak(f"plying {music}")
        mixer.music.load(music)
        mixer.music.play()
    def next_song():
        music=random.choice(os.listdir())
        mixer.music.load(music)
        return mixer.music.play()
    def pause_song():
        return mixer.music.pause()
    def stop_song():
        return mixer.music.stop()


if __name__=='__main__':
    # os.startfile("jarvis.mp4")
    # img=cv2.imread("jarvis.png")
    # img_rez=imutils.resize(img,width=2000)
    # cv2.imshow("Jarvis",img_rez)
    speak("Welcome back sir, How can I assist you?")
    while True:
        query=lisening_user().lower()
        # speak(query)

        # logic for executing task based on query
        if query=="wish me":
            wishme()
        elif "wikipedia" in query:
            speak("Sure sir wait a while.")
            try:
                results=wiki(query)
                print(results)
                speak("according to wikipedia")
                speak(results)
            except Exception:
                speak("can't find it on wikipedia!")
            
        elif "jarvis" in query:
            speak("Sure sir wait a while.")
            results=gpt_searching(query)
            print(results)
            speak(results)
        elif "exit" in query:
            speak("Goodbye sir.")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            exit()
        elif "in browser" in query:
            url=browser_search(query)
            webbrowser.open(url)
        elif "play song" in query:
           speak("Playing the song")
           play_music.current_song()
        elif "play next song" in query:
            play_music.next_song()
        elif "pause song" in query:
            play_music.pause_song()
        elif "stop song" in query:
            play_music.stop_song()
            os.chdir("C:\\Users\\vp587\\Desktop\\Python\\Projects")
        elif "time" in query:
            strTime=datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
        elif "open vs code" in  query:
            app_path="C:\\Users\\vp587\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(app_path)
        elif "browser" in query:
            app_path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk"
            os.startfile(app_path)
        elif "open command prompt" in query:
            app_path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Git\\Git Bash.lnk"
            os.startfile(app_path)
        elif "open file manager" in query:
            app_path="C:\\Users\\vp587\\Desktop"
            os.startfile(app_path)
        elif "whatsapp" in query:
            pywhatkit.sendwhatmsg("+916362374373","Hello there, This side vp587",int(datetime.now().hour),int(datetime.now().minute),True,2)
        else:
            results=gpt_searching(query)
            print(results)
>>>>>>> 30f677d512a1cc73fcc317dcbb1053c48315a537:AIchatbot.py
            speak(results)