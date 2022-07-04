import requests
from bs4 import BeautifulSoup
import img2pdf
import os
from PyPDF2 import PdfFileReader, PdfFileMerger

def search_manga():
    site = "https://mangareader.to/search"
    user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
    tmp_dir = "/tmp"

    search_title = input("Enter manga title: ")
    params = {
        "User-Agent":   user_agent,
        "keyword":      search_title,
    }

    # Search for manga, parse html
    search = requests.get(site, params=params)
    search_soup = BeautifulSoup(search.text, "html.parser")

    # Then print
    results = search_soup.find_all("h3", class_="manga-name")
    for result in results:
        print(result.text)


if __name__ == "__main__":
    search_manga()
