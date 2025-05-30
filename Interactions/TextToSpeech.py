import pygame
import asyncio
import edge_tts
import os
from dotenv import dotenv_values
 
env_vars = dotenv_values(".env")
AstVoice = env_vars.get("MarkedVoice")

audio_file_path = r"Data\speech.mp3"

async def TextToAudioFile(text) -> None:
    
    if os.path.exists(audio_file_path):
        os.remove(audio_file_path)
        
    communicate = edge_tts.Communicate(text, AstVoice, pitch="+5Hz", rate="+13%")
    await communicate.save(audio_file_path)
    
def TTS(Text, func=lambda r=None: True):
    while True:
        try:
            asyncio.run(TextToAudioFile(Text))
            
            pygame.mixer.init()
            pygame.mixer.music.load(audio_file_path)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                if func() == False:
                    break
                pygame.time.Clock().tick(10)
            
            return True
        
        except Exception as e:
            print(f"Error in TTS: {e}")  
            
        finally:
            try:
                func(False)
                pygame.mixer.music.stop()
                pygame.mixer.quit()
            
            except Exception as e:
                print(f"Error in final block: {e}")

def TextToSpeech(Text, func = lambda r = None: True):
    Data = str(Text).split(".")
    
    responses = "The rest of the result has been printed to the chat screen, kindly check it out."
    
    if len(Data) > 4 and len(Text) >= 250:
        TTS(" ".join(Text.split(".")[0:2]) + ". " + responses, func)
        
    else:
        TTS(Text, func)
        
if __name__ == "__main__":
    while True:
        TextToSpeech(input("Enter the text: "))
        