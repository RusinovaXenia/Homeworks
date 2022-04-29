#Задания 6-7
def int_func(text):
    return text.title()
x = []
for letter in input('Введите слова через пробел: ').split(' '):
    x.append(int_func(letter))
print(' '.join(x))