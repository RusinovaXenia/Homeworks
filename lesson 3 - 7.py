#Задание 7
def title(text):
    listed_text = list(text)
    listed_text[0] = listed_text[0].upper()
    return ''.join(listed_text)
output_2 = []
for word in input('Введите слова через пробелам: ').split(' '):
    output_2.append(title(word))
print(" ".join(output_2))