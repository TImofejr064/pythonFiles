from bs4 import BeautifulSoup
import requests

source = requests.get('https://5-ege.ru/daty-po-istorii-rossii/').text

soup = BeautifulSoup(source, 'lxml')

block = soup.find('div', class_='entry-content')

dates = block.find_all('p').text
print(dates)