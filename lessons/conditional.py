"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1 and 5. What is it?")
guess: int = int(input("What is your guess? "))

if guess == 3:
    print("Correct!")
else:
    print("WRONG!")

print("Game Over.")