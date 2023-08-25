# !/usr/bin/python

friends = ["Kevin", "Karen", "Jim", "Jack", "Qwack"]
lucky_numbers = [7, 4, 2, 69, 42]

print(friends)
coordinates = (4, 7)
print(coordinates[0])
print(lucky_numbers[-2:])


# Happy Feet subroutine
def happy_feet(user, happy_status):
    if happy_status == "yes":
        return_value = ("I am happy that you are happy " + user)
    elif happy_status == "no":
         return_value = ("I feel bad that you are not happy " + user)
    else:
        return_value = "What you talkin about Willis?"

    return return_value


user_input = input("What is your name?: ")
happy_status_input = input("Are your feet happy?: ")
message = (happy_feet(user_input, happy_status_input.lower()))
print(message)

'''
This is a comment
'''
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print("Largest number: " + str(max_num(22, 999, 2)))

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")


