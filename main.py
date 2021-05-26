import webbrowser
import pyautogui

#Taking the meeting link from the user
url = input("Enter the meeting link: ")
browser = webbrowser.open(url)