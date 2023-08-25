import re

def checkio(words: str) -> bool:
    return bool(re.search("[a-zA-Z]+\s[a-zA-Z]+\s[a-zA-Z]+", words))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True
    assert checkio("Hello World hello") == True
    assert checkio("He is 123 man") == False
    assert checkio("1 2 3 4") == False
    assert checkio("bla bla bla bla") == True
    assert checkio("Hi") == False
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")