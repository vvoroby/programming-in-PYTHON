class Hotel:

    #словарь для хранения различных типов номеров (SGL, DBL и Junior Suite, Suite) и их занятости
    def __init__(self, num_rooms_SGL, num_rooms_DBL, num_rooms_JuniorSuite, num_rooms_Suite):
        self._rooms = dict()
        self._rooms['SGL'] = [[0 for _ in range(num_rooms_SGL)], 1000]
        self._rooms['DBL'] = [[0 for _ in range(num_rooms_DBL)], 2000]
        self._rooms['Junior Suite'] = [[0 for _ in range(num_rooms_JuniorSuite)], 3000]
        self._rooms['Suite'] = [[0 for _ in range(num_rooms_Suite)], 4000]

    # метод для бронирования номера по уникальному значению в списке
    def occypy(self, room_type, room_id):
        if self._rooms[room_type][0][room_id-1] == 0:
            self._rooms[room_type][0][room_id-1] = 1  # бронируем номер
        else:
            raise RuntimeError("Номер занят")

    # метод для освобождения номера по уникальному значению в списке
    def free(self, room_type, room_id):
        self._rooms[room_type][0][room_id-1] = 0  # освобождаем номер

    # метод для красивой печати списка номеров через вызов функции print
    def __str__(self):
        a = ''
        for item in self._rooms:
            for j in range(len(self._rooms[item][0])):
                if self._rooms[item][0][j] == 0:
                    a += 'Тип ' + item + ' Номер ' + str(j + 1) + " свободен\n"
                else:
                    a += 'Тип ' + item + ' Номер ' + str(j + 1) + " занят\n"
        return a

    # метод, который занимает все свободные номера в отеле
    def all_occypy(self):
        for item in self._rooms:
            for j in range(len(self._rooms[item][0])):
                self._rooms[item][0][j] = 1

    # метод, который возвращает долю занятых номеров
    def procent_occypy(self):
        count_occypy = 0
        count_all = 0
        for item in self._rooms:
            for j in range(len(self._rooms[item][0])):
                count_all += 1
                if self._rooms[item][0][j] == 1:
                    count_occypy += 1
        return f'{round(count_occypy/count_all, 2)}%'

    # метод, который освобождает все занятые номера отеля
    def all_free(self):
        for item in self._rooms:
            for j in range(len(self._rooms[item][0])):
                if self._rooms[item][0][j] == 1:
                    self._rooms[item][0][j] = 0

    # метод, который возвращает выручку, исходя из занятости комнат (стоимость комнаты - 5 тыс. у.е.)
    def profit(self):
        sum = 0
        for item in self._rooms:
            for j in range(len(self._rooms[item][0])):
                if self._rooms[item][0][j] == 1:
                    sum += self._rooms[item][1]
        return sum


hotel = Hotel(5,5,3,3) # в нашем отеле, например, 5 номеров категории SGL и DBL и по 3 номера других категорий
print(hotel._rooms)  # смотрим номера через атрибут self.rooms
print()

hotel.occypy("SGL", 4) # бронируем номера
hotel.occypy("DBL", 3)
hotel.occypy("Suite", 1)
print(hotel) # выводим информацию о состоянии всех номеров
print(hotel.profit()) # смотрим выручку
print(hotel.procent_occypy()) # смотрим долю занятых номеров
print()

hotel.free("DBL", 3) # освобождаем номер
print(hotel) # выводим информацию о состоянии всех номеров
print(hotel.profit()) # смотрим выручку
print(hotel.procent_occypy()) # смотрим долю занятых номеров
print()

hotel.all_free() # освобождаем все номера
print(hotel.profit()) # смотрим выручку
print(hotel.procent_occypy()) # смотрим долю занятых номеров
print()

hotel.all_occypy() # занимаем все номера
print(hotel.profit()) # смотрим выручку
print(hotel.procent_occypy()) # смотрим долю занятых номеров
