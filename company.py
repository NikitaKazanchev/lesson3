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
# total_taxes_when_None = {}
# total_tax_in_case_of_a_match = {}
# departments_of_the_organization = []
# for department in departments:
#     total_salary = 0
#     departments_of_the_organization.append(department['title'])
#     for name in department["employers"]:
#         total_salary += name["salary_rub"]
        
#     for tax in taxes:
#         if tax["department"] is None:
#             total_taxes_when_None[department["title"]] = total_salary * tax['value_percents'] / 100
#         elif tax['department'] in departments_of_the_organization:
#             total_tax_in_case_of_a_match[department["title"]] = total_salary * tax['value_percents'] / 100
    
# for department_name, total_tax in total_taxes_when_None.items():
#     if department_name in total_tax_in_case_of_a_match:
#         total_tax_in_case_of_a_match[department_name] += total_tax
# print(f'Cуммарным налогом {total_tax_in_case_of_a_match}')
# print(f'Cуммарным налогом {total_taxes_when_None}')
    

# #14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.

# departments_of_the_organization = []
# tax_in_case_of_a_match = {}
# for department in departments:
#     departments_of_the_organization.append(department['title'])
#     taxes_when_None = {}
#     employee_salaries = {}
#     for name in department["employers"]:
#         employee_salaries[name['first_name']] = name['salary_rub']
        
#         for tax in taxes:
#             if tax["department"] is None:
#                 taxes_when_None[name['first_name']] = name['salary_rub'] - name['salary_rub'] * (tax['value_percents'] / 100)
#             elif tax['department'] in departments_of_the_organization:
#                 tax_in_case_of_a_match[name['first_name']] = name['salary_rub'] - name['salary_rub'] * (tax['value_percents'] / 100)
#     print(f'Pарплаты с учётом налогов {department["title"]} {taxes_when_None}')
            
#     for department_name, total_tax in taxes_when_None.items():
#         if department_name in tax_in_case_of_a_match:
#             tax_in_case_of_a_match[department_name] += total_tax
        
#     for department_name, total_tax in employee_salaries.items():
#         if department_name in tax_in_case_of_a_match:
#             tax_in_case_of_a_match[department_name] -= total_tax

# print(f'Pарплаты с учётом налогов {department["title"]} {tax_in_case_of_a_match}')
       
    
#16. Вывести список отделов, отсортированный по месячной налоговой нагрузки.   

#17. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
departments_of_the_organization = []
tax_in_case_of_a_match = {}
for department in departments:
    departments_of_the_organization.append(department['title'])
    taxes_when_None = {}
    employee_salaries = {}
    for name in department["employers"]:
        employee_salaries[name['first_name']] = name['salary_rub']
        
        for tax in taxes:
            if tax["department"] is None:
                taxes_when_None[name['first_name']] = (name['salary_rub'] * (tax['value_percents'] / 100)) * 12
            elif tax['department'] in departments_of_the_organization:
                tax_in_case_of_a_match[name['first_name']] = (name['salary_rub'] * (tax['value_percents'] / 100)) * 12
        
    for employee_name, total_tax in taxes_when_None.items():
        if total_tax > 100000:
            print(f'Сотрудник {department["title"]} за которого платят больше 100к налогов: {employee_name} - {total_tax}')
                  
    for employee_name, total_tax in taxes_when_None.items():
        if employee_name in tax_in_case_of_a_match:
            tax_in_case_of_a_match[employee_name] += total_tax
    
    for employee_name, total_tax in tax_in_case_of_a_match.items():
        if total_tax > 100000:
            print(f'Сотрудник {department["title"]} за которого платят больше 100к налогов: {employee_name} - {total_tax}')
        
        
#18. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.

departments_of_the_organization = []
tax_in_case_of_a_match = {}
for department in departments:
    departments_of_the_organization.append(department['title'])
    taxes_when_None = {}
    employee_salaries = {}
    for name in department["employers"]:
        employee_salaries[name['first_name']] = name['salary_rub']
        
        for tax in taxes:
            if tax["department"] is None:
                taxes_when_None[name['first_name']] = name['salary_rub'] * (tax['value_percents'] / 100)
            elif tax['department'] in departments_of_the_organization:
                tax_in_case_of_a_match[name['first_name']] = name['salary_rub'] * (tax['value_percents'] / 100)
    
    min_tax_when_None =  min(taxes_when_None)
    worker_when_None = {}
    for worker_min_tax in min_tax_when_None:
        if worker_min_tax in name['first_name']:
            worker_when_None[name['first_name']] = name['last_name']
    print(f'{worker_when_None} c меньшим налогов в компании из {department["title"]}')


    for employee_name, total_tax in taxes_when_None.items():
        if employee_name in tax_in_case_of_a_match:
            tax_in_case_of_a_match[employee_name] += total_tax

min_tax_in_case_of_a_match = min(tax_in_case_of_a_match)
worker_tax_in_case_of_a_match = {}
for worker_min_tax in min_tax_in_case_of_a_match:
    if worker_min_tax in name['first_name']:
        worker_tax_in_case_of_a_match[name['first_name']] = name['last_name']
print(f'{worker_tax_in_case_of_a_match} c меньшим налогов в компании из {department["title"]}')   