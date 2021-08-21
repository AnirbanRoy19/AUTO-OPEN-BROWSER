import time
import webbrowser
import os
url = 'https://i.pinimg.com/originals/66/b5/5f/66b55f8e2ca22a800af0aecf9d01d848.gif'
x = 4
while x < 6:
    x = webbrowser.open(url)
    time.sleep(0.5)
    os.system('taskkill /im chrome.exe /f')
