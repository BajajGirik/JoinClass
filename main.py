import webbrowser
import pyautogui
import time

#Taking the meeting code from the user
url = "https://meet.google.com/"
url += input("Enter the meeting code: ")

#Enter 0 to use default (the first account)
#Enter 1 to use the next account...and so on
msg = "Enter the account from which you would like to enter\n"
example = "Enter 0 to use default(First account)\nEnter 1 to use the next one...and so on\n"

acc = input(msg+example)
url += f'?authuser={acc}'

browser = webbrowser.open(url)

time.sleep(3)

#Opening console on browser
pyautogui.press('f12')
time.sleep(2)

#Pressing tab to focus the curson on console. If you are in brave comment out the below line
pyautogui.press('tab')

#To write javascript on console
#Storing the mic button and video button in variable x
pyautogui.write('let x=document.querySelectorAll(".U26fgb")',interval = 0.015)
pyautogui.press('enter')

#Clicking the mic button
pyautogui.write('x[0].click()',interval = 0.015)
pyautogui.press('enter')

#Clicking the video button
pyautogui.write('x[1].click()',interval = 0.015)
pyautogui.press('enter')

#Clicking the join now button
pyautogui.write('document.querySelector(".uArJ5e").click()',interval = 0.02)
pyautogui.press('enter')

#To remove console from screen
pyautogui.press('f12')