"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import random
import csv


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    jobs = ('Music teacher', 'Architect', 'Engineer', 'Dancer', 'Programmer', 'Cook', 'Policeman')
    names = ('Julia', 'Ivan', 'John', 'Caty', 'Anne', 'Josef', 'Margo', 'Tim')

    person_jobs = [{'name': random.choice(names),
                    'job': random.choice(jobs),
                    'age': random.randint(24, 65)} for _ in range(30)]

    with open('person_jobs.csv', 'w', encoding='utf8') as csvfile:
        fieldnames = ['name', 'job', 'age']
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(person_jobs)


if __name__ == "__main__":
    main()
