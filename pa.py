    







import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time

#function to make assistant speak
def speak(text):
    engine=pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5)
#function to take a voice command from the user
def take_command():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Kelkkunnund Ettaaaa")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Thiriynnind thiriynnind")
            command=recognizer.recognize_google(audio)
            print(f"user said:{command}")
        except sr.UnknownValueError:
            print("Anakk thirinjittillaaaaa")
            return None
        except sr.RequestError:
            print("Net onnum kittnnillaaa ettaa")
            return None
    return command.lower()
            


        
    #Function to respond to different commands
def respond(command):
    if 'hello' in command or 'hi' in command:
        speak("Hello!Ettaaaa,ningakk enna bende")
    elif 'time' in command:
        current_time=datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Ippo samayam{current_time}")
    elif 'search' in command:
        speak("Enna ninkk search cheyyande?")
        search_query=take_command()
        if search_query:
            speak(f"searching for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif 'open' in command:
        if 'safari' in command:
            speak("Safari thorakkalaanne")
            os.system("Open -a safari")
    elif 'calculator'in command:
        speak(" calculator thorakkalaanne")
        os.system("Opening -a Calculator")
    elif 'bye' in command or 'exit' in command or 'quit' in command:
        speak("Sheriyenna njn pokkay")
        exit()
    else:
        speak("sorriyee ath anakkarilla")
        
                
            
            
            
        
        
        
        #main function to run the assistant
def run_assistant():
    speak("Hello,njn ningala assistant,para enna bende?")
    while True:
        command=take_command()
        if command:
            respond(command)
    
    
    #start the assistant
run_assistant()