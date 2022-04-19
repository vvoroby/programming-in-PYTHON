import json

flag = True
name_file = input("Введите имя файла формата .json : ")
try:
    with open(name_file, "r", encoding='utf-8') as file:
        todo_list = json.load(file)
except:
    print("Файл не найден.")
    flag = False

while (flag):
    print(f"""Простой todo:
 1. Добавить задачу.
 2. Вывести весь список текущих задач.
 3. Выход.""")
    vvod = input("Укажите число: ")

    if vvod == "1":
        task = input("Сформулируйте задачу: ")
        category = input("Добавьте категорию к задаче: ")
        time = input("Добавьте время к задаче: ")
        with open(name_file, "w", encoding='utf-8') as file:
            todo_list.append({"task": task, "category": category, "time": time})
            json.dump(todo_list, file)

    if vvod == "2":
        for item in todo_list:
            print(item)

    if vvod == "3":
        print("Задачи сохранены в файл!")
        file.close()
        flag = False
