import pyautogui as pg
import time
person = str(input("Enter the name of the person as per your contact \n"))
Message = str(input("what message do you want to send them \n"))
pg.press('win')
time.sleep(3)
pg.write('whatsapp')
pg.press('enter')
pg.moveTo(322 , 187)
time.sleep(20)
pg.click()
time.sleep(3)
pg.write(person)
time.sleep(2)
pg.press('enter')
time.sleep(2)
pg.write(Message)
pg.press('enter')
