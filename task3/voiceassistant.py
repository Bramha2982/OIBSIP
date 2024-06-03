import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice commands
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-us')
            print(f"You said: {query}\n")
        except Exception as e:
            print("Sorry, I didn't catch that. Can you repeat?")
            return "None"
    return query.lower()

# Function to execute commands
def run_voice_assistant():
    speak("Hello, I am your voice assistant. How can I help you?")
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

        elif 'quit' in query or 'exit' in query:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    run_voice_assistant()
