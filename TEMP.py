import pyautogui
import AppOpener

txt = input(": ")
AppOpener.open("Notepad", match_closest=True, throw_error=True)
pyautogui.write(txt)