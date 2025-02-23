import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random

# Initialize the speech engine
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to wish the user
def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. How can I assist you today?")

# Function to take command input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand. Can you please repeat?")
        return None
    except sr.RequestError:
        speak("Sorry, the service is down.")
        return None

# Function to perform tasks based on the command
def perform_task(command):
    if "wikipedia" in command:
        speak("Searching Wikipedia...")
        command = command.replace("wikipedia", "")
        result = wikipedia.summary(command, sentences=2)
        speak(result)

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "play music" in command:
        music_dir = "C:\\Users\\YourUsername\\Music"  # Replace with your music folder path
        songs = os.listdir(music_dir)
        song = random.choice(songs)
        os.startfile(os.path.join(music_dir, song))
        speak("Playing music...")

    elif "the time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {time}")

    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a nice day.")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")

# Main program
if __name__ == "__main__":
    wish_user()
    while True:
        command = take_command()
        if command:
            perform_task(command)
