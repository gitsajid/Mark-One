import pyautogui
from Interactions.SpeechToText import STT

win_shortcuts = {
    
    # activated by WINDOWS + " "
    
    "toogle tab": lambda: pyautogui.hotkey("alt", "tab"),
    "close active window": lambda: pyautogui.hotkey("alt", "f4"),
    "screenshot": lambda: pyautogui.hotkey("win", "printscreen"),
    "next tab": lambda: pyautogui.hotkey("ctrl", "tab"),
    "previous tab": lambda: pyautogui.hotkey("ctrl", "shift", "tab"),
    "new tab": lambda: pyautogui.hotkey("ctrl", "t"),
    "close tab": lambda: pyautogui.hotkey("ctrl", "w")
}

key_map = {
    
    # activated by PRESS + " "
    
    "delete": lambda: pyautogui.press("delete"),
    "backspace": lambda: pyautogui.press("backspace"),
    "enter": lambda: pyautogui.press("enter"),
    "caps lock": lambda: pyautogui.press("capslock"),
    "escape": lambda: pyautogui.press("esc"),
    
    # F keys
    "f1": lambda: pyautogui.press("f1"),
    "f2": lambda: pyautogui.press("f2"),
    "f3": lambda: pyautogui.press("f3"),
    "f4": lambda: pyautogui.press("f4"),
    "f5": lambda: pyautogui.press("f5"),
    "f6": lambda: pyautogui.press("f6"),
    "f7": lambda: pyautogui.press("f7"),
    "f8": lambda: pyautogui.press("f8"),
    "f9": lambda: pyautogui.press("f9"),
    "f10": lambda: pyautogui.press("f10"),
    "f11": lambda: pyautogui.press("f11"),
    "f12": lambda: pyautogui.press("f12"),
    
    "right": lambda: pyautogui.press("right"),
    "left": lambda: pyautogui.press("left"),
    "up": lambda: pyautogui.press("up"),
    "down": lambda: pyautogui.press("down"),
    
    
    # Letters a to z
    "a": lambda: pyautogui.press("a"),
    "b": lambda: pyautogui.press("b"),
    "c": lambda: pyautogui.press("c"),
    "d": lambda: pyautogui.press("d"),
    "e": lambda: pyautogui.press("e"),
    "f": lambda: pyautogui.press("f"),
    "g": lambda: pyautogui.press("g"),
    "h": lambda: pyautogui.press("h"),
    "i": lambda: pyautogui.press("i"),
    "j": lambda: pyautogui.press("j"),
    "k": lambda: pyautogui.press("k"),
    "l": lambda: pyautogui.press("l"),
    "m": lambda: pyautogui.press("m"),
    "n": lambda: pyautogui.press("n"),
    "o": lambda: pyautogui.press("o"),
    "p": lambda: pyautogui.press("p"),
    "q": lambda: pyautogui.press("q"),
    "r": lambda: pyautogui.press("r"),
    "s": lambda: pyautogui.press("s"),
    "t": lambda: pyautogui.press("t"),
    "u": lambda: pyautogui.press("u"),
    "v": lambda: pyautogui.press("v"),
    "w": lambda: pyautogui.press("w"),
    "x": lambda: pyautogui.press("x"),
    "y": lambda: pyautogui.press("y"),
    "z": lambda: pyautogui.press("z")
}

def press_one_by_one(txt):
    txt = txt.lower()
    
    for t in txt:
        pyautogui.press(t)
    
    pyautogui.PAUSE = 1
    
def PressKeyFn(cmd):
    cmd = cmd.replace("press ", "")
    
    if cmd in key_map:
        key_map[cmd]()
        pyautogui.PAUSE = 0.5
    
    else:
        print("Failed to press.")   
        
def pressKey(key):
    if key in key_map:
        key_map[key]()
    
def contTyping():
    typing = True
    
    while typing:
        alphabets = STT()
        list_alphabets = list(alphabets)
        
        if alphabets == "exit" or alphabets == "stop":
            typing = False
        
        else:
            for alphabet in list_alphabets:
                pressKey(alphabet)
                pyautogui.PAUSE = 0.5
                
            typing = False
            
def contWriting():
    writing = True
    
    while writing:
        sentence = STT()
        
        if sentence == "exit" or sentence == "stop":
            writing = False
            
        else:
            pyautogui.write(sentence)
            pyautogui.PAUSE = 0.5