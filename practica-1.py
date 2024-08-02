# Импортируйте необходимые модули.
from datetime import datetime


# Укажите два параметра функции:
def validate_record(name, birthday):
    # Напишите код, верните булево значение.
    try:
        datetime.strptime(birthday, '%d.%m.%Y')
    except ValueError:
        print(f'Некорректный формат даты в записи: {name}, {birthday}')
        return False
    else:
        return True


# Укажите параметры функции:
def process_people(data):
    # Объявите счётчики.
    good_count = 0
    bad_count = 0
    people = {}
    # в каждой паре значений из списка data
    # проверьте корректность формата даты рождения
    # и в зависимости от результата проверки увеличьте один из счётчиков.
    for items in data:
        name, birthday = items
        if validate_record(name, birthday):
            good_count += 1
        else:
            bad_count += 1
    people['good'] = good_count
    people['bad'] = bad_count
    return people


data = [
    ('Иван Иванов', '10.01.2004'),
    ('Пётр Петров', '15.03.1956'),
    ('Зинаида Зеленая', '6 февраля 1997'),
    ('Елена Ленина', 'Второе мая тысяча девятьсот восемьдесят пятого'),
    ('Кирилл Кириллов', '26/11/2003')
]
statistics = process_people(data)
# Выведите на экран информацию о корректных и некорректных записях
# в таком формате:
# Корректных записей: <число>
# Некорректных записей: <число>
good = statistics['good']
bad = statistics['bad']
print(f'Корректных записей: {good}')
print(f'Некорректных записей: {bad}')
