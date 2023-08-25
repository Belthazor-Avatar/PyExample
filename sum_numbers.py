import re
def sum_numbers(text: str) -> int:
    sum = 0
    for m in re.finditer(r"[0-9]+\b", text):
        if m.group().isnumeric():
            sum += int(m.group())
    print("sum:", sum)
    return int(sum)


sum_numbers_other = lambda text: sum(int(word) for word in text.split() if word.isdigit())

if __name__ == "__main__":
    print("Example:")
    print(sum_numbers("hi"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers("2 2 2") == 6
    assert sum_numbers("hi") == 0
    assert sum_numbers("who is 1st here") == 0
    assert sum_numbers("my numbers is 2") == 2
    assert (
            sum_numbers(
                "This picture is an oil on canvas "
                "painting by Danish artist Anna "
                "Petersen between 1845 and 1910 year"
            )
            == 3755
    )
    assert sum_numbers("5 plus 6 is") == 11
    assert sum_numbers("") == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
