import pyautogui as pt
from time import sleep
import pyperclip
import random


sleep(3)
position1 = pt.locateOnScreen("D:/python/Projects/bot/WhatsApp/smily.png", confidence=.6)
x = position1[0]
y = position1[1]

# gets message


def get_message():
    global x, y, position1
    # position = pt.locateOnScreen("D:/python/Projects/WhatsApp/Green dot.png", confidence=.7)
    # x = position[0]
    # y = position[1]
    # pt.moveTo(x, y)
    # pt.click()
    position1 = pt.locateOnScreen("D:/python/Projects/bot/WhatsApp/smily.png", confidence=.7)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 70, y - 50)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message Recieved : " + whatsapp_message)
    return whatsapp_message

# posts message


def post_message(message):
    global x, y, position1
    position1 = pt.locateOnScreen("D:/python/Projects/bot/WhatsApp/smily.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 200, y + 20)
    pt.click()
    pt.typewrite(message)
    pt.typewrite("\n")

# responding message


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

# checking for new message


def check_for_new_messages():
    pt.moveTo(x + 50, y - 40)

    while True:
        try:
            position = pt.locateOnScreen("D:/python/Projects/bot/WhatsApp/Green dot.png", confidence=.8)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()

        except():
            print("No new user message is found")
        if pt.pixelMatchesColor(int(x + 50), int(y - 40), (255, 255, 255), tolerance=10):
            print("is_white")
            process_message = process_response(get_message())
            post_message(process_message)
        sleep(2)


check_for_new_messages()
