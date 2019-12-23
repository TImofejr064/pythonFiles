import requests

import requests

r = requests.post('https://b.utair.ru/api/v1/login/',
   data = {'login':'+79619478717'},
   headers = {
   'Accept-Language':'en-US,en;q=0.5',
   'Connection':'keep-alive',
   'Host':'b.utair.ru',
   'origin':'https://www.utair.ru',
   'Referer':'https://www.utair.ru/'})

print(r)
print(r.text)