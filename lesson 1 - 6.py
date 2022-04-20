#Задание 6
income = int(input('Укажите выручку: '))
expenses = int(input('Укажите издержки: '))
profit = income - expenses
if income > expenses:
    print('Ваша выручка: ', profit)
    efficiency = profit / income
    n = int(input('Численность сотрудников: '))
    x = profit / n
    print('Прибыль на одного сотрудника составляет:', x)
else:
    print('Вы работаете в убыток')

