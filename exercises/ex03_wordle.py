"""Wordle Function."""

__author__ = "730477260"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(string: str, char: str) -> bool:
    """Searches for character match in string."""
    assert len(char) == 1
    if char in string:
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Returns emoji string of guess."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret)
    emoji: str = ""
    index: int = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            emoji += f"{GREEN_BOX}"
        elif contains_char(secret, guess[index]) is True:
            emoji += f"{YELLOW_BOX}"
        else:
            emoji += f"{WHITE_BOX}"
        index += 1
    return emoji


def input_guess(length: int) -> str:
    """Asks user for a guess of a certain length."""
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            break
        turn += 1
    if turn == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()