"""Following the tutorial for tictactoe."""

CHARS: list[str] = ['   ', ' X ', ' O ']
BOARD: list[list[str]] = [
    [CHARS[0], CHARS[0], CHARS[0]],
    [CHARS[0], CHARS[0], CHARS[0]],
    [CHARS[0], CHARS[0], CHARS[0]]
]


def main() -> None:
    """Main."""
    tictactoe()


def tictactoe() -> None:
    """Something."""
    turn: int = 0
    player: str
    i: int
    j: int
    valid_inputs: list[str] = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    displayTTT()
    while True:
        turn += 1
        player = 'O' if turn % 2 == 0 else 'X'

        # Player Input Spot

        player_input = input("Enter a row (0, 1, or 2) and column (0, 1, or 2), no space, for player " + player + ": ")
        
        # Checks valitidy of input
        
        while player_input not in valid_inputs:
            player_input = input("Invalid input. Try Again:")
        
        i = int(player_input[0])
        j = int(player_input[1])

        if BOARD[i][j] != CHARS[0]:
            player_input = input("There is already someone there! Try Again:")
            i = int(player_input[0])
            j = int(player_input[1])

        # Updates the board

        if player == 'X':
            BOARD[i][j] = CHARS[1]
        elif player == 'O':
            BOARD[i][j] = CHARS[2]
        
        displayTTT()

        if check_win():
            break


def check_win() -> bool:
    """Checks the win condition of the board: 0 = continue playing, 1 = someone won, 2 = draw."""
    mark_x: int = 0
    mark_o: int = 0

    # Checks win condition

    for i in range(0, 3):

        # Checks columns |
        for j in range(0, 3):
            if BOARD[i][j] == CHARS[1]:
                mark_x += 1
            elif BOARD[i][j] == CHARS[2]:
                mark_o += 1
        
        if win(mark_x, mark_o) is True:
            return True
        mark_x = 0
        mark_o = 0

        # Checks rows ---
        for j in range(0, 3):
            if BOARD[j][i] == CHARS[1]:
                mark_x += 1
            elif BOARD[j][i] == CHARS[2]:
                mark_o += 1
            
        if win(mark_x, mark_o) is True:
            return True
        mark_x = 0
        mark_o = 0
    
    # Checks left right diagonal \
    for i in range(0, 3):
        if BOARD[i][i] == CHARS[1]:
            mark_x += 1
        elif BOARD[i][i] == CHARS[2]:
            mark_o += 1

    if win(mark_x, mark_o) is True:
        return True
    mark_x = 0
    mark_o = 0

    # Checks right left diagonal /
    for i in range(0, 3):
        if BOARD[i][2 - i] == CHARS[1]:
            mark_x += 1
        elif BOARD[i][2 - i] == CHARS[2]:
            mark_o += 1
    
    if win(mark_x, mark_o) is True:
        return True

    # Checks if all spaces are filled.
    fill: int = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if BOARD[i][j] != CHARS[0]:
                fill += 1
    
    if fill == 9:
        print("It's a tie!")
        return True

    return False


def win(mark_x: int, mark_o: int) -> bool:
    """Prints win statement and returns win condition."""
    if mark_x == 3:
        print("X wins!")
        return True
    elif mark_o == 3:
        print("O wins!")
        return True
    else: 
        return False


def displayTTT() -> None:
    """Displays the Board."""
    print("-------------")
    for i in range(0, 3):
        print(f'|{BOARD[i][0]}|{BOARD[i][1]}|{BOARD[i][2]}|')
        print("-------------")


if __name__ == '__main__':
    main()