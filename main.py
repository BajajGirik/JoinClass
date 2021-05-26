import webbrowser
import pyautogui
import time

#Taking the meeting link from the user
url = input("Enter the meeting link: ")
browser = webbrowser.open(url)
time.sleep(2.5)

#Opening console on browser
pyautogui.press('f12')
time.sleep(1.5)

#Pressing tab to focus the curson on console
pyautogui.press('tab')

#To write javascript on console
#Storing the mic button and video button in variable x
pyautogui.write('let x = document.querySelectorAll(".U26fgb")')
pyautogui.press('enter')

#Clicking the mic button
pyautogui.write('x[0].click()')
pyautogui.press('enter')

#Clicking the video button
pyautogui.write('x[1].click()')
pyautogui.press('enter')

#Clicking the join now button
pyautogui.write('document.querySelector(".uArJ5e").click()')
pyautogui.press('enter')

#To remove console from screen
pyautogui.press('f12')