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

# # Просте форматування рядка
# name = 'Dmytro'
# print('Hello, {}!'.format(name))

# # Форматування з декількома аргументами
# age = 25
# print('Hello, {}. You are {} years old.'.format(name, age))

# # Використання іменованих аргументів
# print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# # Використання індексів для вказівки порядку аргументів
# print('Hello, {1}. You are {0} years old.'.format(age, name))

# s = "Hello, World!"
# first_five = s[:5]
# print(first_five)  # Виведе 'Hello'

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = numbers[::2]
# print(odd_numbers)

# even_numbers = numbers[1:10:2]
# print(even_numbers)

# length = "2.75"
# width = "1.75"
# area = float(length) * float(width)
# show = f"With width {width} and length {length} of the room, its area is equal to area {area}."
# print(show)

# name = input("Your name? ")
# email = input("Your email? ")
# age = input("Your age? ")
# age = int
# height = input("Your height? ")
# height = float
# is_active = True

# my_list = [2024, 3.12]
# some_data = ['Python']
# my_list.insert(1,'Python')
# my_list.extend(some_data)
# print(my_list)

# num = 10
# if num > 10:
# else:
#     print("num не більше за 10")

# x = int(input('Введіть число: '))
# if x % 2 == 0:
#     print("Число x є парним")
# else:
#     print("Число x є непарним")

# a = int(input ('Введіть число'))
# if a>0:
#     print('Positive number')
# elif a<0:
#     print('Negative number')
# else:
#     print('This is zero')

# money = int(input('insert ammount of money '))
# if money:
#     print(f'You have {money} on your bank account')
# else:
#     print('You have no money on your bank account')

# result = None
# if result:
#     print(result)
# else:
#     print("Result is None, do something")

# user_name = input("Enter your name: ")

# if user_name:
#     print(f"Hello {user_name}")
# else:
#     print("Hi Anonym!")

# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)  # True
# print(a is c)  # False


# name = "Dmytro"
# age = 17
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")
# else:
#     print(f"User {name} can't rent a car")

# num = int(input("Введіть число: "))

# length = len(str(num))

# if length == 2 and num % 2 == 0:
#     print(f"{num} - Парне двозначне число")
# else:
#     print("Ні")

# num = int(input())

# if num % 3 == 0 and num % 5 == 0:
#     print('Fizzbuzz')
# elif num % 3 == 0:
#     print('Fizz')
# elif num % 5 == 0:
#     print('Buzz')
# else:
#     print(num)

# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#     print("X can`t be equal to zero")
#     x = int(input("X: "))

# result = y / x
# print(result)


# x = int(input("X: "))
# y = int(input("Y: "))
# if x >= 0:
#     if y >= 0:  # x > 0, y > 0
#         print("Перша чверть")
#     else:  # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:  # x < 0, y > 0
#         print("Друга чверть")
#     else:  # x < 0, y < 0
#         print("Третя чверть")

# is_nice = False
# if is_nice:
#     state = "nice"
# else:
#     state = "not nice"
# print(state)

# is_nice = True
# state = "nice" if is_nice else "not nice"
# print(state)


# some_data = None
# msg = some_data or "Не було повернено даних"
# print(msg)

# fruit = "banana"

# match fruit:
#     case "apple":
#         print("This is an apple.")
#     case "banana":
#         print("This is a banana.")
#     case "orange":
#         print("This is an orange.")
#     case _:
#         print("Unknown fruit.")

# point = (0, 0)

# match point:
#     case (0, 0):
#         print("Точка в центрі координат")  
#     case (0, y):
#         print(f"Точка лежить на осі Y: y={y}")  
#     case (x, 0):
#         print(f"Точка лежить на осі X: x={x}") 
#     case (x, y):
#         print(f"Точка має координати:  x={x}, y={y}") 
#     case _:
#         print("Це не точка")

# pets = ["dog", "fish", "cat"]

# match pets:
#     case ["dog", _, "cat"]:
#         # Випадок, коли є і собака, і кіт
#         print("There's a dog and a cat.")
#     case ["dog", _, _]:
#         # Випадок, коли є тільки собака
#         print("There's a dog.")
#     case _:
#         # Випадок для інших комбінацій
#         print("No dogs.")

# fruit = 'apple'
# for char in fruit:
#     print(char)


# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     print(char, end=" ")

# some_iterable = ["a", "b", "c"]

# for i in some_iterable:
#     print(i)

odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)
