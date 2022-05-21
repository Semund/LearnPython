# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
from collections import Counter

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
print('#1')

cnt = Counter(student['first_name'] for student in students)
for name, freq in cnt.items():
    print(f'{name}: {freq}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
print('===========\n#2')

cnt = Counter(student['first_name'] for student in students)
print(f'Самое частое имя среди учеников: {cnt.most_common(1)[0][0]}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ], [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

print('===========\n#3')

for cl_number, school_class in enumerate(school_students, start=1):
    cnt = Counter(cl['first_name'] for cl in school_class)
    print(f'Самое частое имя в классе {cl_number}: {cnt.most_common(1)[0][0]}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

print('===========\n#4')
for cl in school:
    boys, girls = 0, 0
    for person in cl['students']:
        if is_male[person["first_name"]]:
            boys += 1
        else:
            girls += 1
    print(f'Класс {cl["class"]}: девочки {girls}, мальчики {boys}')

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

print('===========\n#5')

max_boys, max_girls = 0, 0
more_girls, more_boys = None, None
for cl in school:
    boys, girls = 0, 0

    for person in cl['students']:
        if is_male[person["first_name"]]:
            boys += 1
        else:
            girls += 1

    if boys > max_boys:
        more_boys = cl
        max_boys = boys
    if girls > max_girls:
        more_girls = cl
        max_girls = girls

print(f'Больше всего мальчиков в классе {more_boys["class"]}')
print(f'Больше всего девочек в классе {more_girls["class"]}')
