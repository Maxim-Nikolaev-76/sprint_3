# Список для тестирования.
numbers = [1, 3, 4, 6, 9, 11]

# Здесь напишите ваше генераторное выражение.
simple_generator = (num ** 2 for num in numbers if num % 3 == 0)
# Распечатайте сумму квадратов.
print(sum(simple_generator))
