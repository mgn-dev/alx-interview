#!/usr/bin/env python3
import sys

"""
This module solves the N queens problem, which involves placing N
non-attacking queens on an N x N chessboard. The program prints all
possible solutions, one per line. Usage: nqueens N N must be an integer
greater than or equal to 4.
"""


def print_board(board):
    """Prints the board configuration."""
    for row in board:
        print(' '.join('Q' if col == 1 else '.' for col in row))


def is_safe(board, row, col, N):
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
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if j >= N:
            break
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, N):
    """Uses backtracking to find all solutions to the N queens problem."""
    if row >= N:
        print_board(board)
        print()  # Print a new line after each solution
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place queen
            solve_nqueens(board, row + 1, N)  # Recur to place rest of queens
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
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    main()
