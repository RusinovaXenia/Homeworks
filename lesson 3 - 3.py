#Задание 3
def my_func(arg1, arg2, arg3):
    print(arg1 + arg2 + arg3 - min([arg1, arg2, arg3]))
my_func(int(input('Число 1:')),int(input('Число 2:')),int(input('Число 3:')))