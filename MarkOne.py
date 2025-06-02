# MY IMPORTS
from Interactions.TextToSpeech import TTS
from Interactions.SpeechToText import STT
import RealTimeStatus
import query_library
from Authentications.FaceRecognition import FaceRecognition
from QueryModifier import QueryModification

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
        
        executing_query = QueryModification(command_query)
        
        print(Fore.RESET + ">>> ", Fore.YELLOW + executing_query)
        
        if executing_query in query_library.deactivating_command:
            print("Deactivating...")
            TTS("You can call me anytime.")
            exit()
            
        elif executing_query in query_library.about_mark_one:
            print("About Mark One...")
            TTS("Hello, I am Mark One. A virtual assistant.")
            
        elif "time" in executing_query:
            print("Telling time...")
            TTS(RealTimeStatus.getTime())
        
        elif "power status" in executing_query:
            power_status = RealTimeStatus.BatteryStatus().getBatteryStatus()
            TTS(power_status)
            
        
if __name__ == "__main__":
    # PART OF AUTHENTICATION
    # activate = FaceRecognition().run_recognition()
    activate = True
    
    if activate:
        print(Fore.GREEN + "Initializing...")
        
        GreetMe()
        initialize_MarkOne()
        
    else:
        exit()