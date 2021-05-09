#Using speech_recognition library
import speech_recognition as speech
import pyttsx3


engine=pyttsx3.init()

engine.setProperty("RATE",100)
                  
engine.say("Hello there sir, I am JARVIS, your personal assistant. I am made to make your life easier.")
engine.say("I can do many things such as tell you the time, weather and I can open websites for you!")
engine.say("You can say, JARVIS wake up to activate me.")


engine.runAndWait()


while True:
    try:
        #Take the user input to activate reception of Voice Commands
        userInput=input("Press v to start voice commands and q to quit: ")
        
        if userInput=='v':
            
            #Take Voice commands from mic
            r=speech.Recognizer()
            with speech.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Speak:")
                audio=r.listen(source)
            #Convert Voice Commands to Text
            command=r.recognize_google(audio)
            
            print("You said: "+command)
        else:
            break
   
    #Statements to Handle errors while receiving voice commands
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
print("Nice interacting with you!!")

