def printMax(x, y):
    ''' Именно эту запись

        Выводит printMax.__doc__. '''

    x = int(x)
    y = int(y)

    if x > y :
        print(x , '- наибольшее число')
    elif x < y :
        print(y, '- наибольшее число')

printMax(3, 5)
print(printMax.__doc__)