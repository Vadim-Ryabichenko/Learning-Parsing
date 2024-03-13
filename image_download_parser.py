import requests
from bs4 import BeautifulSoup
import fake_useragent


my_user = fake_useragent.UserAgent().random
header = {'user-agent': my_user}
url = f'https://www.nastol.com.ua/peoples/'

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')


block = soup.findAll('div', class_='verh')


image_number = 1

for image in block:
    image_link = image.find('a').get('href')
    download = requests.get(image_link).text
    download_soup = BeautifulSoup(download, 'html.parser')
    download_block = download_soup.find('div', class_='llink')

    image_link2 = download_block.find('a').get('href')
    download2 = requests.get(image_link2).text
    download_soup2 = BeautifulSoup(download2, 'html.parser')
    
    result_link = download_soup2.findAll('div')[16].find('a').get('href')

    image_bytes = requests.get(f'{result_link}').content

    with open(f'image/{image_number}.jpg', 'wb') as file:
        file.write(image_bytes)
    image_number += 1


