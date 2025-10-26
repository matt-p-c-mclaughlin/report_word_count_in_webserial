import os
import sys
from pathlib import Path

OG_STDOUT = sys.stdout
OG_README = Path(f"{os.path.abspath(__file__)}/../../Plain_README.md")

MD_file_path = Path(f"{os.path.abspath(__file__)}/../../Outputs/search-report.md")
TXT_file_path = Path(f"{os.path.abspath(__file__)}/../../Outputs/search-report.txt")
README_file_path = Path(f"{os.path.abspath(__file__)}/../../README.md")

def reset_output_files():
    for path in [MD_file_path, TXT_file_path, README_file_path]:
        if os.path.exists(path):
            try:
                os.remove(path)
                print(f"File '{path}' deleted successfully.")
            except OSError as e:
                print(f"Error deleting file '{path}': {e}")
        
        path.parent.mkdir(parents=True, exist_ok=True) 
        path.touch()

    # Copy Plain README to README.md
    try:
        with open(OG_README, 'r') as source_file:
            content = source_file.read()

        with open(README_file_path, 'w') as destination_file:
            destination_file.write(content)
        print(f"Content successfully copied from '{OG_README}' to '{README_file_path}'.")
    except FileNotFoundError:
        print(f"Error: One of the files was not found. Please check the paths.")
    except Exception as e:
        print(f"An error occurred: {e}")

