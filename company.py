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

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов с суммарным налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов с указанием месячной налоговой нагрузки – количеством денег, которые в месяц этот отдел платит налогами.
16. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
17. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
18. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
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

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

# # 1. Вывести названия всех отделов
# for department in departments:
#     print(department["title"])
    

# # 2. Вывести имена всех сотрудников компании.
# for department in departments:
#     for name in department["employers"]:
#         print(name["first_name"])

# # 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
# for department in departments:
#     for name in department["employers"]:
#         print(name["first_name"], department["title"])
    


# # 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
# for department in departments:
#     for name in department["employers"]:
#         if name["salary_rub"] > 100000:
#             print(name["first_name"])
    

# # 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
# for department in departments:
#     for name in department["employers"]:
#         if name["salary_rub"] < 80000:
#             print(name["position"])


# # 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
# for department in departments:
#     total_salary = 0
#     for name in department["employers"]:
#         total_salary += name["salary_rub"]
#     print(department["title"], total_salary)


# # 7. Вывести названия отделов с указанием минимальной зарплаты в нём.
# for department in departments:
#     salaries = []
#     for name in department["employers"]:
#         salaries.append(name["salary_rub"])
#     print(f'Минимальной зарплаты {department["title"]} {min(salaries)}')


# # 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
# for department in departments:
#     salaries = []
#     for name in department["employers"]:
#         salaries.append(name["salary_rub"])
#     min_wage = min(salaries)
#     max_wage = max(salaries)
#     average_salary = sum(salaries) / len(department["employers"])
#     print(f'{department["title"]} минимальная {min_wage}, среднаяя {average_salary}, максимальная {max_wage}, зарплаты.')


# # 9. Вывести среднюю зарплату по всей компании.
# sum_money = 0
# total_employees = 0
# for department in departments:
#     total_employees += len(department["employers"])
#     for name in department["employers"]:
#         sum_money += name["salary_rub"]
# print(f'{sum_money / total_employees} средняя зарплата по всей компании')


# # 10. Вывести названия должностей, которые получают больше 90к без повторений.
# positions = []
# for department in departments:
#     for name in department["employers"]:
#         if name["salary_rub"] > 90000:
#             positions.append(name["position"])
# print(' '.join(set(positions)))


# # 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
# girls = {"Michelle", "Nicole", "Christina", "Caitlin"}
# for department in departments:
#     salary_girls = []
#     for name in department["employers"]:
#         if name["first_name"] in girls:
#             salary_girls.append(name["salary_rub"])
#     average_salary_girls = round(sum(salary_girls) / len(salary_girls), 2)
#     print(f'Средняя зарплата девушек {department["title"]} {average_salary_girls}')


# # 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
# vowels = set("aeiouy")
# employee_name = []
# for department in departments:
#     for name in department["employers"]:
#         if name["last_name"][-1] in vowels:
#             employee_name.append(name["first_name"])
# print("Люди, чьи фамилии заканчиваются на гласную букву", ' '.join(set(employee_name)))


# 13. Вывести список отделов с суммарным налогом на сотрудников этого отдела.
for department in departments:
    tax_interest = 0
    for tax in taxes:
        if tax['department'] is None or tax['department'] == department['title']:
            tax_interest += tax['value_percents']
    
    total_salary = 0
    for name in department['employers']:
        total_salary += name["salary_rub"]
        
    total_tax = total_salary * tax_interest // 100     
    print(f'Суммарный налог на {department["title"]}: {total_tax}') 
    
    
#14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
for department in departments:
    salary_including_taxes = {}
    tax_interest = 0
    for tax in taxes:
        if tax['department'] is None or tax['department'] == department['title']:
            tax_interest += tax['value_percents']
    for name in department['employers']:
        salary_including_taxes[name['first_name']] = name['salary_rub'] - (name['salary_rub'] * tax_interest // 100)
    print(f'Зарплаты с учётом налогов {department["title"]} {salary_including_taxes}')
      
    
# #16. Вывести список отделов, отсортированный по месячной налоговой нагрузки.   
department_total_taxes = {}
for department in departments:
    tax_interest = 0
    for tax in taxes:
        if tax['department'] is None or tax['department'] == department['title']:
            tax_interest += tax['value_percents']

    for name in department['employers']:
        department_total_taxes[department['title']] = name['salary_rub'] * tax_interest // 100
    
departments_names_by_total_taxes = sorted(
    department_total_taxes,
    key=department_total_taxes.get,
    reverse=True,
)

for department_name in departments_names_by_total_taxes:
    print(department_name)
    
# #17. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
for department in departments:
    salary_including_taxes = {}
    tax_interest = 0
    for tax in taxes:
        if tax['department'] is None or tax['department'] == department['title']:
            tax_interest += tax['value_percents']
    for name in department['employers']:
        salary_including_taxes[name['first_name']] = name['salary_rub'] * tax_interest // 100 * 12
        
    for employee_name, total_tax in salary_including_taxes.items():
        if total_tax > 100000:
            print(f'Сотрудник {employee_name} {department["title"]} за которого платят больше 100к налогов в год - {total_tax}')
        
        
# #18. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
for department in departments:
    salary_including_taxes = {}
    tax_interest = 0
    for tax in taxes:
        if tax['department'] is None or tax['department'] == department['title']:
            tax_interest += tax['value_percents']
    for name in department['employers']:
        salary_including_taxes[name['first_name']] = name['salary_rub'] * tax_interest // 100
    
        
    min_salary_including_taxes = min(salary_including_taxes.items(), key=lambda item: item[1])
    print(f'{min_salary_including_taxes} c меньшим налогов в компании из {department["title"]}') 