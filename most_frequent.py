def most_frequent(data: list) -> str:
    letters = {}
    for d in data:
        if d in letters:
            letters.update({d: letters[d] + 1})
        else: letters[d] = 1

    sorted_letters = dict(sorted(letters.items(), key=lambda x: x[1], reverse = True))
    return str(list(sorted_letters)[0])

def most_frequent2(data: list) -> str:
    return max(data, key=data.count)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent2(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent2(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent2(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")
