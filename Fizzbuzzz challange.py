def fizz_buzz(number: int) -> str:
    """
    Play Fizz buzz

    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


input("Play Fizz Buzz.   Press ENTER to start")
print()

next_number = 0
while next_number < 50:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_number = fizz_buzz(next_number)
    players_answer = input("your go ")
    if players_answer != correct_number:
        print("Sorry you are wrong!", correct_number)
        break
else:
    print("well,you are done now {}".format(next_number))
