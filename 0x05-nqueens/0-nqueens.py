#!/usr/bin/env python3
import sys

"""
This module solves the N queens problem, which involves placing N 
non-attacking queens on an N x N chessboard. The program prints all 
possible solutions, one per line. Usage: nqueens N N must be an integer 
greater than or equal to 4.
"""


def get_queen_positions(board):
    """Returns a list of the positions of the queens."""
    positions = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                positions.append([row, col])
    return positions


def print_solutions(solutions):
    """Prints all solutions with the specific format."""
    for solution in solutions:
        print(solution)


def is_safe(board, row, col):
    """Checks if placing a queen at board[row][col] is safe."""
    # Check this column on the upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if j < 0:
            break
        if board[i][j] == 1:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if j >= len(board):
            break
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, solutions):
    """Uses backtracking to find all solutions to the N queens problem."""
    if row >= len(board):
        solutions.append(get_queen_positions(board))
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            solve_nqueens(board, row + 1, solutions)  # Recur to place rest of the queens
            board[row][col] = 0  # Backtrack


def main():
    """Main function to get input and solve the N queens problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0] * N for _ in range(N)]  # Initialize the board
    solutions = []
    solve_nqueens(board, 0, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
