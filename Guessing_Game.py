#!/usr/bin/python3

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("What is your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You guessed correctly!")

for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for name in friends:
    print(name)

for index in range(3, 10):
    print(index)

for index in range(5):
    if index == 0:
        print("First time.")
    else:
        print("Everyone after that.")


print("len of friends: ")
for index in range(len(friends)):
    print(index)