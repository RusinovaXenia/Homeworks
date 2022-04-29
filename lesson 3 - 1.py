#Задание 1
a = int(input('введите число: '))
b = int(input('введите еще число: '))
def func(a, b):
    if b != 0:
        s = a / b
    else:
        s = 'нельзя делить на 0'
    return s
print(func(a, b))
