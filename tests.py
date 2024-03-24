# # Введення (отримання даних)
# ім_я = input("Введіть ваше ім'я: ")

# # Перетворення (обробка даних)
# вітання = f"Привіт, {ім_я}!"

# # Виведення (виведення даних)
# print(вітання)

# s1 = "Василь"
# s2 = "Васильович!"
# joined_string = f"Здарова! {s1} {s2}"
# print (joined_string)

# s1 = 'Hello'
# s2 = 'world!'
# joined_string = f"{s1} {s2}"  # Hello world!

# x1 = 10
# y1 = 10
# x2 = 25
# y2 = 25
# d = ((x1-x2)**2 + (y1-y2)**2)**0.5
# print (d)

# a = float(input("Введіть сторону квадрата:"))
# P = 4*a
# print(f"Периметр квадрата дорівнює {P}")

# # Цінова політика продуктів
# price_per_croissant = 1.04
# price_per_glass = 0.34
# price_per_coffee_pack = 4.42

# # Кількість кожного продукту
# num_croissants = int(input("Введіть кількість круасанів: "))
# num_glases = int(input("Введіть кількість стаканів: "))
# num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# # Обчислення загальної вартості
# total_cost = num_croissants * price_per_croissant +\
#              num_glases * price_per_glass + \
#              num_coffee_packs * price_per_coffee_pack

# # Визначаємо кількість повних доларів і центів
# total_dollars = int(total_cost)
# total_cents = int(total_cost * 100)

# # вивід результату
# print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
# print(f"Загальна вартість у центах: {total_cents} центів")

# chars = ['a', 'b', 'c', ]
# numbers = [1, 2]

# chars.extend(numbers) #доповнення списку іншим списком

# chars.insert(3,"b")

# let_ind = chars.index("c") #знаходження індекса числа

# print ((let_ind))

# my_list = [1, 2, 3, 4, 2, 2, 5, 2, 2, 2]
# count_2 = my_list.count(2) # перерахунок
# print(count_2)


# my_list = [1, 2, 3, 4, 5, 1,]
# print(len(my_list))

# nums = [3, 1, 4, 1, 5, 9, 2]
# nums.sort(reverse=True)
# print(nums)

# words = ["banana", "apple", "cherry"]
# words.sort(key=len)
# # sorted (words)
# print(words)

# my_dict = {"name": "Dmytro", "age": 24, "city": "Ivano-Frankivs'k"}
# my_dict["email"] = "dimakrevsun98@gmail.com"
# my_dict["age"] = 25
# del my_dict["age"]

# print("email" in my_dict)
# print("age" in my_dict)

# my_dict = {"name": "Dmytro", "age": 25}
# age = my_dict.get("age")  # Поверне 25
# gender = my_dict.get("gender")
# print(gender)

# b = set #Множина
# b = {1, 2, 3, 3, 2}
# print(b)

# lst = [1, 2, 3, 1, 2, 2, 3, 4, 1] #Виключення  дублів зі списку шляхом перетворення списку в множину
# d_lst = set(lst)
# lst = d_lst
# lst.add(4)

# print(lst)

# numbers = {1, 2, 3}
# numbers.discard(4)
# print(numbers)

# a = {1, 2, 3} #Знаходження спільних елементів у множинах
# b = {3, 4, 5}
# print(a.intersection(b))
# print(a & b)

# a = {1, 2, 3} #Знаходження різниці елементів у множинах
# b = {3, 4, 5}
# print(a.difference(b))
# print(a - b)

# a = {1, 2, 3} #Знаходження симетричної різниці (не спільні елементи) елементів у множинах
# b = {3, 4, 5}
# print(a.symmetric_difference(b))  # {1, 2, 4, 5}
# print(a ^ b)  # {1, 2, 4, 5}

# a = frozenset([1, 2, 3])
# b = frozenset([3, 4, 5])

# union = a | b  # Об'єднання множин
# intersection = a & b  # Перетин множин
# difference = a - b  # Різниця множин
# symmetric_difference = a ^ b  # Симетрична різниця

# print(union)  # frozenset({1, 2, 3, 4, 5})
# print(intersection)  # frozenset({3})
# print(difference)  # frozenset({1, 2})
# print(symmetric_difference)  # frozenset({1, 2, 4, 5})


# points = {   #Кортежний словник
#     (0, 0): "C",
#     (1, 1): "A",
#     (2, 2): "B"
# }
# turple_c = points.get((0, 0))
# print(turple_c)


# s = "Hello Dmytro"
# print(s[0])# H
# print(s[-1])# o

# Просте форматування рядка
name = 'Dmytro'
print('Hello, {}!'.format(name))

# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))

# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))

