from bs4 import BeautifulSoup as BS
import requests 

while True:

	word = input('Введите искомое слово: ')

	r     = requests.get('http://gramota.ru/slovari/dic/?word='+word+'&all=x'+str(word))
	soup  = BS(r.content, 'lxml')

	block = soup.find('div', class_='inside block-content').text
	print(block)

#video = soup.find_all('ytd-video-renderer', class_ = 'style-scope ytd-expanded-shelf-contents-renderer')
#for links in leftSide.find_all('li') :
	#print (links.text)
