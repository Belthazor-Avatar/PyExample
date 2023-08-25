def PrintTriangle():
    lines = []
    b = 34
    for r in range(b):
        l = (b - r)
        s = str(r * ' ')
        left = str(l * str(' ') + '/')
        right = str(r * str(' ') + s + '\\')
        line = str(left + right)
        lines.append(line)

    for line in lines:
        print(line)

    print('/' + (b * 2) * '_' + '\\')


PrintTriangle()