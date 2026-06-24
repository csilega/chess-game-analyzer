import chess.pgn
import os

def parse_moves(game):
    """
    Parse the moves from a chess game.

    Args:
        game (chess.pgn.Game): The chess game.

    Returns:
        list: A list of the moves in the game."""
    board = game.board()
    moves = []
    for move in game.mainline_moves():
        board.push(move)
        moves.append(board.copy())
    return moves