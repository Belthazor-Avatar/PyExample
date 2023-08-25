import re
def end_zeros(a: int) -> int:
    zeros = re.search("0*$", str(a))
    return len(zeros.group())


print('Example:')
print(end_zeros(10))

assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")