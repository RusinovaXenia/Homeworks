#Задание 5
income = int(input('Укажите выручку: '))
expenses = int(input('Укажите издержки: '))
if income < expenses:
    print('Вы работаете в убыток')
else:
    print('Поздравляю, вы получаете доход')