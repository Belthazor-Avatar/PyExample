#!/usr/bin/python3

employee_file = open("employees.txt", "r")

if employee_file.readable():
    print(employee_file.read())
    for employee in employee_file.readlines():
        print("Employee: " + employee)

'''
    print(employee_file.readline())
    array = employee_file.readlines()
'''

employee_file.close()

'''
Read:
open("employees.txt", "r")
Write:
open("employees.txt", "w")
Append:
open("employees.txt", "a")
Read + Write:
open("employees.txt", "r+")
'''

# Append text to bottom of file
employee_file = open("employees.txt", "a")
employee_file.write("Toby Chong - Robot Resources\n")
employee_file.close()
employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()

# Write a new file
print("New file created then read file new file: ")
employee_file_new = open("employees_new.txt", "w")
employee_file_new.write("Tommy Chong - Robot Assassin Resources\n")
employee_file_new.close()
employee_file_new = open("employees_new.txt", "r")
print(employee_file_new.read())
employee_file_new.close()
