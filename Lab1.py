#Лабораторная работа №1
from pprint import pprint

print('Чтобы увидеть перечень всех команд введите help')
documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

def polki_now():
    return list(directories.keys()) #print(*list(directories.keys()), sep=",")

def p(num_p):
    for item in documents:
        if item['number'] == num_p:
            return f'Владелец документа: {item["name"]}'
    return f'Документ не найден в базе'

def s(num_s):
    for item in directories:
        if num_s in directories[item]:
            return f'Полка хранения: {item}'
    return f'Документ не найден в базе'

def l():
    info = []
    for item in documents:
        info.append(f"№: {item['number']}, тип: {item['type']}, владелец: {item['name']}, {s(item['number'])}")
    return info

def ads(new_polka):
    if new_polka not in directories.keys():
        directories[new_polka] = {}
        return f'Полка добавлена. Текущий перечень полок: {polki_now()}'
    else:
        return f'Такая полка уже существует. Текущий перечень полок: {polki_now()}'

def ds(num_ds):
    if num_ds in directories.keys():
        if len(directories[num_ds]) == 0:
            del directories[num_ds]
            return f'Полка удалена. Текущий перечень полок: {polki_now()}'
        elif len(directories[num_ds]) != 0:
            return f'На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {polki_now()}'
    else:
        return f'Такой полки не существует. Текущий перечень полок: {polki_now()}'

def ad(number_ad, type_ad, name_ad, num_polka):
    if num_polka in directories.keys():
        documents.append({'type': type_ad, 'number': number_ad, 'name': name_ad})
        directories[num_polka] = [number_ad]
        return f'Документ добавлен.'
    else:
        return f'Такой полки не существует. Добавьте полку командой as.'

def d(number_d):
    for item in documents:
        if item['number'] == number_d:
            documents.remove(item)
            for item2 in directories:
                if number_d in directories[item2]:
                    directories[item2].remove(number_d)
                    return f'Документ удален.'
    return f'Документ не найден в базе.'

def m(number_m, polka_m):
    if polka_m in directories.keys():
        for item in directories:
            if number_m in directories[item]:
                directories[item].remove(number_m)
                directories[polka_m].append(number_m)
                return f'Документ перемещен. Текущий список документов: {l()}'
        return f'Документ не найден в базе. Текущий список документов: {l()}'
    else:
        return f'Такой полки не существует. Текущий перечень полок: {polki_now()}'


vvod = input('Введите команду: ')
while vvod != 'q':
    if vvod == 'p':
        num_p = input('Введите номер документа: ')
        print('Результат: ', p(num_p))

    if vvod == 's':
        num_s = input('Введите номер документа: ')
        print('Результат: ', s(num_s))

    if vvod == 'l':
        print('Результат: ')
        pprint(l())

    if vvod == 'ads':
        new_polka = input('Введите номер полки: ')
        print('Результат: ', ads(new_polka))

    if vvod == 'ds':
        num_ds = input('Введите номер полки: ')
        print('Результат: ', ds(num_ds))

    if vvod == 'ad':
        number_ad = input('Введите номер документа: ')
        type_ad = input('Введите тип документа: ')
        name_ad = input('Введите владельца документа: ')
        num_polka = input('Введите полку для хранения: ')
        print(ad(number_ad, type_ad, name_ad, num_polka))
        print('Текущий список документов:')
        pprint(l()) 

    if vvod == 'd':
        number_d = input('Введите номер документа:')
        print('Результат: ', d(number_d))
        print('Текущий список документов:')
        pprint(l())

    if vvod == 'm':
        number_m = input('Введите номер документа:')
        polka_m = input('Введите номер полки:')
        print('Результат: ', m(number_m, polka_m))

    if vvod == 'help':
        print('p - узнать владельца документа по его номеру\n'
              's - узнать на какой полке он хранится документ по его номеру\n'
              'l - увидеть полную информацию по всем документам\n'
              'ads - добавить новую полку\n'
              'ds - удалить существующую полку из данных (только если она пустая)\n'
              'ad - добавить новый документ в данные\n'
              'q - завершить работу\n'
              'd - удалить документ из данных\n'
              'm - переместить документ с полки на полку')

    vvod = input('Введите команду: ')
