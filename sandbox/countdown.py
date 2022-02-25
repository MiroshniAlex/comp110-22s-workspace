"""Mimicking the Gameshow Countdown."""

from random import randint


def main() -> None:
    """The main function."""
    mode: int = gamemode()
    if mode == 1:
        math_game()
    elif mode == 2:
        letters_game()


def gamemode() -> int:
    """What mode do you want to play."""
    mode: int = int(input("Would you like to play the math game or letters game. \n Type 1 for the math game and 2 for the letters game: "))
    while mode != 1 and mode != 2:
        mode = int(input("You must type either 1 for math or 2 for letters. \n Try again. "))
    return mode


def math_game() -> list[int]:
    """Chooses random small and large numbers."""
    # Initializing variables

    print("Hi, you can choose a combination of 6 large and small numbers. \n How many small numbers and large numbers would you like?")
    small: int = int(input("Small Numbers: "))
    large: int = int(input("Large Numbers: "))
    nums_list: list[int] = []
    large_nums: list[int] = [25, 50, 75, 100]
    rand_idx: int
    valid: bool = False

    # Checks the validity of the inputs

    while valid is False:
        if small < 2:
            print("The amount of small numbers must be more than 2.")
            small = int(input("Try Again. Small Numbers: "))

        elif small > 6:
            print("The amount of small numbers must be less than 6.")
            small = int(input("Try Again. Small Numbers: "))
        
        elif large < 0:
            print("The amount of large numbers cannot be negative.")
            large = int(input("Try Again. Large Numbers: "))

        elif large > 4:
            print("You can choose a maximum of 4 large numbers.")
            large = int(input("Try Again. Large Numbers: "))

        elif small + large != 6:
            print("You need a total of 6 numbers.")
            small = int(input("Try Again. Small Numbers: "))
            large = int(input("Large Numbers: "))
        
        else:
            valid = True
    
    # Choosing the numbers

    for n in range(0, small):
        nums_list.append(randint(1, 10))

    for n in range(0, large):
        rand_idx = randint(0, 3 - n)
        nums_list.append(large_nums[rand_idx])
        large_nums.pop(rand_idx)
    
    # Shows the numbers

    print(nums_list)

    print(f"You have 30 seconds to get to {randint(100, 999)}. Good luck!!")

    return nums_list


def letters_game() -> list[str]:
    """The letters game."""
    # Variable Initialization

    letter_list: list[str] = []
    consonants: list[str] = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vowels: list[str] = ['a', 'e', 'i', 'o', 'u']
    letter_amount: int = 9
    player_choice: str
    rand_idx: int

    # Asks player for consonant or vowel and chooses one randomly

    for n in range(0, letter_amount):
        player_choice = input("Would you like a consonant (c) or a vowel (v)? ")
        while player_choice not in ['c', 'v', 'consonant', 'vowel']:
            player_choice = input("That is an invalid input. Try Again. \n Would you like a consonant (c) or a vowel (v)? ")
        print(player_choice)
        if player_choice in ["c", "consonant"]:
            rand_idx = randint(0, 20)
            letter_list.append(consonants[rand_idx])
            print(f"Your consonant is {consonants[rand_idx]}")
        elif player_choice in ["v", "vowel"]:
            rand_idx = randint(0, 4)
            letter_list.append(vowels[rand_idx])
            print(f"Your vowel is {vowels[rand_idx]}")

    # prints the letters
    letter_str: str = ''.join(map(str, letter_list))
    print(letter_list)
    print(letter_str)

    return letter_list        


if __name__ == "__main__":
    main()