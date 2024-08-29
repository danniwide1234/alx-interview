#!/usr/bin/python3
import sys

def print_usage_and_exit(message):
    """Prints an error message and exits the program with status 1."""
    print(message)
    sys.exit(1)

def is_safe(board, row, col):
    """Checks if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col, solutions):
    """Recursively attempts to place queens on the board."""
    if col == len(board):
        solutions.append([[i, board[i].index(1)] for i in range(len(board))])
        return
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, col + 1, solutions)
            board[row][col] = 0

def main():
    """Main function to handle input and solve the N Queens problem."""
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")
    
    if N < 4:
        print_usage_and_exit("N must be at least 4")

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
