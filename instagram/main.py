from selenium import webdriver
from time import sleep
import pyautogui as pt
import pyperclip
import random
browser = webdriver.Chrome('D:/python/Projects/bot/instagram/chromedriver.exe')
browser.get('https://www.instagram.com/')
sleep(2)


# auto login
def login():
    username = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/"
                                             "div[1]/div/form/div/div[1]/div/label/input")
    username.send_keys("abinorobilin_")
    sleep(1)
    password = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/"
                                             "div[1]/div/form/div/div[2]/div/label/input")
    password.send_keys("sherylpriscilla@123")
    password.submit()
    sleep(5)


login()


# responding notification
def notification():
    not_now = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
    not_now.click()
    sleep(2)
    notifi = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    notifi.click()
    sleep(2)


notification()


def get_messages():

    # chat = pt.locateOnScreen("D:/python/Projects/bot/instagram/bluedot.png", confidence=.9)
    # x = chat[0]
    # y = chat[1]
    # pt.moveTo(x, y)
    # pt.click()
    # sleep(2)
    position1 = pt.locateOnScreen("D:/python/Projects/bot/instagram/smiley.png", confidence=.9)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 90, y - 80)
    sleep(1)
    option = pt.locateOnScreen("D:/python/Projects/bot/instagram/option.png", confidence=.9)
    pt.moveTo(option[0:4])
    pt.click()
    x = option[0]
    y = option[1]
    pt.moveTo(x + 180, y - 40)
    pt.click()
    message = pyperclip.paste()
    return message


def post_message(message):
    chat_box = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/'
                                             'div[2]/div/div/div[2]/textarea')
    chat_box.click()
    pt.typewrite(message)
    send = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/'
                                         'div/div[2]/div/div/div[3]/button')
    send.click()


def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any questions!"
    else:
        if random_no == 0:
            return "That's cool!"
        elif random_no == 1:
            return "If urgent give me a call!"
        else:
            return "Sorry don't mind testing my code"


def check_for_new_messages():
    mes = browser.find_element_by_class_name('xWeGp')
    mes.click()
    sleep(2)

    while True:

        chat = pt.locateOnScreen("D:/python/Projects/bot/instagram/bluedot.png", confidence=.9)
        if chat is not None:
            pt.moveTo(chat)
            pt.moveRel(-100, 0)
            pt.click()
            sleep(1)
            process_message = process_response(get_messages())
            post_message(process_message)


check_for_new_messages()
