import requests
import img2pdf
import os
from PyPDF2 import PdfFileReader, PdfFileMerger
from tqdm import tqdm

#TODO Generate config file for these things
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'
    }
#TODO Specify temporary image directory
#TODO Specify default destination for saved content


# Download images, then convert to pdf
def download_pdf(url, filename):
    img_filename = filename + ".jpg"
    pdf_filename = filename + ".pdf"
    params = {"v": "12"} # Specific to https://readm.org

    with open(img_filename, "wb") as image:
        r = requests.get(url, headers=headers, params=params)
        for chunk in r.iter_content(chunk_size=128):
            image.write(chunk)
    with open(pdf_filename, "wb") as pdf:
        pdf.write(img2pdf.convert(img_filename))
    os.remove(img_filename)

# Uses download_pdf function to download a whole chapter
def download_chapter(manga_id, chapter, chapter_title):
    base_url = f"https://www.readm.org/uploads/chapter_files/{manga_id}/{chapter}/"
    pages = 1 # Count the number of pages in the chapter
    while True:
        url = base_url + f"{pages}.jpg"
        test = requests.get(url, headers=headers)
        if test.status_code != 200:
            pages -= 1
            break
        else:
            pages += 1

    chapter = PdfFileMerger(strict=False)
    for i in tqdm(range(pages), desc=f"Downloading {chapter_title}...",
                  ascii=False, ncols=75):
        page = i + 1
        url = base_url + f"{page}.jpg"
        download_pdf(url, str(page))
        with open(f"{page}.pdf", "rb") as current_file:
            current_page = PdfFileReader(current_file, strict=False)
            chapter.append(current_page)
        os.remove(f"{page}.pdf")
    chapter.write(f"{chapter_title}.pdf")

if __name__ == '__main__':
    download_chapter(17427, 1, "Chapter 1")
    download_chapter(17427, 2, "Chapter 2")
    download_chapter(17427, 3, "Chapter 3")
