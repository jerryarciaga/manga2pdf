import requests
from bs4 import BeautifulSoup
import img2pdf
import os
from PyPDF2 import PdfFileReader, PdfFileMerger

def search_manga():
    base_url = "https://mangareader.to"
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

    # Have user select what manga to download, then return the url
    choice = input("Enter number of title to download: ")
    return "".join([base_url, results[int(choice)-1].find("a")["href"]])

def select_chapter(url):
    base_url = "https://mangareader.to"
    user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
    params = {
        "User-Agent": user_agent,
    }

    # Request for chapter page
    chapter_page = requests.get(url, params=params)
    chapter_soup = BeautifulSoup(chapter_page.text, "html.parser")
    print(chapter_soup)

    # Then print chapter by chapter
    chapters = chapter_soup.find_all("li", class_="item reading-item chapter-item")
    index = 1
    for chapter in chapters:
        title = chapter.find(class_="item-link").find(class_="name")
        print(f"{index}. {title.text.strip()}")
        index += 1
    choice = input("Enter number of chapter to download: ")
    return "".join([base_url, chapters[int(choice)-1].find("a")["href"]])

if __name__ == "__main__":
    manga_url = search_manga()
    chapter_url = select_chapter(manga_url)
    print(chapter_url)
