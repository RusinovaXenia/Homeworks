#Задание 5
my_list = [7, 5, 3, 3, 2]
a = int(input('Ваш рейтинг: '))
my_list.append(a)
my_list.sort(reverse=True)
print(my_list)