import os
import speech_recognition as sr


def takecommand():
    # It takes microphone input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening...")
        print("Listening..")

        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        # print("Recognizing...")
        print("Recognizing...")

        query = r.recognize_google(audio, language='en-in')
        # print(f"User said: {query}\n")
        print(f"User said: {query}\n")


    except Exception as e:
        # printint("I was not able to recognize")

        return "none"
    return query.lower()


while True:
    wake_Up = takecommand()
    
    if 'jarvis' in wake_Up:
        os.startfile('D:\\Project III Year\\chat.py')


    else:
        print("Nothing.....")


    
