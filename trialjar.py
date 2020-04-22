import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests
import json
import urllib.request
from bs4 import BeautifulSoup



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
Voice_rate = 225
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate' , Voice_rate)

def response(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        response("Good Morning!")

    elif hour>=12 and hour<18:
        response("Good Afternoon!")   

    else:
        response("Good Evening!")  

    response("I am your assistant . Please tell me what can i do for you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  #duration=1
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)

    except Exception as e:
        # print(e)    
        print("can you say that again please i didn't get it properly...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            response('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            response("According to Wikipedia")
            print(results)
            response(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)    
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            response("Sir, the time is {strTime}")

        elif 'email to person' in query:
            try:
                response("What should I say?")
                content = takeCommand()
                to = "personemail@gmail.com"    
                sendEmail(to, content)
                response("Email has been sent!")
            except Exception as e:
                print(e)
                response("Sorry my friend person. I am not able to send this email")

        elif 'stop' in query:
            break

        elif 'get news' in query:
            response("News for today...")
            url = ('http://newsapi.org/v2/top-headlines?country=in&apiKey=f3ef8f0f1939482491de40ee5f8686df')
            news = requests.get(url)
            news_dict = news.json()
            arts = news_dict['articles']

            for articles in arts:
                try:

                    response(articles['title'])
                    response('')
                except:
                    response(articles['title'].encode('utf-8'))

        elif 'give me a weather of' in query:
            place = query[20:]
            url ="http://api.weatherstack.com/current?access_key=4d84d938c204df5773539c9affb09078&query="+place
            responses = requests.get(url)
            weather = responses.json()
            try:
                temp = weather['current']['temperature']
                response("temprature is")
                response(temp)
                des = weather['current']['weather_descriptions']
                dire = weather['current']['wind_dir']
                humidity = weather['current']['humidity']
                uv =weather['current']['uv_index']
                response("weather is")
                response(des)
                response("wind directions is")
                response(dire)
                response("humidity")
                response(humidity)
                response("U v index")
                response(uv)
            except:
                response("try again")            
           