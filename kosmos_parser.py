from bs4 import BeautifulSoup
import requests

source = requests.get('https://restoran-kosmos.ru/').text

soup = BeautifulSoup(sorce, 'lxml')
