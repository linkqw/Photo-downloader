import os
from bs4 import BeautifulSoup
import requests
import urllib.request


url = input("Введите путь к альбому с сайта вконтакте")
response = requests.get(url)
first_parser = BeautifulSoup(response.text, "lxml")

count = 1

direction = "downloads/"
if not os.path.isdir(direction):
    os.makedirs(direction)

images = first_parser.findAll('a', href=True)

for i in images:

    file_name = str(count) + ".jpg"
    temp_response = requests.get("https://vk.com" + i.get('href'))
    second_parser = BeautifulSoup(temp_response.text, 'lxml')

    src = second_parser.find('img')
    urllib.request.urlretrieve(src.get('src'), direction + file_name)

    print('another one was loaded...') if count > 1 else print('start is successfully')

    count += 1

print('ended')
