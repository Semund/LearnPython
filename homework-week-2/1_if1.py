"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    answer = ''
    try:
        user_age = int(input('Input your age: '))
    except ValueError:
        answer = 'You must enter an integer number'
    else:
        if user_age > 23:
            answer = 'You must working'
        elif user_age > 17:
            answer = 'You must be a student'
        elif user_age > 6:
            answer = 'You must go to school'
        else:
            answer = 'Go to kindergarten'
    finally:
        print(answer)


if __name__ == "__main__":
    main()
