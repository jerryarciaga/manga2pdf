import requests

#TODO Generate config file for this thing
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'
    }

#TODO Get this url from parsed HTML
url = 'https://cdn.readdetectiveconan.com/file/mangap/5624/10067000/1.jpeg'

#TODO Turn this into class function
def download_image(url, filename):
    with open(filename, "wb") as image:
       r = requests.get(url, headers=headers)
       for chunk in r.iter_content(chunk_size=128):
           image.write(chunk)

download_image(url, "image.jpg")

