def checkio(array: list[int]) -> int:
    value = 0
    for i in range(0, len(array), 2):
        value += array[i]

    if array:
        return int(array[-1] * int(value))
    else:
        return 0


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")