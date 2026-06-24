Chess Game Analyzer

A Python tool that parses chess games from PGN files, analyzes material balance move-by-move, and visualizes the results as a chart.

What it does:

Loads any chess game in PGN format
Parses every move and tracks the board state
Calculates material balance (white minus black) after each move
Outputs a chart showing who had the material advantage throughout the game

Project structure

chess-game-analyzer/
│
├── main.py          # Entry point — ties all modules together
├── load_pgn.py      # Loads a PGN file and returns a game object
├── parse_game.py    # Parses moves into a list of board states
├── analyze.py       # Calculates material balance per move
├── visualize.py     # Plots and saves the material balance chart
├── example.pgn      # Sample game to test with
└── README.md

Requirements:

Python 3.8+
python-chess
matplotlib

Installation

1. Clone the repository

git clone https://github.com/csilega/chess-game-analyzer.git
cd chess-game-analyzer

2. Install dependencies

pip install chess 
pip install matplotlib

Usage

1. Get a PGN file

Download any game from Lichess or Chess.com in PGN format and place it in the project folder.

2. Run the analyzer

python main.py

By default, it loads example.pgn. To analyze a different file, update the filename in main.py:

game = load_game("your_game.pgn")

3. View the output

A chart will pop up and save as material_balance_plot.png in the project folder.



How material balance is calculated:

Each piece is assigned a standard value:

Piece Value:
Pawn = 1
Knight = 3
Bishop = 3
Rook = 5
Queen = 9

After each move, white's total material minus black's total material is calculated. A positive value means white is ahead; a negative value means black is ahead.

Example output is shown in material_balance_plot.png:
The chart is from a real 85-move game. 
You can see white briefly winning material around move 11, the game staying roughly equal through the middlegame, and white pulling ahead decisively in the endgame.

Planned improvements:


-Stockfish integration for position evaluation beyond material count
-Automatic annotation of key turning points on the chart
-Support for analyzing multiple games from a single PGN file
-Command-line argument for specifying the PGN file path
