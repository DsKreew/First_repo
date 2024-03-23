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

words = ["banana", "apple", "cherry"]
words.sort(key=len)
# sorted (words)
print(words)
