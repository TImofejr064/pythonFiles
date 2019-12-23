import sys #импорт модуля sys

print('Аргументы командной строки :')

for i in sys.argv: # выводим в цикле аргументы 
    print(i)       # командной строки  
                   # что-бы передать аргументы, при вызове 
                   # записываем так: python using_sys.py Дим Дымыч лох 
print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')