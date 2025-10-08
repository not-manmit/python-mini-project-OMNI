import pyttsx3
import sys
import url
from weather import weather_status
from news import fetch_news
import webbrowser
import speech_recognition as sr

api_key = "Your weather API key"
def get_weather(location):
    result = weather_status(api_key, location)
    if isinstance(result, list):  # Check if the result is valid
        temp = result[0]
        feels = result[1]
        humidity = result[2]
        print(f"At {location}, the temperature is {temp} degree Celsius, but it feels like {feels} degree Celsius, and the humidity is {humidity} percent.")
        speak(f"At {location}, the temperature is {temp} degree Celsius, but it feels like {feels} degree Celsius, and the humidity is {humidity} percent.")
    else:
        speak("Sorry, I couldn't fetch the weather data. Please check the location or your API key.")

def speak(text):
    tts_engine = pyttsx3.init()
    rate = tts_engine.getProperty("rate")
    voices = tts_engine.getProperty("voices")
    tts_engine.setProperty("voice", voices[1].id) #Female voice for better speech
    tts_engine.setProperty('rate', rate - 15)
    tts_engine.say(text)
    tts_engine.runAndWait()

def command_process(input_text):
    if(input_text.lower() == "open youtube"):
        webbrowser.open(url.URL.youtube)
    elif(input_text.lower() == "open github"):
        webbrowser.open(url.URL.github)
    elif(input_text.lower() == "open linkedin"):
        webbrowser.open(url.URL.linkedin)
    elif(input_text.lower() == "open instagram"):
        webbrowser.open(url.URL.instagram)

    elif(input_text.lower() in ["play blinding lights", "play blinding light", "blinding light"]):
        webbrowser.open(url.Music.blinding_lights)
    elif(input_text.lower() in ["play faded", "play fade"]):
        webbrowser.open(url.Music.faded)
    elif(input_text.lower() in ["play alone", "play all"]):
        webbrowser.open(url.Music.alone)
    elif(input_text.lower() in ["play interstellar", "play insternal"]):
        webbrowser.open(url.Music.interstellar)
    
    string = input_text.lower()
    if("weather" in string and "at" in string):
        location = string.split()
        get_weather(location[-1])

    elif("current affair" in input_text.lower()):
        speak(fetch_news())
    

    #To exit the process
    elif(input_text.lower() in ["exit process", "abort"]):
        print("Bye!")
        speak("Have a good day mate, see you again!")
        sys.exit()

omni_init = False #flagged at false initially

if __name__ == "__main__":
    speak("Initialising Omni!")
    print("Listening.......")
    r = sr.Recognizer()
    mic = sr.Microphone()
    while True:
        try:
            with mic as source:
                print("Recognizing.......")
                input_audio = r.listen(source, phrase_time_limit = 3)
                input_text = r.recognize_google(input_audio)
        
            print(input_text)

            if(input_text.lower() in ["hello omni", "hello om", "hello omnee", "hello omn", "omni"]):
                speak("Hello, I am Omni.")
                omni_init = True
            
            if (omni_init == True):
                command_process(input_text)
            
        except sr.UnknownValueError:
            print("Didn't recognize audio input. Try again.")
            speak("I didn't understand that. Please try again.")
        except Exception as e:
            print("Error:", e)
            speak("An unexpected error occurred. Please try again.")