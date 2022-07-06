"""
Tic Tac Toe Player
"""
import copy
import math

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


def count_board(board):
    x_count = 0
    o_count = 0
    empty_count = 0
    for i in board:
        for j in i:
            if j == X:
                x_count += 1
            elif j == O:
                o_count += 1
            elif j == EMPTY:
                empty_count += 1

    return x_count, o_count, empty_count


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count, o_count, empty_count = count_board(board)

    if empty_count == 9:
        return X
    if x_count + o_count == 9:
        return None
    if x_count == o_count:
        return X
    if x_count > o_count:
        return O
    return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    playerr = player(board)

    if action[0] > 2 or action[0] < 0 or action[1] > 2 or action[1] < 0:
        raise Exception("bad input")

    new_board[action[0]][action[1]] = playerr
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]

    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    s = winner(board)

    if s == X or s == O:
        return True

    x, o, e = count_board(board)
    if s is None and x + o == 9:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    r = winner(board)
    if r == X:
        return 1
    if r == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
