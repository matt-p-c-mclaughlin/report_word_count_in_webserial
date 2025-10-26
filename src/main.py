import requests
from bs4 import BeautifulSoup
import time
import datetime
from pathlib import Path

## My helpers
from init_files import *
from printers import print_MD, print_TXT

def main():
    start = time.time()
    start_url = "https://www.royalroad.com/fiction/130987/all-jobs-and-classes-i-just-wanted-one-skill-not/chapter/2563494/chapter-01"
    search_keyword = "smirk"

    #Initialize output files
    reset_output_files()

    scrape_chapters(start_url, search_keyword, delay=0.5)

    end = time.time()
    t = str(datetime.timedelta(seconds = end - start))[2:10]

    print_MD(f"<p>Time taken: {t}</p>")
    print_TXT(f"Time taken: {t}")
    add_report_to_README()

    print("Exit")

def scrape_chapters(start_url: str, search_string: str, delay: float = 1.0):
    
    total_count = 0
    current_url = start_url
    chapter_number = 1

    print_MD(f"<p>Starting scrape from: <a href={start_url}>{start_url}</a></p>\
<p>Searching for occurrences of: <mark>{search_string}</mark></p>")
    print_TXT(f"Starting scrape from: {start_url}\n\
Searching for occurrences of: {search_string}\n")

    while current_url:
        try:
            response = requests.get(current_url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching {current_url}: {e}")
            break

        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Count occurrences (case-insensitive)
        chap_name = soup.find("h1").get_text(strip=True) if soup.find("h1") else "Unknown Title"
        if chap_name == "Comedian0": break
        page_text = soup.get_text()
        count = page_text.lower().count(search_string.lower())
        total_count += count

        
        if chapter_number == 1:
            print_MD("<details closed><summary>Chapter Count List</summary><p></p>")

        print_MD(f"&emsp;<u>{chap_name}</u>: {count}")
        print_TXT(f"    {chap_name}: {count}")

        # Look for "Next Chapter" link
        next_url = None
        if chapter_number == 1:
            # Slower search for Ch 1 only - buttons are ordered differently when no previous chapter
            buttons = soup.select("a.btn.btn-primary.col-xs-12")
            for btn in buttons:
                if "Next" in btn.get_text():
                    next_url = btn.get("href")
                    break
        else:
            # Look for "Next Chapter" link
            next_url = soup.select("a.btn.btn-primary.col-xs-12")[1].get("href") if len(soup.select("a.btn.btn-primary.col-xs-12")) > 1 else None

        if not next_url:
            break

        # Convert relative URLs to absolute if necessary
        if next_url.startswith('/'):
            from urllib.parse import urljoin
            current_url = urljoin(current_url, next_url)
        else:
            current_url = next_url

        chapter_number += 1
        #time.sleep(delay)  # Be polite

    chapter_number -= 1 # Adjust for last increment when no next_url
    print_MD("</details>")
    
    print_MD(f"<p>Finished scraping.</p> <h3>Total occurrences of {search_string}' \
across {chapter_number} chapters: <mark>{total_count}</mark></h3>\
<p>Average of {total_count/chapter_number:.2f} per chapter.</p>")
    
    print_TXT(f"Finished scraping.\n\
Total occurrences of '{search_string}' across {chapter_number} chapters: {total_count}\n\
Average of {total_count/chapter_number:.2f} per chapter.")
  
### Append report to README.md
### This is so that when viewed on GitHub, the latest report is visible without needing to open the Outputs folder
### Readme.md is reset at start of run to Plain_README.md
def add_report_to_README():
    try:
        with open(str(README_file_path), "a", encoding="utf-8") as destination:
            with open(str(MD_file_path), "r", encoding="utf-8") as source:
                markdown_text = source.read()
                destination.write("## Latest Report" + "\n")
                for line in markdown_text.splitlines():
                    destination.write(line + "\n")
    except FileNotFoundError:
        print(f"Error: {MD_file_path} not found. Please create the file or specify the correct path.")
        exit()

if __name__ == "__main__":
    main()