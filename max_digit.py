#def max_digit(a: int) -> int:
    #m = sorted([i for i in str(a)], reverse=True)
    #return int(m[0])


max_digit = lambda number: int(max(str(number)))

print('Example:')
print(max_digit(10))

assert max_digit(10) == 1
assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(10000) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")