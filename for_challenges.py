names = ['Оля', 'Петя', 'Вася', 'Маша']
for names_list in names:
    print(names_list)



names = ['Оля', 'Петя', 'Вася', 'Маша']
for names_list in names:
    print(f"{names_list}: {len(names_list)}")



is_male = {
    'Оля': False,  
    'Петя': True,  
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in names:
    if is_male[name]:
        print("пол мужской")
    else:
        print("пол женский")   


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]

print(f"Всего {len(groups)} группы")
for index, value in enumerate(groups, 1):
    print(f"Группа {index}: {len(value)} ученика")

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]

for index, value in enumerate(groups,1):
    students = ", ".join(value)
    print(f"Группа {index}: {students}")