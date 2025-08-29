import matplotlib.pyplot as plt
from datetime import datetime
import os
import sys


def plot_habit_progress(habit_name, completions, show_plot=False):
    """Generate a progress graph for a habit.

    Args:
        habit_name (str): Name of the habit.
        completions (list of str): List of ISO format datetime strings.
        show_plot (bool): Whether to display the plot interactively.
    """
    if not completions:
        print("No completion data available for this habit.")
        return None

    dates = [datetime.fromisoformat(c) for c in completions]
    dates_sorted = sorted(dates)

    plt.figure(figsize=(10, 5))
    plt.plot(dates_sorted, range(1, len(dates_sorted) + 1), 'b-o')
    plt.title(f"{habit_name} Completion Progress")
    plt.xlabel("Date")
    plt.ylabel("Total Completions")
    plt.grid(True)
    plt.xticks(rotation=45)

    os.makedirs("graphs", exist_ok=True)
    filename = f"graphs/{habit_name.lower().replace(' ', '_')}_progress.png"
    plt.tight_layout()
    plt.savefig(filename)

    if show_plot:
        plt.show()  # This opens the interactive plot window

    plt.close()

    return filename
