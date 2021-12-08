import pyautogui as pg
import time
person = str(input("Enter the name of the person as per your contact \n"))
Message = str(input("what message do you want to send them \n"))
number = int(input("Enter the number of times you want to send the message\n"))
pg.press('win')
time.sleep(3)
pg.write('whatsapp')
pg.press('enter')
pg.moveTo(322 , 187)
time.sleep(10)
pg.click()
time.sleep(3)
pg.write(person)
time.sleep(2)
pg.press('enter')
# makes code work after 2 seconds
time.sleep(2)
for i in range(number):
    time.sleep(1)
    pg.write(Message)
    pg.press('enter')
