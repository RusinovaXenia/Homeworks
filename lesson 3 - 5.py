#Задание 5
summary = 0
print("Введите цифры через пробел для подсчета")
print("x - спец.символ, заканчивающий подсчет, пустая строка тоже заканчивает подсчет")
def digital_sum(s, str):
 arr = str.split(' ')
 str_sum = 0
 for i in arr:
  if i != "x":
   str_sum = str_sum + int(i)
   is_no_x = True
  else:
   is_no_x = False
   break
 return str_sum, is_no_x

while True:
 user_input = input()
 if user_input:
  summary = summary + digital_sum(summary, user_input)[0]
  print(summary)
 else:
  break
 if digital_sum(summary, user_input)[1]:
  continue
 else:
  break
 print(summary)
