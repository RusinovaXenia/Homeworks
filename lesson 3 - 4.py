#Задание 4
def my_func(x, y):
    s=1
    for i in range(y):
        s = x*s
    return s
#    return x ** y
print(f'{my_func(int(input("x: ")), int(input("y: ")))}')
