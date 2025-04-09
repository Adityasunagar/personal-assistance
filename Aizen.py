# Aizen.py
# This is a simple voice assistant program that can do the following:
# 1. Wish the user according to the time of the day
# 2. Take voice input from the user and convert it to text
# 3. Search Wikipedia for information
# 4. Open YouTube, Google, and StackOverflow    
# 5. Play music from the computer
# 6. Tell the time
# 7. Open Visual Studio Code
# 8. Open Google News
# 9. Open the weather website
# 10. Set a reminder
# 11. Send an email to a specific email address
# 12. Quit the program

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
import os
import random
import smtplib
import requests
import json
import psutil
from textblob import TextBlob

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#function to speak the string which is passed to it as an argument
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#function to wish the user according to the time of the day and greet the user

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good Evening!")
    print("Greetings. I am Aizen, your personal assistant. How may I assist you today?" )
    speak("Greetings. I am Aizen, your personal assistant. How may I assist you today?")

#this function will take the user's voice input and convert it to text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("I apologize, could you kindly repeat that?")
        speak("I apologize, could you kindly repeat that?")
        return None
    return query

#this function will detect the emotion of the user based on the input provided
def detect_emotion(user_input):
    sentiment = TextBlob(user_input).sentiment.polarity
    return (
        "I sense positivity. That is great!" if sentiment > 0
        else "You seem upset. I am here to assist." if sentiment < 0
        else "I detect neutrality. How can I help you?"
    )

#this function will return the system status including battery level and cpu usage
def system_status():
    cpu_usage = psutil.cpu_percent()
    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else "Unknown"
    return f"CPU usage is {cpu_usage}%. Battery level is at {battery_percent}%"

#this function will return a random joke
def tell_joke():
    return pyjokes.get_joke()

def calculate(expression):
    try:
        result = eval(expression)
        print(f"The result of {expression} is {result}")
        speak(f"The result of {expression} is {result}")
    except:
        speak("I couldn't calculate that.") 
            

#main function to execute the voice assistant program 
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if query is None:
            continue

        query = query.lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for your query. Please be more specific.")
                print(e.options)
            except wikipedia.exceptions.PageError:
                speak("I could not find any results for your query.")
            except wikipedia.exceptions.WikipediaException as e:
                speak("An error occurred while searching Wikipedia.")
                print(e)

        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening StackOverflow...")
            webbrowser.open("stackoverflow.com")

        elif 'play music' or 'play a song' in query:
            music_dir = 'F:\\music'
            songs = os.listdir(music_dir)
            if songs:
                speak("I found some songs in your music directory. Would you like to play a random song?")
                response = takeCommand()
                if response is None:
                    continue
                if 'yes' in response or 'sure' in response:
                    random_song = random.choice(songs)
                    os.startfile(os.path.join(music_dir, random_song))
                else:
                    speak("Here are a few options.")
                    for i, song in enumerate(songs[:5]):  # Show only the first 5 songs
                        print(f"{i + 1}. {song}")
                        speak(f"Option {i + 1}: {song}")
                    speak("Please say the number of the song you want to play.")
                    song_number = takeCommand()
                    if song_number is None:
                        continue
                    if song_number.isdigit():
                        song_index = int(song_number) - 1
                        if 0 <= song_index < len(songs):
                            os.startfile(os.path.join(music_dir, songs[song_index]))
                        else:
                            speak("Invalid number. Playing the first song.")
                            os.startfile(os.path.join(music_dir, songs[0]))
                    else:
                        speak("No valid input received. Playing the first song.")
                        os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("No music files found in the directory. Please make sure the directory is not empty and try again.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%A, %B %d, %Y")
            print(f" the date is {strDate}")
            speak(f"The date is {strDate}")

        elif 'open code' in query:
            speak("Opening Visual Studio Code...")
            codePath = "C:\\Users\\ADITYA\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)

        elif 'news' in query:
            speak("Opening Google News...")
            webbrowser.open("https://news.google.com")

        elif 'weather' in query:
            speak("Opening weather website...")
            webbrowser.open("https://www.weather.com")

        elif 'set reminder' in query:
            speak("What shall I remind you about?")
            reminder = takeCommand()
            if reminder is None:
                continue
            speak(f"Reminder set for: {reminder}")

        elif 'open gmail' in query:
            speak("Opening Gmail...")
            webbrowser.open("https://mail.google.com")

        elif 'system status' in query:
            status = system_status()
            print(status)
            speak(status)

        elif 'tell me a joke' in query:
            joke = tell_joke()
            print(joke)
            speak(joke)

        elif 'how are you' in query:
            print("I am doing well. Thank you for asking!")
            speak("I am doing well. Thank you for asking!")

        elif 'detect emotion' in query:
            speak("I am analyzing your emotions. Please wait...")
            emotion = detect_emotion(query)
            print(emotion)
            speak(emotion)

        elif 'calculate' in query:
            speak("What should I calculate?")
            expression = takeCommand()
            if expression:
                calculate(expression)

            
        elif 'quit' in query:
            print("As you wish, Master. Until we meet again, farewell!")
            speak("As you wish, Master. Until we meet again, farewell!")
            break

        elif 'back to code' in query:
            print("Taking you back to the code editor...")
            speak("Taking you back to the code editor...")
            code_editor_path = "C:\\Users\\ADITYA\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(code_editor_path)
            break

        elif 'shutdown' in query:
            speak("Are you sure you want to shut down the system?")
            confirmation = takeCommand()
            if confirmation and ('yes' in confirmation or 'sure' in confirmation):
                speak("Shutting down the system. Goodbye!")
                os.system("shutdown /s /t 1")
            else:
                speak("Shutdown canceled.")

        elif 'open instagram'in query:
            speak("opening Instagram")
            webbrowser.open('https://www.instagram.com/')
        
        else:
            continue