# MY IMPORTS
from Interactions.TextToSpeech import TTS
from Interactions.SpeechToText import STT
import RealTimeStatus
import command_list
from Authentications.FaceRecognition import FaceRecognition

# PYTHON IMPORTS
import datetime
from colorama import Fore

def GreetMe():
    hr = int(datetime.datetime.now().hour)

    if hr >= 0 and hr <= 12:
        TTS("Good morning. At your service,sir.")
        
    elif hr > 12 and hr <= 18:
        TTS("Good afternoon. At your service,sir.")
        
    else:
        TTS("Good evening. At your service,sir.")

def initialize_MarkOne():
    while True:
        print(Fore.BLUE + "Listening...")
        command_query = STT()
        command_query = command_query.lower().strip()
        print(Fore.RESET + ">>> ", Fore.YELLOW + command_query)
        
        if command_query in command_list.deactivating_command:
            print("Deactivating...")
            TTS("You can call me anytime.")
            exit()
            
        elif command_query in command_list.about_mark_one:
            print("About Mark One...")
            TTS("Hello, I am Mark One. A virtual assistant.")
            
        elif "time" in command_query:
            print("Telling time...")
            TTS(RealTimeStatus.getTime())
        
        elif "power status" in command_query:
            power_status = RealTimeStatus.BatteryStatus().getBatteryStatus()
            TTS(power_status)
            
        
if __name__ == "__main__":
    # PART OF AUTHENTICATION
    activate = FaceRecognition().run_recognition()
    
    if activate:
        print(Fore.GREEN + "Initializing...")
        
        GreetMe()
        initialize_MarkOne()
        
    else:
        exit()