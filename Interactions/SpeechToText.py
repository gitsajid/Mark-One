import speech_recognition as sr
from colorama import Fore

recognizer = sr.Recognizer()

def STT():
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source=source, duration=0.2)
                audio = recognizer.listen(source=source)
                MyText = recognizer.recognize_google(audio)
                
                return MyText
            
        except sr.RequestError as e:
            print(e)
            
        except sr.UnknownValueError:
            print(Fore.RED + "Can't hear...")
            
if __name__ == "__main__":
    while True:
        text = STT()
        print(Fore.GREEN + ">>> ", text)
        
        if text == "exit":
            exit()