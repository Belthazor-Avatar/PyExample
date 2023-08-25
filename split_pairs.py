def split_pairs(a):
    first = 0
    second = 1
    letter_pairs = []
    a_list = list(a)
    if a:
        for i in range(0, len(a), 2):
            if second < len(a):
                letter_pairs.append(a_list[first] + a_list[second])
                first += 2
                second += 2
            else:
                letter_pairs.append(a_list[first] + '_')

    return letter_pairs


def split_pairs_other(a):
    return [ch1 + ch2 for ch1, ch2 in zip(a[::2], a[1::2] + '_')]

if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs_other('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
