"""Tic Tac Toe."""


def main() -> None:
    """Main."""
    board = []
    turn = 0
    for i in range(0, 3):
        board.append([' ', ' ', ' '])
    
    print("    1    2    3")
    print(f'A {board[0]}')
    print(f'B {board[1]}')
    print(f'C {board[2]}')
    
    for i in range(0, 9):
        turn += 1
        board = move(board, turn)
        print("    1    2    3")
        print(f'A {board[0]}')
        print(f'B {board[1]}')
        print(f'C {board[2]}')
        win_cond(board)


def move(board: list[list], turn: int) -> list[list]:
    """Makes a move."""
    space: dict = {"A": 0, "B": 1, "C": 2}
    str_pos: str = input("What space would you like to move to? ")

    if str_pos[0] not in space:
        str_pos = input("Try Again. ")
    elif str_pos[1] not in ['1', '2', '3']:
        str_pos = input("Try Again. ")
    
    row: int = space[str_pos[0]]
    col: int = int(str_pos[1]) - 1

    while board[row][col] != ' ':
        str_pos = input("That is an incorrect move! Try Again. ")
        row = space[str_pos[0]]
        col = int(str_pos[1]) - 1
    
    if turn % 2 == 1:
        board[row][col] = 'X'
    else:
        board[row][col] = 'O'
    
    return board


def win_cond(board: list[list]) -> None:
    """Checks if win condition is meet."""
    mark_x: int = 0
    mark_o: int = 0

    # Checks win condition

    for i in range(0, len(board)):

        # Checks columns |
        for j in range(0, len(board[0])):
            if board[i][j] == 'X':
                mark_x += 1
            elif board[i][j] == 'O':
                mark_o += 1
        
        win(mark_x, mark_o)
        mark_x = 0
        mark_o = 0

        # Checks rows ---
        for j in range(0, len(board[0])):
            if board[j][i] == 'X':
                mark_x += 1
            elif board[j][i] == 'O':
                mark_o += 1
            
        win(mark_x, mark_o)
        mark_x = 0
        mark_o = 0
    
    # Checks left right diagonal \
    for i in range(0, len(board)):
        if board[i][i] == 'X':
            mark_x += 1
        elif board[i][i] == 'O':
            mark_o += 1

    win(mark_x, mark_o)
    mark_x = 0
    mark_o = 0

    # Checks right left diagonal /
    for i in range(0, len(board)):
        if board[i][2 - i] == 'X':
            mark_x += 1
        elif board[i][2 - i] == 'O':
            mark_o += 1
    
    win(mark_x, mark_o)


def win(mark_x: int, mark_o: int) -> None:
    """Prints win statement and returns win condition."""
    if mark_x == 3:
        print("X wins!")
        exit()
    elif mark_o == 3:
        print("O wins!")
        exit()


if __name__ == '__main__':
    main()