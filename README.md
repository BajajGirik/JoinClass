# JoinClass

This is a repository that will automate your joining of classes held on Google Meet.\
This code does not work for Safari. So change your default browser to GoogleChrome.

# Requirements:

1. pip install pyautogui.
2. pip install time.
3. You must be logged in to your google account before using this.

# Explanation:

Firstly, the program will ask you for the google meet code.\
Next up, it will ask you for the account with which you would like to enter.  
You might be having multiple accounts that are logged into your browser.\
To switch the user, my program takes in a parameter and possible values for this parameter can be:

1. Enter 0 for default (using the first account present in your browser).
2. Enter 1 for the next...and so on.

# Fix for brave browser:

If you are using brave browser, then comment out line 26.\
Also when you launch up brave browser, it continues from where you left off and due to that feature my program bugs out sometimes. If you don't want that to happen, go to settings and change the "on start-up" setting to "Open the new tab page".

<img width="685" alt="Screenshot 2021-05-27 at 12 43 02 PM" src="https://user-images.githubusercontent.com/76426486/119782514-e7c46f80-bee9-11eb-899a-3aa12f91a38d.png">
