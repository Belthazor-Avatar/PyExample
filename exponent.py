#!/usr/bin/python3


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3, 2))

print("Same as: 3**2")
print(3**2)