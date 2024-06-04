from multiprocessing.spawn import _main
import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime


# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak out the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main function to listen for commands and respond
def main():

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Use Google's speech recognition to convert audio to text
        command = recognizer.recognize_google(audio)

        print("You said: " + command)
        
        # Simple commands to demonstrate functionality
        if "hello" in command:
            speak("Hello! How can I help you?")
        elif "what is your name" in command:
            speak("I am a voice assistant built with Python.")
        elif "open Google" in command:
            webbrowser.open("https://www.google.com")
        elif "open sign up LinkedIn page" in command:
            webbrowser.open("https://www.google.com/search?q=linkedin")
        elif "time" in command:
            # Get the current time
            current_time = datetime.now().strftime("%H:%M:%S")
            print("Current time is:", current_time)
            engine.say("The current time is " + current_time)
            engine.runAndWait()
        else:
            speak("Sorry, I didn't understand that command.")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    


if __name__ == "__main__":
    while True:
        main()
