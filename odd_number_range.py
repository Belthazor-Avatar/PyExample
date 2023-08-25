l = int(input())
r = int(input())
def oddNumbers(l, r):
    r = (r + 1)
    arr = []
    for i in range(l, r):
        if (i % 2) != 0:
            arr.append(i)

    return arr


arr = oddNumbers(l, r)
for item in arr:
    print(item)

