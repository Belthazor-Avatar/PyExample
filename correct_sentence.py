def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    texts = list(text)
    if texts[0].islower():
        texts[0] = texts[0].upper()
    if texts[-1] != '.':
        texts.append('.')

    text = ''
    for i in texts:
        text += i

    return str(text)


def correct_sentence_other(text: str) -> str:
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")

print('Example:')
print(correct_sentence("greetings, friends"))

assert correct_sentence('greetings, friends') == 'Greetings, friends.'
assert correct_sentence('Greetings, friends') == 'Greetings, friends.'
assert correct_sentence('Greetings, friends.') == 'Greetings, friends.'
assert correct_sentence('greetings, friends.') == 'Greetings, friends.'
assert correct_sentence_other('welcome to New York') == 'Welcome to New York.'

print("The mission is done! Click 'Check Solution' to earn rewards!")