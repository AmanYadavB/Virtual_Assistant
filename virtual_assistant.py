import pyttsx3
import speech_recognition as sr
import webbrowser
import yfinance as yf
#import pywhatkit
import pyjokes
import datetime
import wikipedia

# id's of voices
id1='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
id2='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# hear the mic and return the audio as text
def transform_audio_into_text():
    # store recognizer in a variable
    r = sr.Recognizer()

    # set microphone
    with sr.Microphone() as source:

        #waiting time
        sr.pause_threshold = 0.8

        print("You can now speak")

        # save what you hear
        audio = r.listen(source)

        try:
            # search on google
            request = r.recognize_google(audio, language="en-us")

            # test in text
            print("You said: " + request)

            return request
        # in case it didnt understand
        except sr.UnknownValueError:
            #show proof
            speak("OOps! I didnt understand what you said")

            # return error
            return "I'm still waiting"
        
        except sr.RequestError:
            #show proof
            speak("OOps! there is no service")

            # return error
            return "I'm still waiting"
        
        except:
            
            #show proof
            speak("OOps! something went wrong")

            # return error
            return "I'm still waiting"

def speak(message):
    # start the engine
    engine = pyttsx3.init()
    engine.setProperty('voice', id2)
    engine.say(message)
    engine.runAndWait()
#transform_audio_into_text()

def ask_day():
    day = datetime.datetime.today()

    week_day = day.weekday()

    calander = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    speak("Today is " + calander[week_day])

def ask_time():

    time = datetime.datetime.now()
    print(time.hour)
    speak(f'Hello Aman!, The time is, {time.hour} hours and {time.minute} minutes')

def initial_greeting():
    speak("Hi, I am Zara, How may i assist you today")

def my_assistant():

    initial_greeting()

    go_on = True

    # main_loop
    while go_on:

        my_request = transform_audio_into_text().lower()

        if 'open youtube' in my_request:
            speak("Sure, I am opening youtube")
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'play a random song' in my_request:
            speak("Sure, playing it right away")
            webbrowser.open('https://www.youtube.com/watch?v=JK_3gYHNoSw&list=RDJK_3gYHNoSw&start_radio=1')
        elif 'open browser' in my_request:
            speak("Sure, I'm on it")
            webbrowser.open('https://www.google.com')
            continue
        elif 'what day is today' in my_request:
            ask_day()
            continue
        elif 'what time it is' in my_request:
            ask_time()
            continue
        elif 'do a wikipedia search for' in my_request:
            speak('Please wait, I am looking for it')
            my_request = my_request.replace('do a wikipedia search for', '')
            answer = wikipedia.summary(my_request, sentences=4)
            speak('According to wikipedia: ')
            speak(answer)

my_assistant()

