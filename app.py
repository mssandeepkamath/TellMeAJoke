import requests,pyttsx3,json,speech_recognition as sr

class Joke:

    def __init__(self,set_up,punch_line) -> None:
        self.set_up=set_up
        self.punch_line=punch_line

    def __str__(self) -> str:
        return f"{self.set_up},{self.punch_line}"
        
r=sr.Recognizer()

url:str="https://official-joke-api.appspot.com/random_joke"

def joke_reader():
    
    response=requests.get(url)

    data=json.loads(response.text)

    joke=Joke(data["setup"],data["punchline"])

    pyttsx3.speak(joke)

def error_reader():
    pyttsx3.speak("Sorry, couldn't understand you")


def listner_daemon():

    try:

        with sr.Microphone() as source2:
            

            r.adjust_for_ambient_noise(source2, duration=1)
             
            
            audio2 = r.listen(source2)
             
            
            MyText = r.recognize_google(audio2)

            MyText = MyText.lower()

 
            if(MyText=="tell me a joke"):

                joke_reader()

            else:

                 error_reader()

    except sr.RequestError as e:

        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:

        print("unknown error occurred")


print("Say: \"Tell me a joke\"")         

listner_daemon()
    