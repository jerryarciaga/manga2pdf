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
    img_filename = filename + ".jpeg"
    pdf_filename = filename + ".pdf"
    with open(img_filename, "wb") as image:
        r = requests.get(url, headers=headers)
        for chunk in r.iter_content(chunk_size=128):
            image.write(chunk)
    with open(pdf_filename, "wb") as pdf:
        pdf.write(img2pdf.convert(img_filename))
    os.remove(img_filename)

# Example Usage
if __name__ == '__main__':
    numPages = 14 # TODO Get this number from parsing HTML
    chapter = PdfFileMerger(strict=False)
    # TODO Turn this chunk of for loop code into a function
    for page in range(numPages):
        url = f"https://cdn.readdetectiveconan.com/file/mangap/3262/10156000/{page+1}.jpeg"
        download_pdf(url, f"Page {page + 1}")
        currentFile = open(f"Page {page + 1}.pdf", "rb")
        currentPage = PdfFileReader(currentFile)
        chapter.merge(
            position=page,
            fileobj=currentPage,
        )
        currentFile.close()
        os.remove(f"Page {page + 1}.pdf")
    chapter.write('chapter.pdf')

