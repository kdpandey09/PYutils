from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,random
between_messages = 2000
browser = webdriver.Chrome('chromedriver')
def auth(username,password):
    try:
        browser.get('https://www.instagram.com/accounts/login/?next=/direct/inbox/')
        time.sleep(10)
        input_username = browser.find_element_by_name('username')
        input_password = browser.find_element_by_name('password')

        input_username.send_keys(username)
        time.sleep(3)
        input_password.send_keys(password)
        time.sleep(2)
        input_password.send_keys(Keys.ENTER)

    except Exception as err:
        print(err)
        browser.quit()   

def send_message(users,messages):
    try:
       time.sleep(5)
       browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
       time.sleep(5)
       browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
       time.sleep(5)
       browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
       time.sleep(5)
       for user in users:
            time.sleep(3)
            browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
            time.sleep(3)
            browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]').find_element_by_tag_name('button').click()
       browser.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[3]/div/button/div').click()
       time.sleep(5)
       browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(messages)
       time.sleep(3)
       browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

    except Exception as err:
        print(err)
        browser.quit() 
password = '' # write your login password here
username = '' # write your login username here
users = ['subin_sk','um5ng','_himanisoni_','mitalilohar_']
auth(username,password)
send_message(users,'working')