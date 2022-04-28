#Задание 2
a = input('Введите последовательность чисел: ')
a = a.split(' ')
for i in range(0, len(a) - 1, 2):
    a[i],a[i+1] = a[i+1], a[i]
print(a)