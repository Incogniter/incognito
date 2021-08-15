def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("EEK!!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(" ")
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")

print("_" * 50)


# handling invalid arguments
# handling errors
# value error
def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        raise ValueError("string {} is lager than the screen_width{}".format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(" ")
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")

print("=" * 30)


# tried one
def banner_text(text: str = " ",screen_width:int = 25) -> None: #annotations
    if len(text) > screen_width - 4:
        print("Your text is longer than the screen width")
    if text == "*":
        print("*" * screen_width)
    else:
        centerted = text.center(screen_width - 4)
        outputString = "**{}**".format(centerted)
        print(outputString)
        print(banner_text.__doc__)


banner_text("*")
banner_text("love you soo much")
banner_text("Sheryl Priscilla")
banner_text("*")
