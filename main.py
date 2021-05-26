import webbrowser
import pyautogui
import time

#Taking the meeting link from the user
url = input("Enter the meeting link: ")
browser = webbrowser.open(url)
time.sleep(2)

#Opening console on browser
pyautogui.press('f12')
time.sleep(1)

#Pressing tab to focus the curson on console
pyautogui.press('tab')