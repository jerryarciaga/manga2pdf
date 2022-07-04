import requests
from bs4 import BeautifulSoup
import img2pdf
import os
from PyPDF2 import PdfFileReader, PdfFileMerger

def search_manga():
    site = "https://mangareader.to/search"
    user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"

    search_title = input("Enter manga title: ")
    params = {
        "User-Agent":   user_agent,
        "keyword":      search_title,
    }

    # Search for manga, parse html
    search = requests.get(site, params=params)
    search_soup = BeautifulSoup(search.text, "html.parser")

    # Then print numbered list
    results = search_soup.find_all("h3", class_="manga-name")
    index = 1
    print(f"Results for {search_title}:\n")
    for result in results:
        print(f"{index}. {result.text.strip()}")
        index += 1

    # Have user select what manga to download
    choice = input("Enter number of title to download: ")
    return results[int(choice)-1].find("a")["href"]

if __name__ == "__main__":
    lambsauce = search_manga()
    print(f'''
        Gordon: Where's the lamb sauce?
        manga2pdf: {lambsauce}
    ''')
