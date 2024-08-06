import pyttsx3 as p
import speech_recognition as sr
import datetime
import wikipedia
import os
import random
import webbrowser
import pyautogui

engine = p.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon sir")
    elif hour >= 16 and hour < 20:
        speak("Good Evening sir")
    else:
        speak("Good Night sir")
    
    speak("I am Sara, your voice assistant. How are you?")

def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.pause_threshold = 2
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening....")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            speak("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak(f"Could not request results; {e}")
            return None

def find_music_files(directory, extensions=('.mp3', '.wav', '.flac', '.aac', '.m4a')):
    music_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extensions):
                music_files.append(os.path.join(root, file))
    return music_files

if __name__ == "__main__":
    wishMe()
    user_response = get_voice_input()
    if user_response:
        if "good" in user_response.lower() or "fine" in user_response.lower():
            speak("I am also doing good. How can I help you?")
        elif "bad" in user_response.lower():
            speak("Sorry for asking sir. How can I help you?")

    while True:
        query = get_voice_input()
        if query:
            query = query.lower()
            if "wikipedia" in query:
                speak("What do you want to search on Wikipedia?")
                search_query = get_voice_input()
                if search_query:
                    speak(f"Searching Wikipedia for {search_query}")
                    results = wikipedia.summary(search_query, sentences=2)
                    speak("According to Wikipedia")
                    speak(results)
            elif 'play some music' in query:
                speak("Searching for music files...")
                music_dir = r'C:\Users\pavan kalyan\Music\New folder' 
                music_files = find_music_files(music_dir)
                if music_files:
                    song = random.choice(music_files)
                    speak(f"Playing {os.path.basename(song)}")
                    os.startfile(song)
                else:
                    speak("No music files found in the specified directory.")
            elif 'open chrome' in query:
                speak("Opening Chrome")
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  
                os.startfile(chrome_path)
            elif 'i have a query' in query:
                speak("What is your query?")
                search_query = get_voice_input()
                if search_query:
                    speak(f"Searching Chrome for {search_query}")
                    webbrowser.open(f"https://www.google.com/search?q={search_query.replace(' ', '+')}")
            elif 'open youtube' in query:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
            elif 'search youtube' in query:
                speak("What do you want to search on YouTube?")
                search_query = get_voice_input()
                if search_query:
                    speak(f"Searching YouTube for {search_query}")
                    webbrowser.open(f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}")
            elif 'open gmail' in query:
                speak("Opening Gmail")
                webbrowser.open("https://mail.google.com")
            elif 'play spotify' in query:
                speak("What song do you want to play on Spotify?")
                search_query = get_voice_input()
                if search_query:
                    speak(f"Searching Spotify for {search_query}")
                    webbrowser.open(f"https://open.spotify.com/search/{search_query.replace(' ', '%20')}")
            elif 'go to home page' in query:
                speak("Going to the home page")
                webbrowser.open("https://www.google.com")
            elif 'go back to home screen' in query:
                speak("Going back to the home screen")
                pyautogui.hotkey('win', 'd')
            elif 'stop' in query or 'exit' in query:
                speak("Goodbye sir, have a nice day!")
                break
