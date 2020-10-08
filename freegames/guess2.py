"""Guess a number within a range.

Exercises

1. Change the range to be from 0 to 1,000,000.
2. Can you still guess the number?
3. Print the number of guesses made.
4. Limit the number of guesses to the minimum required.

"""

from random import randint

start = 0
end = 1000000
value = randint(start, end)

print(value)
print("I'm thinking of a number between", start, "and", end)

guess = None
i = 0
while i < 10:
    text = input("Guess the number: ")
    guess = int(text)
    i = 1 + i
    if guess < value:
        print("Higher.")
        if i > 9:
            print("Game over The answer is", value)
            break
    elif guess > value:
        print("Lower.")
        if i > 9:
            print("Game over The answer is", value)
            break
    elif guess == value:
        print("Congratulations! You guessed the right answer:", value)
        break