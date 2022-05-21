# Вывести последнюю букву в слове
import re

word = 'Архангельск'
print('=============\n#1')
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'

print('=============\n#2')
print(word.lower().count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
print('=============\n#3')
print(len([letter for letter in word.lower() if letter in ('а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')]))

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print('=============\n#4')
# print(len(sentence.split()))
print(len(re.findall(r'\w+', sentence)))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print('=============\n#5')
words = re.findall(r'\w+', sentence)
for word in words:
    print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print('=============\n#6')
words = re.findall(r'\w+', sentence)
print(sum((len(w) for w in words)) / len(words))