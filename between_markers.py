import re


def between_markers(text: str, start: str, end: str) -> str:
    value = ''
    status = False
    for i in list(text):
        if i == start:
            status = True
        elif i == end:
            status = False
            break
        elif status:
            value += i

    return value

def between_markers_other(text: str, start: str, end: str) -> str:
    return text[text.index(start) + 1:text.index(end)]


print('Example:')
print(between_markers('What is >apple<', '>', '<'))

assert between_markers('What is >apple<', '>', '<') == 'apple'
assert between_markers('What is [apple]', '[', ']') == 'apple'
assert between_markers('What is ><', '>', '<') == ''
assert between_markers('[an apple]', '[', ']') == 'an apple'
assert between_markers_other('[an apple]', '[', ']') == 'an apple'

print("The mission is done! Click 'Check Solution' to earn rewards!")