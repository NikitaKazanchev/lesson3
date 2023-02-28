"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

# 1. Вывести названия всех отделов
for department in departments:
    print(department["title"])
    

# 2. Вывести имена всех сотрудников компании.
for department in departments:
    for name in department["employers"]:
        print(name["first_name"])

# 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
for department in departments:
    for name in department["employers"]:
        print( name["first_name"], department["title"])
    


# 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
for department in departments:
    for name in department["employers"]:
        if name["salary_rub"] > 100000:
            print(name["first_name"])
    

# 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
for department in departments:
    for name in department["employers"]:
        if name["salary_rub"] < 80000:
            print(name["position"])


# 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
for department in departments:
    total_salary = 0
    for name in department["employers"]:
        total_salary += name["salary_rub"]
    print(department["title"], total_salary)


# 7. Вывести названия отделов с указанием минимальной зарплаты в нём.
for department in departments:
    salaries = []
    for name in department["employers"]:
        salaries.append(name["salary_rub"])
    print(f'Минимальной зарплаты {department["title"]} {min(salaries)}')


# 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
for department in departments:
    salaries = []
    sum_money = 0
    for name in department["employers"]:
        salaries.append(name["salary_rub"])
        sum_money += name["salary_rub"]
    min_wage = min(salaries)
    max_wage = max(salaries)
    average_salary = sum_money / len(department["employers"])
    print(f'{department["title"]} минимальная {min_wage}, среднаяя {average_salary}, максимальная {max_wage}, зарплаты.')


# 9. Вывести среднюю зарплату по всей компании.
sum_money = 0
total_employees = 0
for department in departments:
    for name in department["employers"]:
        sum_money += name["salary_rub"]
        total_employees += 1
print(f'{sum_money / total_employees} средняя зарплата по всей компании')


# 10. Вывести названия должностей, которые получают больше 90к без повторений.
positions = []
for department in departments:
    for name in department["employers"]:
        if name["salary_rub"] > 90000:
            positions.append(name["position"])
print(' '.join(set(positions)))


# 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
girls = {"Michelle", "Nicole", "Christina", "Caitlin"}
for department in departments:
    average_salary = []
    for name in department["employers"]:
        if name["first_name"] in girls:
            average_salary.append(name["salary_rub"])
    average_salary_girls = round(sum(average_salary)/len(average_salary), 2)      
    print(f'Средняя зарплата девушек {department["title"]} {average_salary_girls}')


# 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
vowels = set("aeiouy")
employee_name = []
for department in departments:
    for name in department["employers"]:
        if name["last_name"][-1] in vowels:
            employee_name.append(name["first_name"])
print("Люди, чьи фамилии заканчиваются на гласную букву", ' '.join(employee_name))


vowels = ("a", "e", "i", "o", "u", "y")
employee_name = []
for department in departments:
    for name in department["employers"]:
        employee_name.append(name["last_name"])
        string_of_surnames = ' '.join(employee_name)
        if string_of_surnames.endswith(vowels):
            print("Человек, чья фамилия заканчиваются на гласную букву", name["first_name"])