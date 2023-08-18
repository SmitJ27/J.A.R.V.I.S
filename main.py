import cv2
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyautogui
#import pywhatkit
import pywhatkit as kit
import pyjokes
import sys
import PyPDF2
from requests import get
import requests
import speedtest
import operator
import instaloader
import time
import json
import datetime
import pywhatkit
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from PyQt5.uic import loadUiType
from JarvisUi import Ui_MainWindow
import os
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")



def pdf_reader():
    book = open('D:\\python_tutorial.pdf')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book{pages} ")
    speak("Sir please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


class Mainthread(QThread):
    def __init__(self):
        super(Mainthread,self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=6, phrase_time_limit=4)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        query = query.lower()
        return query


    def TaskExecution(self, kit=None):
        if __name__ == "__main__":
            wish()
            while True:
            # if 1:
                self.query = self.takeCommand()

                # Logic for executing tasks based on query
                if 'wikipedia' in self.query:
                    speak('Searching Wikipedia...')
                    self.query = self.query.replace("wikipedia", "")
                    results = wikipedia.summary(self.query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif "open Notepad" in self.query:
                    npath = "C:\\windows\\system32\\notepad.exe"
                    os.startfile(npath)
                    speak("opening notepad")

                elif 'play' in self.query:
                    song = self.query.reverse('play', '')
                    speak('OK Playing some songs' + song)
                    pywhatkit.playonyt(song)


                elif "close notepad" in self.query:
                    speak("okay boss closing notepad")
                    os.system(" taskkill /F /im notepad.exe ")
                    speak("Command executed Successfully")

                elif "write a note" in self.query:
                    speak("What should i write, sir")
                    note = self.takeCommand()
                    file = open('jarvis.txt', 'w')
                    speak("Sir, Should i include date and time")
                    snfm = self.takeCommand()
                    if 'yes' in snfm or 'sure' in snfm:
                        strTime = datetime.datetime.now().strftime("%H: %M: %S")
                        file.write(strTime)
                        file.write(" :- ")
                        file.write(note)
                    else:
                        file.write(note)

                elif 'open youtube' in self.query:
                    webbrowser.open("youtube.com")
                    speak("Command executed Successfully,do u have any other task?")

                elif 'read pdf' in self.query:
                    pdf_reader()

                elif 'news' in self.query:

                    try:
                        jsonObj = urlopen(
                            '''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=\\times of India Api key\\''')
                        data = json.load(jsonObj)
                        i = 1

                        speak('here are some top news from the times of india')
                        print('''=============== TIMES OF INDIA ============''' + '\n')

                        for item in data['articles']:
                            print(str(i) + '. ' + item['title'] + '\n')
                            print(item['description'] + '\n')
                            speak(str(i) + '. ' + item['title'] + '\n')
                            i += 1
                    except Exception as e:

                        print(str(e))

                elif "open camera" in self.query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow("webcam", img)
                        k = cv2.waitKey(100)
                        if k == 50:
                            break
                    cap.release()
                    cv2.destroyAllWindows()

                elif "ip address" in self.query:
                    ip = get('https://api.ipify.org').text
                    speak(f"your ip address is {ip}")
                    speak("Command executed Successfully,do u have any other task?")

                elif "where is" in self.query:
                    query = self.query.replace("where is", "")
                    location = query
                    speak("User asked to Locate")
                    speak(location)
                    webbrowser.open("https://www.google.nl/maps/place/" + location + "")

                elif "microsoft teams" in self.query:
                    mpath = "C:\\Users\\hp\\AppData\\Local\\Microsoft\\Teams\\previous\\Teams.exe"
                    os.startfile(mpath)

                elif "tell me a joke" in self.query:
                    joke = pyjokes.get_joke()
                    speak(joke)
                    speak("Command executed Successfully,do u have any other task?")


                elif "open teamviewer" in self.query:
                    tvpath = "C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe"
                    os.startfile(tvpath)
                    speak("Command executed Successfully,do u have any other task?")


                elif 'open stackoverflow' in self.query:
                    webbrowser.open("stackoverflow.com")
                    speak("time to copy-paste.. hehe")
                    speak("Command executed Successfully,do u have any other task?")

                elif "open command prompt" in self.query:
                    os.system("start cmd")
                    speak("opening command prompt")
                    speak("Command executed Successfully,do u have any other task?")

                elif 'open youtube' in self.query:
                    webbrowser.open("youtube.com")

                elif 'open google' in self.query:
                    speak("sir what shall i search on google")
                    cm = self.takeCommand().lower()
                    webbrowser.open(f"{cm}")

                elif 'open stackoverflow' in self.query:
                    webbrowser.open("stackoverflow.com")

                elif 'play' in self.query:
                    song = self.query.replace('play', '')
                    speak('playing ' + song)
                    pywhatkit.playonyt(song)

                elif 'the time' in self.query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif 'open code' in self.query:
                    codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                elif "play songs on youtube" in query:
                    kit.playonyt("on my way")

                elif 'play music' in self.query:
                    music_dir = 'C:\\Users\\Smit Joshi\\Music\\Songs'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))
                    speak("Playing music hope u like it...")
                    #speak("Command executed Successfully,do u have any other task?")

                elif 'the time' in self.query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Boss, the time is {strTime}")
                    speak("Command executed Successfully,do u have any other task?")

                elif 'open code' in self.query:
                    codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code"
                    os.startfile(codePath)
                    speak("Command executed Successfully,do u have any other task?")

                elif "restart the system" in self.query:
                    os.system("shutdown /r /t 5")

                elif "shutdown the system" in self.query:
                    os.system("shutdown /s /t 5")

                elif "set alarm" in self.query:
                    speak("Sir please tell me the time to set alarm. For example set alarm at 5:30 am")
                    tt = self.takeCommand()
                    tt = tt.replace("set alarm at ", "")
                    tt = tt.replace(".", "")
                    tt = tt.upper()
                    import MyAlarm

                    MyAlarm.alarm(tt)

                elif "internet speed" in self.query:
                    st = speedtest.speedtest()
                    dl = st.download()
                    up = st.upload()
                    speak(f"Sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed ")
                    speak("Task executed Successfully,do u have any other task?")

                elif "weather" in self.query:
                    search = "weather in pune"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current, {search} is {temp}")
                    speak("command executed Successfully do u have any other task")

                elif "calculate" in self.query:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        speak("say what you want to calculate, example 3 plus 3")
                        print("Listening....")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    my_string = r.recognize_google(audio)
                    print(my_string)


                    def get_operator_fn(op):
                        return {
                            '+': operator.add,
                            '-': operator.sub,
                            'x': operator.mul,
                            'divided': operator.__truediv__,
                        }[op]


                    def eval_binary_expr(op1, oper, op2):
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)


                    speak("Your result is")
                    speak(eval_binary_expr(*(my_string.split())))
                    speak("Task executed Successfully,do u have any other task?")

                elif "activate how to do mod" in self.query:
                    speak("How to do mode is activated tell me what uou want to know")
                    how = self.takeCommand()
                    max_results = 1
                    how_to = search_wikihow (how, max_results)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)
                    pass

                elif "where i am" in self.query or "where we are" in self.query:
                    speak("wait sir ,let me check")
                    try:
                        ipAdd = requests.get('https://api.ipify.org').text
                        print(ipAdd)
                        url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                        geo_requests = requests.get(url)
                        geo_data = geo_requests.json()
                        city = geo_data['city']
                        state = geo_data['state']
                        country = geo_data['country']
                        speak(f"Sir i am not sure, but i think we are in{city} city of {state} state in {country} country")
                    except Exception as e:
                        speak("Sorry sir, Due to network issue i am not able to find where we are.")
                        pass

                elif "Instagram profile" in self.query or "profile on instagram" in self.query:
                    speak("Sir please enter the user name correctly.")
                    name = input("Enter username here:")
                    webbrowser.open(f"www.instagram.com/{name}")
                    speak(f"Sir here is the profile of the user {name}")
                    time.sleep(5)
                    speak("sir would you like to download profile picture of this account.")
                    condition = self.takeCommand().lower()
                    if "yes" in condition:
                        mod = instaloader.Instaloader()
                        mod.download_profile(name, profile_pic_only=True)
                        speak("I am done sir, Profile picture is saved on our main folder , Iam ready for next command")
                    elif "not" in condition:
                        speak("ok sir")
                    else:
                        pass

                elif "take screenshot" in self.query:
                    speak("sir, please tell me the name for this screenshot file")
                    name = self.takeCommand().lower()
                    speak("please sir hold the screen for few seconds, i am taking screenshot")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("I am done sir, screenshot is saved on our main folder , Iam ready for next command")

                elif "hello" in self.query:
                    speak("Hello sir, may i help you with something?")

                elif "how are you" in self.query:
                    speak("i am fine sir, what about you")

                elif "good" in self.query:
                    speak("it's my pleasure sir")

                elif "you can sleep" in self.query or "sleep now" in self.query:
                    speak("Okay sir, I am going to sleep you can call me anytime.")
                    break

startExecution = Mainthread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("E:/Python Programs/Final jarvis/Jarvis/background.jpg")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/Python Programs/Final jarvis/Jarvis/ironman.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/Python Programs/Final jarvis/Jarvis/equalizer.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/Python Programs/Final jarvis/Jarvis/heart.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/Python Programs/Final jarvis/Jarvis/iron man.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/Python Programs/Final jarvis/Jarvis/pagal.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
     

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())
