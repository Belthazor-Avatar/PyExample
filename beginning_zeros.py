import re

def beginning_zeros(a: str) -> int:
    return len(a) - len(a.lstrip('0'))
    #zeros = re.search("^0*", str(a))
    #return len(zeros.group())

print('Example:')
print(beginning_zeros('10'))

assert beginning_zeros('100') == 0
assert beginning_zeros('001') == 2
assert beginning_zeros('100100') == 0
assert beginning_zeros('001001') == 2
assert beginning_zeros('012345679') == 1
assert beginning_zeros('0000') == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")