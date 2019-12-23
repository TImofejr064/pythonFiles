from bs4 import BeautifulSoup
import requests
from colorama import init
init()
from colorama import Fore, Back, Style

for i in range(1, 17):
	if i == 1 :
		source = requests.get('https://coreyms.com').text

		soup = BeautifulSoup(source, 'lxml')

		for article in soup.find_all('article'):

			headline = article.header.h2.a.text	
			print(Back.WHITE + Fore.BLACK + headline)

			description = article.div.p.text
			print(Back.YELLOW + Fore.BLACK + description)

			#vid_src = article.find('iframe')['src']
			#vid_id = vid_src.split('/')[4]
			#print(Back.RED + Fore.BLACK +vid_src)
	else :
		source = requests.get('https://coreyms.com/page' + str(i)).text

		soup = BeautifulSoup(source, 'lxml')

		for article in soup.find_all('article'):

			headline = article.header.h2.a.text	
			print(Back.WHITE + Fore.BLACK + headline)

			description = article.div.p.text
			print(Back.YELLOW + Fore.BLACK + description)

			#vid_src = article.find('iframe')['src']
			#vid_id = vid_src.split('/')[4]
			#print(Back.RED + Fore.BLACK +vid_src)

