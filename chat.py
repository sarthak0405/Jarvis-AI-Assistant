import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
from requests import get
import pywhatkit as kit
import sys
import datetime
import pyautogui
import keyboard
import os
import openai
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from jarvis import Ui_mainGUI 
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QTextEdit
from apiconfig import apikey

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 190)

#Connectivity for the start and stop button
class MainThread(QThread):
    
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.Task_Gui()

    
    def Task_Gui(self):
        main()
        while True :
            query = takecommand().lower()

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainGUI()
        self.ui.setupUi(self)
        self.ui.startbutton.clicked.connect(self.startTask)
        self.ui.stopbutton.clicked.connect(self.close)

    def startTask(self):

        self.ui.movie= QtGui.QMovie("D:\\Project III Year\\GUI\\B.G\\vecteezy_technology-background-video-4k-hd-resolution_22653051_155.gif")
        self.ui.bg.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie= QtGui.QMovie("D:\\Project III Year\\GUI\\B.G\\Hero_Template.gif")
        self.ui.graph.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:\\Project III Year\\GUI\\B.G\\Earth.gif")
        self.ui.earth.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:\\Project III Year\\GUI\\B.G\\Siri")
        self.ui.reactor.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        startExecution.start()

    def terminalPrint(self, text):
        
        engine.say(text)
        print(text)
         # ui.terminalPrint(audio)
        print("    ")
    
        engine.runAndWait()
        self.ui.area.appendPlainText(text)

    def terminalPr(self, txt):
        self.ui.area.appendPlainText(txt)

#Chat Mode
chatStr = ""
def chat(query):
    if "none" in query :
        ui.terminalPrint("Say again")
    else :    
        global chatStr
        #print(chatStr)
        openai.api_key = apikey
        chatStr += f"User : {query}\nJarvis : "
        response = openai.Completion.create(
            model = "gpt-3.5-turbo-instruct",
            prompt = chatStr,
            temperature = 0.7,
            max_tokens = 256,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0
        )

        ui.terminalPrint(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]

#Code generation
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for  Prompt: {prompt}\n"
    
    response = openai.Completion.create(
        model = "gpt-3.5-turbo-instruct",
        prompt = prompt,
        temperature = 0.7,
        max_tokens = 800,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0

    )
    ui.terminalPrint("generating Code")
    print(response["choices"][0]["text"])
    text += (response["choices"][0]["text"])

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{prompt[0:50]}.txt", "w") as f :
        # speak("generating Code")
        f.write(text)
        ui.terminalPrint("Opening Code")    
        os.startfile(f'D:\\Project III Year\\Openai\\{prompt[0:50]}.txt')

#Take the command from the user
def takecommand():
    # It takes microphone input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        ui.terminalPr("Listening...")
        print("Listening..")

        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        ui.terminalPr("Recognizing...")
        print("Recognizing...")

        query = r.recognize_google(audio, language='en-in')
        ui.terminalPr(f"User said: {query}\n")
        print(f"User said: {query}\n")


    except Exception as e:
        # ui.terminalPrint("I was not able to recognize")

        return "none"
    return query.lower()

#Wish Good Morning, Afternoon or Evening
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        ui.terminalPrint("Good Morning Sir!")
        

    elif hour >= 12 and hour < 18:
        ui.terminalPrint("Good Afternoon Sir") 
    
    else:
        ui.terminalPrint("Good Evening!")

    ui.terminalPrint("I am Jarvis Sir....Please tell me how can I help you?")

#playing music according to the user
def music():
    # if 'you' in query:
    ui.terminalPrint('tell me the name of the song?')
    music_nav = takecommand()

    if 'animal' in music_nav:
        os.startfile('D:\\Project III Year\\Music\\animal.mp3')

    

    else:
        ui.terminalPrint("I didn't find the song in your music directory so I have played it on youtube")
        kit.playonyt(music_nav)
        ui.terminalPrint('Enjoy Sir')

#Youtube Automation
def YoutubeAuto():
    ui.terminalPrint("Whats your command sir?")
    comm = takecommand()

    if 'pause' in comm:
        keyboard.press('k')

    elif 'restart video' in comm:
        keyboard.press('0')

    elif 'mute' in comm:
        keyboard.press('m')

    elif 'skip' in comm:
        keyboard.press('1')

    elif 'back' in comm:
        keyboard.press('j')

    elif 'fullscreen' in comm:
        keyboard.press('f')

    elif 'film mode' in comm:
        keyboard.press('t')

    ui.terminalPrint('Done Sir!')

#Chrome Automation
def ChromeAuto():
    ui.terminalPrint('Chrome Autuomation Started')
    command = takecommand()

    if 'close this tab' in command:
        keyboard.press_and_release('ctrl + w')

    elif 'open new tab' in command:
        keyboard.press_and_release('ctrl + t')

    elif 'open new window' in command:
        keyboard.press_and_release('ctrl + n')

    elif 'show history' in command:
        keyboard.press_and_release('ctrl + h')

    elif 'show downloads' in command:
        keyboard.press_and_release('ctrl + j')

#C programs
def Cprogram():
    
        ui.terminalPrint("What is the name of the program : ")
        c_prog = takecommand()

        if 'even' in c_prog:
            os.startfile('D:\\Project III Year\\Code Database\\evenodd.py.txt')
            ui.terminalPrint("Successfully Opened even odd program")

        elif 'alphabet' in c_prog:
            os.startfile('d:\\Project III Year\\Code Database\\Alphabet.txt')
            ui.terminalPrint("Successfully Opened Alphabet program")


        elif 'area of rectangle' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\arearofrect.txt')
            ui.terminalPrint("Successfully Opened area of rectangle program")


        elif 'add two numbers' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\addtwonumbers.txt')
            ui.terminalPrint("Successfully Opened add two numbers program")

        elif 'ascii value' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\ASCIIvalue.txt')
            ui.terminalPrint("Successfully Opened ASCII value program")

        elif 'calculator' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\Calculator.txt')
            ui.terminalPrint("Successfully Opened calculator program")

        elif 'character pattern' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\characterpattern.txt')
            ui.terminalPrint("Successfully Opened characterpattern program")

        elif 'factorial' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\factorial.txt')
            ui.terminalPrint("Successfully Opened factorial program")

        elif 'fibonacci' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\fibonacci.txt')
            ui.terminalPrint("Successfully Opened fibonacci program")

        elif 'compound interest' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\Compoundinterest.txt')
            ui.terminalPrint("Successfully Opened Compound interest program")

        elif 'concatenate' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\Concatenate.txt')
            ui.terminalPrint("Successfully Opened concatenate program")

        elif 'diamond pattern' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\diamondpattern.txt')
            ui.terminalPrint("Successfully Opened diamond pattern program")

        elif 'factor of number' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\Factorsofnumber.txt')
            ui.terminalPrint("Successfully Opened factor of number program")

        elif 'inverted hollow star pattern' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\invertedhollowstarpattern.txt')
            ui.terminalPrint("Successfully Opened inverted hollow star pattern program")

        elif 'largest number in array' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\largenumberinarray.txt')
            ui.terminalPrint("Successfully Opened largest number in array program")

        elif 'lcm of two numbers' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\LCMoftwonumbers.txt')
            ui.terminalPrint("Successfully Opened lcm of two numbers program")

        elif 'leapyear' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\leapyear.txt')
            ui.terminalPrint("Successfully Opened leapyear program")

        elif 'length of string' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\lengthofstring.txt')
            ui.terminalPrint("Successfully Opened length of string program")

        elif 'long keyword' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\longkeyword.txt')
            ui.terminalPrint("Successfully Opened long keyword program")

        elif 'max and min array' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\maxandminarray.txt')
            ui.terminalPrint("Successfully Opened max and min array program")

        elif 'multiply two matrix' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\multiplytwomatrix.txtt')
            ui.terminalPrint("Successfully Opened multiply two matrix program")

        elif 'natural number' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\naturalnumber.txt')
            ui.terminalPrint("Successfully Opened natural number program")

        elif 'number pattern' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\numberpattern.txt')
            ui.terminalPrint("Successfully Opened number pattern program")

        elif 'palindrome' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\Palindrome.txt')
            ui.terminalPrint("Successfully Opened palindrome program")

        elif 'perimeter of rectangle' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\perimterofrect.txtt')
            ui.terminalPrint("Successfully Opened perimeter of rectangle program")

        elif 'postitve' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\positivenegative.txt')
            ui.terminalPrint("Successfully Opened positive negative program")

        elif 'power' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\powerofnumber.txt')
            ui.terminalPrint("Successfully Opened power of number program")

        elif 'prime number' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\Primenumber.txt')
            ui.terminalPrint("Successfully Opened prime number program")

        elif 'pyramid' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\pyramidpattern.txt')
            ui.terminalPrint("Successfully Opened pyramid pattern program") 

        elif 'root' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\rootofQuadraticequ.txt')
            ui.terminalPrint("Successfully Opened root of quadratic equation program") 

        elif 'quotient and remainder' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\QuotientandRemainder.txt')
            ui.terminalPrint("Successfully Opened quotient and remainder program") 

        elif 'reverse' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\reversenumber.txt')
            ui.terminalPrint("Successfully Opened reverse number program") 

        elif 'search in array' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\searchinarray.txt')
            ui.terminalPrint("Successfully Opened search in array program") 

        elif 'simple interest' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\Simpleinterest.txt')
            ui.terminalPrint("Successfully Opened simple interest program") 

        elif 'size of data type' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\sizeofdatatype.txt')
            ui.terminalPrint("Successfully Opened size of datatype program") 

        elif 'sort a string' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\sortastring.txt')
            ui.terminalPrint("Successfully Opened sort a string program") 

        elif 'swap two numbers' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\swaptonumbers.txt')
            ui.terminalPrint("Successfully Opened swap two numbers program") 

        elif 'table' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\table.txt')
            ui.terminalPrint("Successfully Opened table program") 

        elif 'transpose' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\transpose.txt')
            ui.terminalPrint("Successfully Opened transpose program") 

        elif 'triangle' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\triangle.txt')
            ui.terminalPrint("Successfully Opened triangle program") 

        elif 'two array' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\twodarray.txt')
            ui.terminalPrint("Successfully Opened two array program")

        elif 'vowel' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\Vowelorconsonant.txt')
            ui.terminalPrint("Successfully Opened vowel and consonant program") 

        elif 'array rotation' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\arrayrotation.txt')
            ui.terminalPrint("Successfully Opened array rotation program")

        elif 'input' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\input.txt')
            ui.terminalPrint("Successfully Opened input program")

        elif 'large number in array' in c_prog:
            os.startfile('d:\\Project III Year\\c program\\largenumberinarray.txt')
            ui.terminalPrint("Successfully Opened large number in array program")  

        else:
            sub = "Write a code for " + c_prog + " in C"
            ai(prompt = sub) 

#C++ Programs
def Cppprogram():

         ui.terminalPrint("What is the name of the program ? ")
         cpp_prog = takecommand()

         if 'even' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\evenodd.txt')
            ui.terminalPrint("Successfully Opened even odd program")
            
         elif 'factorial' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\factorial.txt')
            ui.terminalPrint("Successfully Opened factorial program")

         elif 'add two numbers' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\addtwono.txt')
            ui.terminalPrint("Successfully Opened add two numbers program")

         elif 'armstrong' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\armstrong.txt')
            ui.terminalPrint("Successfully Opened armstrong program")

         elif 'ascii value' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\asciivalue.txt')
            ui.terminalPrint("Successfully Opened ascii value program")

         elif 'factor of number' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\factorofnumber.txt')
            ui.terminalPrint("Successfully Opened factor of number program")

         elif 'fibonacci' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\fibonacci.txt')
            ui.terminalPrint("Successfully Opened fibonacci program")

         elif 'lcm' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\lcm.txt')
            ui.terminalPrint("Successfully Opened lcm program")

         elif 'leap year' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\leapyear.txt')
            ui.terminalPrint("Successfully Opened leap year program")

         elif 'string length' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\lengthofstring.txt')
            ui.terminalPrint("Successfully Opened string length program")

         elif 'table' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\multiplicationtable.txt')
            ui.terminalPrint("Successfully Opened multiplication table program")

         elif 'palindrome' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\palindrome.txt')
            ui.terminalPrint("Successfully Opened palindrome program")

         elif 'power' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\power.txt')
            ui.terminalPrint("Successfully Opened power program")

         elif 'prime' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\prime.txt')
            ui.terminalPrint("Successfully Opened prime program")

         elif 'concatenate' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\concatenatestring.txt')
            ui.terminalPrint("Successfully Opened concatenate program")

         elif 'string copy' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\copyofstring.txt')
            ui.terminalPrint("Successfully Opened string copy program")  

         elif 'gcd' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\gcd.txt')
            ui.terminalPrint("Successfully Opened gcd program")

         elif 'largest three number' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\largestthreenumbers.txt')
            ui.terminalPrint("Successfully Opened largest three number program")

         elif 'postfix' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\postfixincrement.txt')
            ui.terminalPrint("Successfully Opened postfix increment program")

         elif 'prefix' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\prefixincrement.txt')
            ui.terminalPrint("Successfully Opened prefix program")

         elif 'print string' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\printstring.txt')
            ui.terminalPrint("Successfully Opened print string program")

         elif 'quotient' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\quotient.txt')
            ui.terminalPrint("Successfully Opened quotient program")

         elif 'remainder' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\remainder.txt')
            ui.terminalPrint("Successfully Opened remainder program")

         elif 'pyramid' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\pyramid.txt')
            ui.terminalPrint("Successfully Opened pyramid program")

         elif 'quadratic' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\quadratic.txt')
            ui.terminalPrint("Successfully Opened quadratic program") 
    
         elif 'reverse' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\reversenumber.txt')
            ui.terminalPrint("Successfully Opened reverse number program")

         elif 'data type size' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\sizeofdatatype.txtt')
            ui.terminalPrint("Successfully Opened data type size program")

         elif 'sum of natural number' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\sumofnaturalno.txt')
            ui.terminalPrint("Successfully Opened sum of natural number program")

         elif 'swap' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\swap.txt')
            ui.terminalPrint("Successfully Opened swap number program")

         elif 'user input' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\userenterno.txt')
            ui.terminalPrint("Successfully Opened user enter number program")

         elif 'vowel' in cpp_prog:
            os.startfile('d:\\Project III Year\\cpp program\\vowelconsonent.txt')
            ui.terminalPrint("Successfully Opened vowel and cansonant program")

         else:
            sub1 = "Write a code for " + cpp_prog + " in C++"
            ai(prompt = sub1) 

# java Programs
def java():

         ui.terminalPrint("What is the name of the program ? ")
         j_prog = takecommand()

         if 'even' in j_prog:
            os.startfile('D:\\Project III Year\\javaevenodd.txt')
            ui.terminalPrint("Successfully Opened even odd program")

         elif 'add two number' in j_prog:
            os.startfile('D:\\Project III Year\\javaaddtwonumber.txt')
            ui.terminalPrint("Successfully Opened add two number program")

         elif 'alphabet' in j_prog:
            os.startfile('D:\\Project III Year\\javaalphabet.txt')
            ui.terminalPrint("Successfully Opened alphabet program")

         elif 'ascii value' in j_prog:
            os.startfile('D:\\Project III Year\\javaasciivalue.txt')
            ui.terminalPrint("Successfully Opened ascii value program")

         elif 'factorial' in j_prog:
            os.startfile('D:\\Project III Year\\javafactorial.txt')
            ui.terminalPrint("Successfully Opened factorial program")

         elif 'fibonacci' in j_prog:
            os.startfile('D:\\Project III Year\\javafibonacci.txt')
            ui.terminalPrint("Successfully Opened fibonacci program")

         elif 'gcd' in j_prog:
            os.startfile('D:\\Project III Year\\javagcd.txt')
            ui.terminalPrint("Successfully Opened gcd and cansonant program")

         elif 'largest three number' in j_prog:
            os.startfile('D:\\Project III Year\\javalargestthreenumbers.txt')
            ui.terminalPrint("Successfully Opened largest three number program")

         elif 'lcm' in j_prog:
            os.startfile('D:\\Project III Year\\javalcm.txt')
            ui.terminalPrint("Successfully Opened lcm program")

         elif 'leap year' in j_prog:
            os.startfile('D:\\Project III Year\\javaleapyear.txt')
            ui.terminalPrint("Successfully Opened leap year program")

         elif 'multiply' in j_prog:
            os.startfile('D:\\Project III Year\\javamultiplytwono.txt')
            ui.terminalPrint("Successfully Opened multiply program")

         elif 'positive' in j_prog:
            os.startfile('D:\\Project III Year\\javapositivenegative.txt')
            ui.terminalPrint("Successfully Opened positive and negative program")

         elif 'neagtive' in j_prog:
            os.startfile('D:\\Project III Year\\javapositivenegative.txt')
            ui.terminalPrint("Successfully Opened positive and negative program")

         elif 'quadratic' in j_prog:
            os.startfile('D:\\Project III Year\\javaquadratic.txt')
            ui.terminalPrint("Successfully Opened quadratic program")

         elif 'quotient' in j_prog:
            os.startfile('D:\\Project III Year\\javaquotient.txt')
            ui.terminalPrint("Successfully Opened quotient program")

         elif 'remainder' in j_prog:
            os.startfile('D:\\Project III Year\\javaremainder.txt')
            ui.terminalPrint("Successfully Opened remainder program")

         elif 'natural number sum' in j_prog:
            os.startfile('D:\\Project III Year\\javasumofnaturalnumber.txt')
            ui.terminalPrint("Successfully Opened natural number sum program")

         elif 'swap' in j_prog:
            os.startfile('D:\\Project III Year\\javaswap.txt')
            ui.terminalPrint("Successfully Opened swap program")

         elif 'vowel' in j_prog:
            os.startfile('D:\\Project III Year\\javavowelconsonant.txt')
            ui.terminalPrint("Successfully Opened vowel and cansonant program")

         else:
            sub3 = "Write a code for " + j_prog + " in Java"
            ai(prompt = sub3)

# Asp Programs
def asp() :
    ui.terminalPrint("What is the name of the program ? ")
    asp_prog = takecommand()
    sub4 = "Write a code for " + asp_prog + " in Asp.net"
    ai(prompt = sub4)

# Python Programs
def python() :
    ui.terminalPrint("What is the name of the program ? ")
    pyt_prog = takecommand()
    sub5 = "Write a code for " + pyt_prog + " in Python"
    ai(prompt = sub5)

# html Programs
def html() :
    ui.terminalPrint("What is the name of the program ? ")
    htm_prog = takecommand()
    sub6 = "Write a code for " + htm_prog + " in HTML"
    ai(prompt = sub6)

# C# programs    
def cs() :
    ui.terminalPrint("What is the name of the program ? ")
    cs_prog = takecommand()
    sub7 = "Write a code for " + cs_prog + " in C#"
    ai(prompt = sub7)

# javascript programs
def js() :
    ui.terminalPrint("What is the name of the program ? ")
    js_prog = takecommand()
    sub8 = "Write a code for " + js_prog + " in javascript"
    ai(prompt = sub8)

# Code Mode
def code():
    while True:
        
        ui.terminalPrint("In which language do you want the code ?")
        query = takecommand()
        if "C".upper() in query:
            Cprogram()
            ui.terminalPrint("Anything else needed ?")
            ans = takecommand()
            if "no" in ans:
                ui.terminalPrint("Exiting Code Mode")
                break
            else:
                continue

        elif "c" in query:
            Cprogram()
            ui.terminalPrint("Anything else needed ?")
            ans = takecommand()
            if "no" in ans:
                ui.terminalPrint("Exiting Code Mode")
                break
            else:
                continue
                

        elif 'see' in query:
            Cprogram()
            ui.terminalPrint("Anything else needed ?")
            ans = takecommand()
            if "no" in ans:
                ui.terminalPrint("Exiting Code Mode")
                break
            else: 
                continue
                

        elif 'c plus plus' in query:
            Cppprogram()
            ui.terminalPrint("Anything else needed ?")
            ans = takecommand()
            if "no" in ans:
                ui.terminalPrint("Exiting Code Mode")
                break
            else: 
                continue
                

        elif 'see plus plus' in query:
            Cppprogram()
            ui.terminalPrint("Anything else needed ?")
            ans = takecommand()
            if "no" in ans:
                ui.terminalPrint("Exiting Code Mode")
                break
            else: 
                continue
                

        elif 'cpp' in query:
            Cppprogram()
            ui.terminalPrint("Anything else needed ?")
            ans = takecommand()
            if "no" in ans:
                ui.terminalPrint("Exiting Code Mode")
                break
            else: 
                continue
                

        elif 'see PP' in query:
            Cppprogram() 
            ui.terminalPrint("Anything else needed ?")
            ans = takecommand()
            if "no" in ans:
                ui.terminalPrint("Exiting Code Mode")
                break
            else: 
                continue
                  

        elif 'java' in query:
            java()
            ui.terminalPrint("Anything else needed ?")
            ans = takecommand()
            if "no" in ans:
                ui.terminalPrint("Exiting Code Mode")
                break
            else: 
                continue
                

        elif 'asp' in query:
            asp()
            ui.terminalPrint("Anything else needed ?")
            ans = takecommand()
            if "no" in ans:
                ui.terminalPrint("Exiting Code Mode")
                break
            else: 
                continue
                

        elif 'python' in query:
            python()
            ui.terminalPrint("Anything else needed ?")
            ans = takecommand()
            if "no" in ans:
                ui.terminalPrint("Exiting Code Mode")
                break
            else: 
                continue
                

        elif 'html' in query:
            html()
            ui.terminalPrint("Anything else needed ?")
            ans = takecommand()
            if "no" in ans:
                ui.terminalPrint("Exiting Code Mode")
                break
            else: 
                continue
                

        elif 'javascript' in query:
            js()
            ui.terminalPrint("Anything else needed ?")
            ans = takecommand()
            if "no" in ans:
                ui.terminalPrint("Exiting Code Mode")
                break
            else: 
                continue
                

        elif 'c sharp' in query:
            cs()
            ui.terminalPrint("Anything else needed ?")
            ans = takecommand()
            if "no" in ans:
                ui.terminalPrint("Exiting Code Mode")
                break
            else: 
                continue
                

        #to close notepad
        elif "close" in query:
            ui.terminalPrint('closing notepad')
            os.system("taskkill /f /im notepad.exe")

        
        # elif 'exit' in query:
        #     ui.terminalPrint('exiting command mode')
        #     break

#Chat Mode
def chatmode():
    ui.terminalPrint('Jarvis Switched to Chat Mode.')
    while True:
        
        query = takecommand().lower()
        print(query)

        if 'exit chat mode' in query:
            ui.terminalPrint('Chat mode exited')
            break

        else:
            chat(query)

def main():
    wishMe()
    while True:

        query = takecommand().lower()
        print(query)

        #Search in Wikipedia
        if 'wikipedia' in query:
            ui.terminalPrint('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            ui.terminalPrint("According to Wikipedia :")
            ui.terminalPrint(results)
            

        #Create a new folder
        elif 'new folder' in query:
            keyboard.press_and_release('ctrl + shift + n')

        #Search anything on youtube
        elif 'youtube' in query:

            ui.terminalPrint('Ok Sir, This is what I found for you!')
            query = query.replace("jarvis", "")
            query = query.replace("youtube", "")
            query = query.replace("search", "")
            query = query.replace("on", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)

            ui.terminalPrint('Done Sir!')

        #To start the youtube automation
        elif 'video tool ' in query:
            YoutubeAuto()

        elif 'pause' in query:
            keyboard.press('k')

        elif 'restart video' in query:
            keyboard.press('0')

        elif 'no volume' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('1')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            ui.terminalPrint('Okay Sir')
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        #Chrome Automation
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'show history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'show downloads' in query:
            keyboard.press_and_release('ctrl + j')

        elif 'chrome automation' in query:
            ChromeAuto()

        # Seacrh through web
        elif 'search' in query:
            ui.terminalPrint("This is what I found for you on google")
            query = query.replace("jarvis", "")
            query = query.replace("on", "")
            query = query.replace("google", "")
            query = query.replace("search", "")
            kit.search(query)

        #Search any website
        elif 'website' in query:
            ui.terminalPrint('Tell me the name of the Website')
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            ui.terminalPrint('Done Sir')

        #Playing any song
        elif 'play a song' in query:
            music()

        # To know the IP
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            ui.terminalPrint(f'Your IP adress is {ip}')

        # To open the command query
        elif 'command' in query:
            ui.terminalPrint('opening CMD')
            os.system("start cmd")

        # To get the current time
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            ui.terminalPrint(f"Sir,The Time is {strTime}")

        #to close notepad
        elif 'close notepad' in query:
            ui.terminalPrint('closing notepad')
            os.system("taskkill /f /im notepad.exe")

        #To open notepad
        elif 'open notepad' in query:
            ui.terminalPrint('opening notepad')
            codePad = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(codePad)
        
        #to open vs code
        elif 'open vs code' in query:
            ui.terminalPrint('opening vs code')
            codePad = "C:\\Users\\shiva\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePad)

        #to open vs code
        elif 'open visual studio code' in query:
            ui.terminalPrint('opening visual studio code')
            codePad = "C:\\Users\\shiva\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePad)

        #to close vs code
        elif 'close vs code' in query:
            ui.terminalPrint('closing vs code')
            os.system("taskkill /f /im Code.exe") 
               
        #to open ms word
        elif 'word' in query:
                ui.terminalPrint('opening ms word')
                codePad = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(codePad)

        #to close ms word
        elif 'close ms word' in query:
            ui.terminalPrint('closing ms word')
            os.system("taskkill /f /im winword.exe")       

        #to open ms excel
        elif 'open excel' in query:
                ui.terminalPrint('opening ms excel')
                codePad = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(codePad)

        #to close ms excel
        elif 'close excel' in query:
            ui.terminalPrint('closing ms excel')
            os.system("taskkill /f /im excel.exe")

        #to open power point
        elif 'open power point' in query:
                ui.terminalPrint('opening power point')
                codePad = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(codePad)

        # to close power point
        elif 'close power point' in query:
            ui.terminalPrint('closing power point')
            os.system("taskkill /f /im powerpnt.exe")

        # To take a screenshot and deciding the name of the file
        elif 'screenshot' in query:
            ui.terminalPrint('ok sir what should I name that file?')
            path = takecommand()
            pathext = path + ".png"
            screenpath = "D:\\Project III Year\\Screenshots\\" + pathext
            kk = pyautogui.screenshot()
            kk.save(screenpath)
            os.startfile(screenpath)
            ui.terminalPrint('Here is your screenshot')

        #To open instagram through web browser
        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com')

        #To change the voice to female
        elif 'female' in query:
                engine.setProperty('voice', voices[1].id)
                ui.terminalPrint("This is my female voice")

        #To chnange to voice to male
        elif 'male' in query:
                engine.setProperty('voice', voices[0].id)
                ui.terminalPrint("This is the male voice")

        # Commanding the AI to repeat after the user
        elif 'repeat after me' in query:
            ui.terminalPrint('Okay Sir! Please Start Speaking')
            words = takecommand()
            ui.terminalPrint(f"You said : {words}")

        #restart, shutdown, sleep
        elif 'shutdown' in query:
            ui.terminalPrint('shutting down')
            os.system("shutdown /s /t 5")

        elif 'shut down' in query:
            ui.terminalPrint('shutting down')
            os.system("shutdown /s /t 5")

        elif 'bye' in query:
            ui.terminalPrint('Thanks Sir for using me, Have a good day')
            sys, exit()

        elif 'back' in query:
            ui.terminalPrint('Welcome Back Sirr.. I was waiting for you')

        elif 'quit' in query:
            ui.terminalPrint('Okay Sir Byee, you can call me anytime')
            break

        # For opening code mode
        elif 'code' in query:
            code()
            
        elif 'programming' in query:
            code()

        #Open Chat mode
        elif 'chat' in query:
            ui.terminalPrint('Opening Chat Mode')
            chatmode()

        else : 
            ui.terminalPrint('Say Again')

app = QApplication(sys.argv)
ui = Main()
ui.show()
sys.exit(app.exec_())

