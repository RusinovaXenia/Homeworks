#Задание 6
products = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

names = []
prices = []
quantity = []
units = []

for i in products:
    names.append(i[1]['название'])
    prices.append(i[1]['цена'])
    quantity.append(i[1]['количество'])
    units.append(i[1]['eд'])

units = set(units)

b = dict(
    название=names,
    цена=prices,
    количество=quantity,
    ед=units
)

print(b)