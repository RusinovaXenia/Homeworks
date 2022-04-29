#Задание 2
a = input('Введите имя: ')
b = input('Введите фамилию: ')
c = input('Введите год рождения: ')
d = input('Введите город проживания: ')
e = input('Введите e-mail: ')
f = input('Введите телефон: ')
def func(**kwargs):
    s = kwargs['Имя']+ ',' + kwargs['Фамилия']+','+kwargs['Год']+','+kwargs['Город']+','+kwargs['Почта']+','+kwargs['Телефон']
    return s
print (func(Имя=a, Фамилия=b, Год=c, Город=d, Почта=e, Телефон=d))
