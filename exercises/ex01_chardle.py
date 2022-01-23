"""Exercise 2 Wordle Mimic."""

__author__ = "730477260"

user_word: str = input("Enter a 5-character word: ")
user_letter: str = input("Enter a single character: ")

# checks
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

if len(user_letter) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + user_letter + " in " + user_word)

occurances: int = 0

for n in range(0, 4):
    if user_letter == user_word[n]:
        print(user_letter + " found at index " + str(n))
        occurances = occurances + 1

if occurances > 0:
    print(str(occurances) + " instances of " + user_letter + " found in " + user_word)
else:
    print("No instances of " + user_letter + " found in " + user_word)