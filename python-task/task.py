import json
import os

def find_max_min_commit_dates(filename):
    """
    Need to find the dates with the highest and lowest number of commits from a JSON file (commit_data.json).

    Args:
        filename: Path of the json file

    Returns:
            - A list of dates with the highest number of commits.
            - The highest number of commits.
            - A list of dates with the lowest number of commits.
            - The lowest number of commits.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file) # Read JSON File and pass JSON Data into dictionary.

        commits_data = data['commits'] # Extracts lists of commits data from data dictionary.

        max_commits = max(entry['commits'] for entry in commits_data) # Iterate commits data and find the max value.

        # Iterate commits data and find the list of dates having max commits.
        max_commit_dates = [entry['date'] for entry in commits_data if entry['commits'] == max_commits]

        min_commits = min(entry['commits'] for entry in commits_data) # Iterate commits data and find the min value.

        # Iterate commits data and find the list of dates having min commits.
        min_commit_dates = [entry['date'] for entry in commits_data if entry['commits'] == min_commits]

        return max_commit_dates, max_commits, min_commit_dates, min_commits

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, None, None, None
    except json.JSONDecodeError:
        print(f"Error: Failed to parse the file. Invalid JSON format in '{filename}'.")
        return None, None, None, None

# Running current script as main program
if __name__ == "__main__":
    # fetching the json file
    filename = os.path.join("data", "commit_data.json")
    max_dates, max_commits, min_dates, min_commits = find_max_min_commit_dates(filename)

    if max_dates and min_dates:
        max_dates_str = ", ".join(max_dates) # Converting list of max dates into comma separated string
        min_dates_str = ", ".join(min_dates) # Converting list of min dates into comma separated string
        print(f"Maximum number of commits were made on {max_dates_str} totalling to {max_commits}")
        print(f"Minimum number of commits were made on {min_dates_str} totalling to {min_commits}")