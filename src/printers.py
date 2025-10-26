from init_files import MD_file_path, TXT_file_path, OG_STDOUT
import sys


def print_MD(s : str):
    with MD_file_path.open('a') as file:
        sys.stdout = file  # Change the standard output to the file we created.
        print(f"""
{s}
              """)
        sys.stdout = OG_STDOUT  # Reset the standard output to its original value.
        
def print_TXT(s : str):    
    with TXT_file_path.open('a') as file:
        sys.stdout = file  # Change the standard output to the file we created.
        print(s)
        sys.stdout = OG_STDOUT  # Reset the standard output to its original value.
   