"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = 0
    oCount = 0
    emptyCount = 0
    for row in board:
        for square in row:
            if square == X:
                xCount += 1
            elif square == O:
                oCount += 1
            else:
                emptyCount += 1

    if emptyCount == 9:
        return X
    if xCount > oCount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # keep track of each row, column and diagonal
    # [row1, row2, row3, col1, col2, col3, diag1, diag2]
    # +1 if X is in position, -1 if O is in position
    score = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                score[i] += 1
                score[j+3] += 1
                if i == j:
                    score[6] += 1
                elif abs(i - j) == 2:
                    score[7] += 1
                if i == 1 and j == 1:
                    score[7] += 1
            elif board[i][j] == O:
                score[i] -= 1
                score[j+3] -= 1
                if i == j:
                    score[6] -= 1
                elif abs(i - j) == 2:
                    score[7] -= 1
                if i == 1 and j == 1:
                    score[7] -= 1
    # print(score)
    if 3 in score:
        return X
    elif -3 in score:
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1

    if winner(board) == O:
        return -1
    
    if winner(board) == None:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            k = min_value(result(board, action))
            if k > v:
                v = k
                best_move = action
    else:
        v = math.inf
        for action in actions(board):
            k = max_value(result(board, action))
            if k < v:
                v = k
                best_move = action
    return best_move


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v