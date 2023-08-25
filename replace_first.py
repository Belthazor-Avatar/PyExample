from typing import Iterable


def replace_first(items: list) -> Iterable:
    if items:
        items.append(items.pop(0))
    return items


print('Example:')
print(list(replace_first([1, 2, 3, 4])))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")