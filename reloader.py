import pyautogui as pg
import time
import webbrowser as wb
# user input
url= str(input("Enter the link of the site you want to reload \n"))
number = int(input("Enter how many times you want it to reload \n"))
# opening the website via your default browser
wb.open(url)
time.sleep(5)
# loop for multiple reloding 
for i in range (number):
    time.sleep(4)
    pg.hotkey('ctrl', 'r')