#!/usr/bin/python3


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))

# here force user to use number
try:
#    value = 10 / 0
    number = int(input("Enter a number, not a letter.  Just a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError as err:
    print(err)
#    print("Invalid Input")
'''
This is how to handle control ^C program exit error to cleanly exit
'''
except KeyboardInterrupt:
    print("\nYou hit control^C")
