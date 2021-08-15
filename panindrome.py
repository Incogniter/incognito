#palindrome
def palindrome_string(string):
    backward = string[: : -1].casefold()
    return backward== string.casefold()
#word = input("enter the string to be checked:")
#if palindrome_string(word):
#    print("{} is a palindrome".format(word))
#else:
#    print("{} is not a palindrome".format(word))
def palindrome_sentence(sentence):
    string= ""   
    for char in sentence:
        #The isalnum() method returns True if all the characters are alphanumeric,/n
        # meaning alphabet letter(a - z) and numbers(0 - 9).
        #Example of characters that are not alphanumeric: (space)!  # %&? etc
        if char.isalnum():
            string += char
    #backward = string[: : -1].casefold()
    #return backward== string.casefold()
    return palindrome_string(string)


word = input("enter the sentence to be checked:")
if palindrome_sentence(word):
    print("{} is a palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))