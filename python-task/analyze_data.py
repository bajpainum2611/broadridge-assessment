import json
import matplotlib.pyplot as plt
import os

def analyze_commit_data(filename):
    """
    Analyzes commit data from a JSON file and generates a line plot.

    Args:
        filename: Path of the json file
    """
    try:
        with open(filename, 'r') as f:
            data = json.load(f)

        dates = [entry['date'] for entry in data['commits']]
        commit_counts = [entry['commits'] for entry in data['commits']]

        plt.figure(figsize=(12, 6))
        plt.plot(dates, commit_counts, marker='o', linestyle='-', color='blue')
        plt.xlabel('Date')
        plt.ylabel('Number of Commits')
        plt.title('Daily Commits Over Time')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        # Annotate maximum and minimum points
        max_commits = max(commit_counts)
        max_indices = [i for i, x in enumerate(commit_counts) if x == max_commits]
        for i in max_indices:
            plt.annotate(f'{max_commits} commits', xy=(dates[i], max_commits), xytext=(dates[i], max_commits + 5),
                         arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

        min_commits = min(commit_counts)
        min_indices = [i for i, x in enumerate(commit_counts) if x == min_commits]
        for i in min_indices:
            plt.annotate(f'{min_commits} commits', xy=(dates[i], min_commits), xytext=(dates[i], min_commits - 5),
                         arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filename}'.")

if __name__ == "__main__":
    # Assuming your file is in the 'data' folder
    filename = os.path.join("data", "commit_data.json")
    analyze_commit_data(filename)