#!/usr/bin/python3

import useful_tools
from Student import Student
from Question import Question

# How to import and use a self made module
print(useful_tools.roll_dice(10))

student1 = Student("Jim", "Business", 3.1, True)
student2 = Student("Pam", "Art", 3.5, False)

print("student1")
print(student1.name)
print(student1.gpa)

print("student2")
print(student2.name)
print(student2.gpa)

question_prompts = [
    "What color are apples\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)

print('{} {}'.format(student1.major, student1.name))