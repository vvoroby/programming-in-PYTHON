def read():
    file = open("students.txt", "r", encoding="utf8")
    lst = file.readlines()
    file.close()
    return lst

def write(lst):
    lst.sort()
    file = open("students.txt", "w", encoding="utf8")
    for student in lst:
        file.write(student)
    file.close()

def add(surname, name):
    lst = read()
    student = surname + ' ' + name + '\n'
    if student in lst:
        return f"Студент уже есть в списке"
    else:
        lst.append(student)
        write(lst)
        return f"Студент добавлен"


def find(surname, name=""):
    lst = read()
    new = []
    for student in lst:
        if name == "":
            if surname in student:
                new.append(student)
        elif surname in student:
            if name in student:
                return f'Студент в группе'
            else:
                return f'Студента нет в группе'
    if len(new) > 0:
        return [print(item) for item in new]
    else:
        return f'Студенты с данной фамилией не найдены'


def edit(surname, name, new_surname="", new_name=""):
    lst = read()
    for student in lst:
        if surname in student:
            if name in student:
                index = lst.index(surname + " " + name + "\n")
                if new_surname != "":
                    surname = new_surname
                if new_name != "":
                    name = new_name
                lst[index] = surname + " " + name + "\n"
                lst.sort()
                write(lst)
                return f"Данные изменены"
    return f'Студент не найден'

def delete(surname, name = ""):
    lst = read()
    if name == "":
        for student in lst:
            if surname in student:
                print("Список студентов:")
                for student in lst:
                    if surname in student:
                        print(student)
                name = input("Введите имя студента: ")
                for student in lst:
                    if name in student:
                        lst.remove(student)
                        write(lst)
                        return f"Студент удален"
    elif name != "":
        for student in lst:
            if surname in student:
                if name in student:
                    lst.remove(student)
                    write(lst)
                    return f"Студент удален"
    return f"Студент не найден"


print('Чтобы увидеть перечень всех команд введите help')
vvod = input("Введите команду: ")

while input != "exit":
    if vvod == "help":
        print('''exit - выйти
add - добавить нового студента
find - найти студента
edit - редактировать информацию о студенте
delete - удалить студента''')

    if vvod == "add":
        surname = input("Введите фамилию студента: ")
        name = input("Введите имя студента: ")
        print(add(surname, name))

    if vvod == "find":
        surname = input("Введите фамилию студента: ")
        name = input("Введите имя студента или ENTER: ")
        print(find(surname, name))

    if vvod == "edit":
        surname = input("Введите фамилию студента: ")
        name = input("Введите имя студента: ")
        new_surname = input("Введите новую фамилию студента или ENTER: ")
        new_name = input("Введите новое имя студента или ENTER: ")
        print(edit(surname, name, new_surname, new_name))

    if vvod == "delete":
        surname = input("Введите фамилию студента: ")
        name = input("Введите имя студента или ENTER: ")
        print(delete(surname, name))

    vvod = input("Введите команду: ")
