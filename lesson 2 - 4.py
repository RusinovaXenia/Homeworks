#Задание 5
a = input('Введите слова через пробел: ')
a = a.split( )
for i, j in enumerate(a):
    print(i+1,j[0:10])