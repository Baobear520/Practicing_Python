from pathlib import Path
import requests
from bs4 import BeautifulSoup


def get_content(url):
    response = requests.get(url)
    html = response.text
    return html

def get_text(page):
    
    # Parse the HTML content
    soup = BeautifulSoup(page, 'html.parser')

    # Locate the table by its id
    table = soup.find('table', id='AutoNumber14')

    # Extract all <p> tags from the located table
    p_tags = table.find_all('p') if table else []
    return p_tags

def save_in_file(path,html):
    # Extract and clean up the text from the <p> tags
    with open(path,"x") as f:
        for tag in html:
            # Remove any nested tags like <font>, <i>, <b> and their content
            text = tag.get_text(separator='\n', strip=True)
            if text:
                f.write(text)

def main():
    url = "http://www.prekfun.com/THEMES/PREKthemes/A-F/Beach/Beach_Songs.htm"
    page = get_content(url)
    html = get_text(page)
    base_path = Path("/Users/aldmikon/Desktop/")
    file_name = "beach_nursery_rhymes.txt"
    path = base_path / file_name
    save_in_file(path,html)
    print(f'The text has been successfully saved in {file_name}')

if __name__ == "__main__":
    main()
    