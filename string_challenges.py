# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
word = word.lower()
print(f'Количество букв "а": {word.count("а")}')


# Вывести количество гласных букв в слове
word = 'Архангельск'
word = word.lower()
count = 0
vowels = ('а', 'е', 'и', 'о', 'у', 'ё', 'ю', 'я')
for letter in word:
    if letter in vowels:
        count += 1
print(f"Количество гласных равно: {count}")


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
count = 0
for letter in sentence.split():
    count += 1
print(f"Количество слов в предложении: {count}")


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for letter in sentence.split():
    print(letter[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
count = 0
count1 = 0
for letter in sentence.split():
    count += len(letter)
    count1 += 1
print(count/count1)