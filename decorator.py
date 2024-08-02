from random import choice, uniform


def format_float_return(func):
    # Ваш код здесь
    def wrapper():
        # Вызвыаем декорируемую функцию.
        result = func()
        # Проверяем, на соответствие классу float.
        if isinstance(result, float):
            # Округляем если это float, переопределяем переменную result
            result = round(result, 2)
        # Возвращаем результат декорируемой функции
        return result
    # Возвращаем результат декоратора
    return wrapper


# Не изменяйте код ниже: он поможет проверить работу декоратора.
# Декорируем функцию:
@format_float_return
def test_function_1():
    """Возвращает случайное число типа float в диапазоне от -10 до 10,
    например -4.3897268052813265.
    """
    return uniform(-10, 10)


# Декорируем вторую функцию:
@format_float_return
def test_function_2():
    """Возвращает случайный элемент списка sequence - число или строку."""
    sequence = [
        3.1415926535,
        'pi',
        3.14,
        'пи',
        'три целых четырнадцать сотых',
        3.14159
    ]
    # Функция choice() из модуля random возвращает 
    # случайный элемент последовательности.
    return choice(sequence)


# Вызовем задекорированные функции для проверки работы декоратора:
print(test_function_1())
print(test_function_2())
