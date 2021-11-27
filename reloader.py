import pyautogui as pg
import time
import webbrowser as wb
print('hello')
url= "https://github.com/kdpandey09"
wb.open(url)
time.sleep(5)
for i in range (20):
    time.sleep(4)
    pg.hotkey('ctrl', 'r')