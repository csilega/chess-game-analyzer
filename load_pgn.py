import chess.pgn
import os

def load_game(filepath):
    """
    Load a chess game from a PGN file.

    Args:
        filepath (str): The path to the PGN file.

    Returns:
        chess.pgn.Game: The loaded chess game."""
    with open(filepath) as f:
        return chess.pgn.read_game(f)
    