"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
import re


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf8') as f:
        input_text = f.read()

    print('#2 Длина текста:', len(input_text))

    print('#3 Количество слов в тексте:', len(re.findall(r'\w+', input_text)))

    with open('referat2.txt', 'w', encoding='utf8') as f:
        f.write(input_text.replace('.', '!'))


if __name__ == "__main__":
    main()
