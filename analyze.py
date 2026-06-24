import chess

def get_material_balance(board):
    """
    Calculate the material balance of a chess board.

    Args:
        board (chess.Board): The chess board.

    Returns:
        int: The material balance, where positive values indicate an advantage for white and negative values indicate an advantage for black."""
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }
    balance = 0
    for piece_type in piece_values:
        balance += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        balance -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
    return balance

def analyze_game(boards):
    """
    Returns a list of material balance values, one per move.
    """
    return [get_material_balance(board) for board in boards]