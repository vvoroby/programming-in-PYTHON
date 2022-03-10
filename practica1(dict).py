#задание 2
students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
grades = {"Вася" : 4, "Петя" : 9, "Марина" : 8, "Люба" : 4, "Коля" : 5, "Ваня": 10}

for item in students:
    if item in grades:
        print(item, grades[item])
    else:
        print(item + " контрольную работу не писал(а)")

for item in students:
    if grades.get(item, 0) >= 8:
        print(item)

good, bad = [], []
for item in students:
    if grades.get(item, 0) >= 6:
        good.append(item)
    else:
        bad.append(item)
print(good, bad)

#задание 3
def sr_ball(marks, x):
    sum_ = 0
    for i in marks.values():
        sum_ += i[x-1]
    return round(sum_ / len(marks.keys()))

marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}
x = int(input('введите курс: '))
print(f'Курс {x} - {sr_ball(marks, x)}')

#заданрие 4
categories = {'отлично' : [8, 9, 10],
             'хорошо' : [6, 7],
             'удовлетворительно' : [4, 5],
             'неуд' : [0, 1, 2, 3]}

for item in categories:
    if sr_ball(marks, x) in categories[item]:
        print(f'Курс {x} - {item}')

#задание 5
count = 0
y = int(input('введите оценку: '))
for i in marks.values():
    for j in i:
        if j >= y:
            count += 1
print(count)

#задание 34
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

count2 = count3 = 0
for item in queries:
    if item.count(' ') == 1:
        count2 += 1
    if item.count(' ') == 2:
        count3 += 1
print(f'Поисковых запросов, содержащих 2 слов(а): {round(count2 / len(queries) * 100, 2)}%')
print(f'Поисковых запросов, содержащих 3 слов(а): {round(count3 / len(queries) * 100, 2)}%')

#задание 35
results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}
for item in results:
    results[item]['ROI'] = {round((results[item]['revenue'] / results[item]['cost'] - 1) * 100, 2)}
print(results)
