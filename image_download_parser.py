import requests
from bs4 import BeautifulSoup
import fake_useragent


my_user = fake_useragent.UserAgent().random
header = {'user-agent': my_user}
url = f'https://wallpaperscraft.ru/'

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

block = soup.find('ul', class_='wallpapers__list')
all_image = block.findAll('li', class_='wallpapers__item')

image_number = 1

for image in all_image:
    image_link = image.find('a').get('href')
    print(image_link)
    image_bytes = requests.get(f'{url}{image_link}').content

    with open(f'image/{image_number}.jpeg', 'wb') as file:
        file.write(image_bytes)
    image_number += 1


