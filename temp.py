import pyttsx3
import requests
import sys
from weather import weather_status
import webbrowser
import speech_recognition as sr

api_key = "8337917e3d9e4475bf943453251801"  # Replace with your actual API key

def get_weather(location):
    print(location)
    result = weather_status(api_key, location)
    if isinstance(result, list):  # Check if the result is valid
        temp = result[0]
        feels = result[1]
        humidity = result[2]
        speak(f"At {location}, the temperature is {temp} degree Celsius, but it feels like {feels} degree Celsius, and the humidity is {humidity} percent.")
    else:
        speak("Sorry, I couldn't fetch the weather data. Please check the location or your API key.")

def speak(text):
    tts_engine = pyttsx3.init()
    rate = tts_engine.getProperty("rate")
    voices = tts_engine.getProperty("voices")
    tts_engine.setProperty("voice", voices[1].id)  # Female voice for better speech
    tts_engine.setProperty('rate', rate - 15)
    tts_engine.say(text)
    tts_engine.runAndWait()

def command_process(input_text):
    string = input_text.lower()
    
    # Check if the user mentioned weather command
    if "weather" in string and "at" in string:
        location = string.split() # Extract location after 'at'

        get_weather(location[-1])

jarvis_init = False  # Flagged at false initially

if __name__ == "__main__":

    print("Listening.......")
    r = sr.Recognizer()
    mic = sr.Microphone()
    
    while True:
        try:
            with mic as source:
                print("Recognizing.......")
                input_audio = r.listen(source)
                input_text = r.recognize_google(input_audio)
        
            print(input_text)

            if input_text.lower() in ["hello jarvis", "hello jarvi", "hello jarv", "hello jar", "jarvis"]:
                speak("Hello, I am Jarvis.")
                jarvis_init = True
            
            if jarvis_init:
                command_process(input_text)
            
        except sr.UnknownValueError:
            print("Didn't recognize audio input. Try again.")
            speak("I didn't understand that. Please try again.")
        except Exception as e:
            print("Error:", e)
            speak("An unexpected error occurred. Please try again.")
