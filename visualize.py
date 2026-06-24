import matplotlib.pyplot as plt

def plot_material_balance(balances):
    """
    Plots the material balance over the course of a chess game.
    """

    moves = list(range(1, len(balances) + 1))

    plt.figure(figsize=(12, 5))
    plt.xlim(1, len(balances))
    plt.plot(moves,balances, color='blue', marker='o', linestyle='-', linewidth=2, markersize=5)
    plt.title('Material Balance Over Moves')
    plt.fill_between(moves, balances, where=[b >= 0 for b in balances], color='green', alpha=0.3, label='White Advantage')
    plt.fill_between(moves, balances, where=[b < 0 for b in balances], color='red', alpha=0.3, label='Black Advantage')
    plt.xlabel('Move Number')
    plt.ylabel('Material Balance (White - Black)')
    plt.axhline(0, color='gray', linestyle='--', label='Equal Material')
    plt.legend()
    plt.tight_layout()
    plt.savefig('material_balance_plot.png')  # Save the plot as a PNG file
    plt.grid()
    plt.show()
    print("Material balance plot saved as 'material_balance_plot.png' and displayed.")