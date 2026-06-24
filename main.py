from load_pgn import load_game
from parse_game import parse_moves
from analyze import analyze_game
from visualize import plot_material_balance

if __name__ == "__main__":
    game = load_game("example.pgn")
    moves = parse_moves(game)
    print(f"Loaded game with {len(moves)} moves.")
    print(moves[0])

if __name__ == "__main__":
    game = load_game("example.pgn")
    moves = parse_moves(game)
    balances = analyze_game(moves)
    print(f"Loaded game with {len(moves)} moves.")
    print(f"Material balances per move: {balances}")

if __name__ == "__main__":
    game = load_game("example.pgn")
    moves = parse_moves(game)
    balances = analyze_game(moves)
    plot_material_balance(balances)