import webbrowser
from time import sleep

url = "https://www.google.com/"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Google\Chrome\Application\chrome.exe"))

while True:
    print("refreshing...")
    webbrowser.open(url)
    sleep(5)

"""
1) Important note: -
2) In sleep parameter you can put any number, the number denotes the delay it will take to open the site again, like eg. it is given 5 so site will be reopened in every 5 seconds.
3) You can put any url u want to put after url = " "
4) You need to provide the path of your browser from the C drive or any drive your browser exe is available
5) This code supports all browser's exe file if the browser's exe path is given correctly
6) The Given path is just an example.
7) You need to have python idle in order to run the program (IDLE VERSION - 3.8 and Above only).
"""
