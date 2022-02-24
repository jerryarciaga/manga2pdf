import requests
import img2pdf
import os
from PyPDF2 import PdfFileReader, PdfFileMerger

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
        print(f"Downloading {r.url}...")
        for chunk in r.iter_content(chunk_size=128):
            image.write(chunk)
    with open(pdf_filename, "wb") as pdf:
        pdf.write(img2pdf.convert(img_filename))
    os.remove(img_filename)

# Uses download_pdf function to download a whole chapter
def download_chapter(manga_id, chapter):
    base_url = f"https://www.readm.org/uploads/chapter_files/{manga_id}/{chapter}/"
    page = 1
    chapter = PdfFileMerger(strict=False)

    while True: # TODO Figure out a way to do this faster
        url = base_url + f"{page}.jpg"
        test = requests.get(url, headers=headers)
        if test.status_code == 200:
            download_pdf(url, str(page))
            with open(f"{page}.pdf", "rb") as current_file:
                current_page = PdfFileReader(current_file)
                chapter.append(current_page)
                current_file.close()
            os.remove(f"{page}.pdf")
            page += 1
        else:
            chapter.write("chapter.pdf")
            break

if __name__ == '__main__':
    download_chapter(17427, 111)
