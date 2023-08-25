import math as m

def square_power(end):
    end += 1
    for num in range(1, end):
        num_sqrt = m.sqrt(num)
        if num_sqrt != round(num_sqrt):
            print(num)
        else:
            print("POWER")

end = 50
square_power(end)
