def backward_string(val: str) -> str:
    return str(val [::-1])


print('Example:')
print(backward_string('val'))

assert backward_string('val') == 'lav'
assert backward_string('') == ''
assert backward_string('ohho') == 'ohho'
assert backward_string('123456789') == '987654321'

print("The mission is done! Click 'Check Solution' to earn rewards!")