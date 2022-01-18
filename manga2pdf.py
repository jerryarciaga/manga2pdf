import requests
import img2pdf
import os

#TODO Generate config file for these things
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'
    }
#TODO Specify temporary image directory
#TODO Specify default destination for saved content


#TODO Get this url from parsed HTML
url = 'https://cdn.readdetectiveconan.com/file/mangap/5624/10067000/1.jpeg'
def download_image(url, filename):
    img_filename = filename + ".jpeg"
    pdf_filename = filename + ".pdf"
    with open(img_filename, "wb") as image:
        r = requests.get(url, headers=headers)
        for chunk in r.iter_content(chunk_size=128):
            image.write(chunk)
    with open(pdf_filename, "wb") as pdf:
        pdf.write(img2pdf.convert(img_filename))



download_image(url, "Teenage Mercenary") # Example usage

#TODO Define functions to download from sources and turn into full PDF
class Manga:
    def __init__(self):
        pass

