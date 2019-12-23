shoplist = ['Choup', 'Pepsi', 'carrot', 'bread', 'car'] # мы создали список 

print('Length of shoplist',len(shoplist)) # здесь мы вывели длину списка

print('Buys: ', end=' ')

for item in shoplist:	 # В этом цикле мы выводим
	print(item, end=' ') # весь список покупок

print('\n I need to add rise. ')
shoplist.append('rise') # Добавляем в список рис

print('Buys: ', end=' ')
for item in shoplist:	 # В этом цикле мы выводим
	print(item, end=' ') # весь список покупок


print('\nFirst thing : ', shoplist[2])

shoplist.sort()
print('\nSort : ', shoplist)

print('Delete Choup')

del shoplist[0]

print('New shoplist : ', shoplist)