import requests
from bs4 import BeautifulSoup



page = 1
url = f'https://kinokrad.cc/page/{page}/'
response = requests.get(url)

data = []

soup = BeautifulSoup(response.text, 'html.parser')
films = soup.findAll('div', class_='shorposterbox')

with open('titles.txt', 'w') as f:
    for film in films:
        link = film.find('a').get('href')
        name = film.find('a').text
        genre = film.find('div', class_='item janr').findAll('span')[1].text.replace('/', ',')
        year = film.find('div', class_='item year').findAll('span')[1].text
        f.write(f'{name}/ link: {link}/ Genre: {genre}/ {year}' + '\n')


