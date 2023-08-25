import re


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    word = re.match(r'^\w+', text)
    return str(word[0])


def first_word_fastest(text: str) -> str:
    i = 0
    while i < len(text) and text[i] != ' ':
        i += 1
    return text[:i]


print('Example:')
print(first_word("Hello world"))
print(first_word_fastest("Hell Oh world"))

assert first_word('Hello world') == 'Hello'
assert first_word('a word') == 'a'
assert first_word('greeting from CheckiO Planet') == 'greeting'
assert first_word('hi') == 'hi'

print("The mission is done! Click 'Check Solution' to earn rewards!")