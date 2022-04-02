import requests
import statistics

def task1():
    try:
        x = int(input('Введите знак: '))
        y = int(input('Введите знак: '))
        znak = input('Введите знак: ')
        assert znak in '+-/', 'Ошибка преобразования типа'
        if znak in '+':
            return int(x) + int(y)
        if znak in '-':
            return int(x) - int(y)
        if znak in '/':
            return int(x) / int(y)
    except ValueError:
        return f'Ошибка преобразования типа'
    except ZeroDivisionError:
        return f'Ошибка деления на нуль'
# print(task1())

import matplotlib.pyplot as plt
def task2():
    resp = requests.get('https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat')
    new_resp = list(map(float, resp.text.split()))
    x_coords = new_resp
    y_coords = []
    for i in range(len(new_resp)):
        y_coords.append(i)
    plt.plot(y_coords, x_coords)
    plt.show()
    print(f'{max(new_resp)}\n {min(new_resp)}\n {statistics.mean(new_resp)}\n {len(set(new_resp))}')
# print(task2())

def task3():
    file = requests.get("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/moby.txt").content.split()
    new_file = []
    for elem in file:
        new_file.append(str(elem)[2:-1].lower().replace(",", '').replace(".", '').replace("--", ''))
    with open("moby_clean.txt", "w", encoding='cp1251') as file:
        for elem in new_file:
            file.write(elem + "\n")
# print(task3())

def task4():
    with open("moby_clean.txt", "r", encoding='cp1251') as file:
        new_file = file.read().split()
        counter = {elem: new_file.count(elem) for elem in new_file}
        sorter = sorted(counter.items(), key=lambda x: x[1])[::-1]
        print(f"Самые частые слова {sorter[0:5]},\n"
              f"Cамые редкие слова {sorter[-5:]}")
# print(task4())

import random
def task5():
    answ = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/responses.txt").text.split("\n")
    ask = input("Введите вопрос: ")
    while ask != "close":
        print(random.choice(answ))
        ask = input("Введите вопрос: ")
# print(task5())

def task6():
    file = requests.get("http://dfedorov.spb.ru/python3/src/romeo.txt").text.split()
    counter = {elem: file.count(elem) for elem in file}
    sorter = sorted(counter.items(), key=lambda x: x[1])[::-1]
    print("Частота использования слов:")
    for elem in sorter:
        print(dict({elem}))
# print(task6())

def task7():
    file = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/text.txt").text
    upletter = 0
    whitespace = 0
    number = 0
    for elem in file:
        if elem == " ":
            whitespace += 1
        elif elem.isupper():
            upletter += 1
        elif elem.isdigit():
            number += 1
    print(f"Заглавных букв: {upletter} \n"
          f"Цифр: {number} \n"
          f"Пробелов: {whitespace}")
# print(task7())
