#Лабораторная работа №1
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

def tec_doc():
    print('Текущий список документов:')
    for item in documents:
        print(f"№: {item['number']}, тип: {item['type']}, владелец: {item['name']}, {s(item['number'])}")

def p(num_p):
    for item in documents:
        if item['number'] == num_p:
            return item['name']
    return str('Документ не найден в базе')

def s(num_s):
    for item in directories:
        if num_s in directories[item]:
            return str('Документ хранится на полке:' + item)
    return str('Документ не найден в базе')

def l():
    for item in documents:
        print(f"№: {item['number']}, тип: {item['type']}, владелец: {item['name']}")

def ads(new_polka):
    if new_polka not in directories.keys():
        directories[new_polka] = {}
        return print('Полка добавлена. Текущий перечень полок: ', list(directories.keys()))
    else:
        return print('Такая полка уже существует. Текущий перечень полок: ', list(directories.keys()), sep=",")

def ds(num_ds):
    if num_ds in directories.keys():
        if len(directories[num_ds]) == 0:
            del directories[num_ds]
            return print('Полка удалена. Текущий перечень полок: ', list(directories.keys()))
        elif len(directories[num_ds]) != 0:
            return print('На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: ', list(directories.keys()))
    else:
        return print('Такой полки не существует. Текущий перечень полок: ', list(directories.keys()))

def ad(number_ad, type_ad, name_ad, num_polka):
    if num_polka in directories.keys():
        documents.append({'type': type_ad, 'number': number_ad, 'name': name_ad})
        directories[num_polka] = ['number_ad']
        print('Документ добавлен')
        tec_doc()
    else:
        print('Такой полки не существует. Добавьте полку командой ads. ')
        tec_doc()

def d(number_d):
    for item in documents:
        if item['number'] == number_d:
            del item
            return str('Результат: Документ удален.')
    return str('Результат: Документ не найден в базе.')

def m(number_m, polka_m):
    if polka_m in directories.keys():
        for item in directories:
            if number_m in directories[item]:
                directories[item].remove(number_m)
                directories[polka_m].append(number_m)
                return (f'Результат: Документ перемещен. {tec_doc()}')
        return (f'Результат: Документ не найден в базе. {tec_doc()}')
    else:
        return (f'Такой полки не существует. Текущий перечень полок: {list(directories.keys())}')


vvod = input('Введите команду: ')
while vvod != 'q':
    if vvod == 'p':
        num_p = input('Введите номер документа: ')
        print('Результат: ' + p(num_p))

    if vvod == 's':
        num_s = input('Введите номер документа: ')
        print('Результат: ' + s(num_s))

    if vvod == 'l':
        l()

    if vvod == 'ads':
        new_polka = input('Введите номер полки: ')
        ads(new_polka)

    if vvod == 'ds':
        num_ds = input('Введите номер полки: ')
        ds(num_ds)

    if vvod == 'ad':
        number_ad = input('Введите номер документа: ')
        type_ad = input('Введите тип документа: ')
        name_ad = input('Введите владельца документа: ')
        num_polka = input('Введите полку для хранения: ')
        ad(number_ad, type_ad, name_ad, num_polka)

    if vvod == 'd':
        number_d = input('Введите номер документа:')
        print(d(number_d))
        tec_doc()

    if vvod == 'm':
        number_m = input('Введите номер документа:')
        polka_m = input('Введите номер полки:')
        print(m(number_m, polka_m))

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
