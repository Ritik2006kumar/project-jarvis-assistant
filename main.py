import speech_recognition as sr # install this icetension
import webbrowser
import pyttsx3    #pip install pyttsx3 
import musicLibrary
import requests
from openai import OpenAI
# pip install speechrecognition pyaudio
# pip install setuptools
#install audio




recognizer = sr.Recognizer()
engine = pyttsx3.init()
news_api="48c96c603ae9442da2b36fca7e86d249"
# convert the text into voice


def speak(text):
    engine.say(text)
    engine.runAndWait ()

def aiprocess(command):
    client = OpenAI(
    api_key="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"
    )
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages =[
        {"role" :"stystem" ,"content":"you are a virtual assistant named jarvis skilling in gernal tasks like alexa ,google could"} ,
        {"role":"user","contant": command}  
     ]
    )

    return completion.choices[0].message.content


def processCommand(c):    
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com") 
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")   
    elif c.lower().startswitch("play"): 
        song=c.lower().split(" ")[1]
        link= musicLibrary.music[song]  
        webbrowser.open(link) 
    elif "what is the weather" in c.lower():
        webbrowser.open("https://weather.com")   
    elif "open chatGPT" in c.lower():
        webbrowser.open("https://chatGPT.com")
    elif "open code with harry" in c.lower():
        webbrowser.open("https://www.codewithharry.com/") 
    elif " the news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apikey={news_api}")
        if r.status_code == 200:
            #parse the json response
            data =r.json

            #extract the article
            articles =data.get('articles' , [])

            for article in articles:
                speak(article['title'])
            # speak a news 
    else:
         output = aiprocess(command)
         speak(output)     




if __name__ == "__main__":
    speak("initializing jarvis......")
    while True:
        #listen for the wake word "jarvis"
        #obtain audio form the microphone 
        r = sr.Recognizer()
        print("recognizing....")
            #recorgnize speech using sphinx


        try:
            with sr.Microphone() as sourse:
               print("listing...... ")
               audio =r.listen(sourse , timeout=2, phrase_time_limit=2)

            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
              speak("ya")
              #listen for command

            

            with sr.Microphone() as sourse:
               print("jarvis active")
               audio =r.listen(sourse)
               command =r.recognize_google(audio)

               processCommand(command)


  
        except sr.UnknownValueError:
            print("jarvis active ...")

        except Exception as e:
            print(" error; {0}" .format(e))






