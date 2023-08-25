#arr = [5, 1, 2, 3, 4, 5]
arr = [2, 3, 1]
k = 5

def findNumber(k, arr):
    y = False
    for item in arr:
        if k == item:
            y = True
            print('YES')
            exit(0)

    if y == False:
        print('NO')


findNumber(k, arr)