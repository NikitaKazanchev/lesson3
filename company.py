"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
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


for department in departments:
    print(department["title"])
    

for department in departments:
    for name in department["employers"]:
        print(name["first_name"])


for department in departments:
    employee_position = {}
    for name in department["employers"]:
        employee_position[name["first_name"]] = department["title"]
    print(employee_position)


for department in departments:
    big_salary = []
    for name in department["employers"]:
        if name["salary_rub"] > 100000:
            big_salary.append(name["first_name"])
    print(big_salary)    
    
# Вариант 1
for department in departments:
    a_small_salary = []
    for name in department["employers"]:
        if name["salary_rub"] < 80000:
            a_small_salary.append(name["position"])
    print(a_small_salary)

# Вариант 2
for department in departments:
    for name in department["employers"]:
        if name["salary_rub"] < 80000:
            print(name["position"])


for department in departments:
    sum_maney = 0
    for name in department["employers"]:
        sum_maney += name["salary_rub"]
    print(department["title"], sum_maney)