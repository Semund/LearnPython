"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def check_strings(string_1, string_2):
    if not (isinstance(string_1, str) and isinstance(string_2, str)):
        return 0
    if string_1 == string_2:
        return 1
    elif len(string_1) > len(string_2):
        return 2
    elif string_2 == 'learn':
        return 3


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print('Strings: abra, cadabra. Result:', check_strings('abra', 'cadabra'), end='\n_______\n')
    print('Strings: cadabra, abra. Result:', check_strings('cadabra', 'abra'), end='\n_______\n')
    print('Strings: equal, equal. Result:', check_strings('equal', 'equal'), end='\n_______\n')
    print('Strings: word, 1. Result:', check_strings('word', 1), end='\n_______\n')
    print('Strings: learn, python. Result:', check_strings('learn', 'python'), end='\n_______\n')
    print('Strings: python the best, learn. Result:', check_strings('python the best', 'learn'), end='\n_______\n')
    print('Strings: abra, learn. Result:', check_strings('abra', 'learn'), end='\n_______\n')


if __name__ == "__main__":
    main()
