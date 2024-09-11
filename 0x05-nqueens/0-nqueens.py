#!/usr/bin/python3
"""
N Queens Problem: Solve the N Queens problem using backtracking.
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False


return True


def solve_n_queens(board, col, n, solutions):
    """
    Use backtracking to solve the N Queens problem and store solutions.
    """
    if col == n:
        # A valid solution has been found, store it in the required format
        solution = [[i, row.index(1)] for i, row in enumerate(board)]
        solutions.append(solution)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place the queen at the position board[i][col]
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_n_queens(board, col + 1, n, solutions)

            # If placing the queen here leads to no solution, backtrack
            board[i][col] = 0

    return res


def n_queens(n):
    """
    Initialize the board and solve the N Queens problem.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    return solutions


if __name__ == "__main__":
    # Input validation
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem and print the solutions
    solutions = n_queens(N)
    for solution in solutions:
        print(solution)
