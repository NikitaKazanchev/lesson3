# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = {}

for student in students:
    if student['first_name'] in names:
        names[student['first_name']] += 1
    else:
        names[student['first_name']] = 1

for index, value in names.items():
    print(f"{index}: {value}") 





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

names = {}

for student in students:
    if student['first_name'] in names:
        names[student['first_name']] += 1
    else:
        names[student['first_name']] = 1
recurring_name = max(names, key=names.get)
print(f"Самое частое имя среди учеников: {recurring_name}") 
    
    

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
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


for students in school_students:
    names = {}
    for index, value in enumerate(students):
        class_number = index
    for student in students:
        if student['first_name'] in names:
            names[student['first_name']] += 1
        else:
            names[student['first_name']] = 1
    recurring_name = max(names, key=names.get)
    print(f'Самое частое имя в классе {class_number}: {recurring_name}')
    
    
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

for classes in school:
    girls = 0
    boys = 0
    for student in classes['students']:
        if is_male[student['first_name']]:
            boys += 1
        else:
            girls +=1
    print(f"Класс {classes['class']}: девочки {girls}, мальчики {boys}")




# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '4d', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}




for classes in school:
    girls = 0
    boys = 0
    for student in classes['students']:
        if is_male[student['first_name']]:
            boys += 1
        else:
            girls +=1