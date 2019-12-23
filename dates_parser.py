from bs4 import BeautifulSoup
import requests

source = requests.get('https://bingoschool.ru/blog/28/').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

for lists in article.find_all('ul'):
	for date in lists.find_all('li'):
		print(date.text)