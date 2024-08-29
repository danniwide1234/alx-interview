#!/usr/bin/python3
import sys

def print_usage_and_exit(message):
    """Prints an error message and exits the program with status 1."""
    print(message)
    sys.exit(1)

def solve_nqueens(N):
    """Uses backtracking to solve the N Queens problem and print solutions."""
    solutions = []
    queens = [-1] * N  # Positions of queens on each row (-1 indicates no queen)
    cols = [False] * N  # Track columns that are under attack
    diag1 = [False] * (2 * N - 1)  # Track left diagonals (/)
    diag2 = [False] * (2 * N - 1)  # Track right diagonals (\)

    def backtrack(row):
        if row == N:
            solutions.append([[i, queens[i]] for i in range(N)])
            return
        for col in range(N):
            if not cols[col] and not diag1[row - col + N - 1] and not diag2[row + col]:
                # Place the queen
                queens[row] = col
                cols[col] = diag1[row - col + N - 1] = diag2[row + col] = True
                backtrack(row + 1)
                # Remove the queen
                queens[row] = -1
                cols[col] = diag1[row - col + N - 1] = diag2[row + col] = False

    backtrack(0)
    return solutions

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

    solutions = solve_nqueens(N)
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
