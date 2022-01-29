"""One Shot Wordle."""

__author__ = "730477260"

# initialization of variable
secret_word: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji_hint: str = ""
guess_index: int = 0
secret_word_index: int = 0
player_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

# checks format of guess
while len(player_guess) != len(secret_word):
    player_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

# begins checking guess for correct letters
while guess_index < len(secret_word):
    secret_word_index = 0
    incorrect_pos: bool = False
    if player_guess[guess_index] == secret_word[guess_index]:
        emoji_hint += f"{GREEN_BOX}"
    else:
        # This while loop checks if the secret letter in the currect guess index position matches any other letters in the guess
        while secret_word_index < len(secret_word):
            if player_guess[guess_index] == secret_word[secret_word_index]:
                incorrect_pos = True
            secret_word_index += 1
        if incorrect_pos is True:
            emoji_hint += f"{YELLOW_BOX}" 
        else:
            emoji_hint += f"{WHITE_BOX}"
    guess_index += 1

print(emoji_hint)

if player_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")