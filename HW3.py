# # Task 1
import random
#
# random_int = random.randint(1, 10)
# while True:
#     my_int = int(input('Введите целое число от 1 до 10: '))
#     if my_int == random_int:
#         print(f'Верно! Это {random_int}')
#         break
#     else:
#         print('Число меньше загаданного' if my_int < random_int else 'Число больше загаданного')
#         print('Попробуйте еще раз')

# Task 2
def random_password () -> str:
    my_password = ''
    len_password = random.randint(7, 10)
    for i in range(len_password):
        my_password = my_password + chr(random.randint(33, 126))
    return my_password

# print(random_password())

# Task 3
def check_password (password: str) -> bool:
    count_upper = count_lower = count_digit = 0
    if len(password) > 7:
        for i in range(len(password)):
            if password[i].isupper():
                count_upper += 1
            elif password[i].islower():
                count_lower += 1
            elif password[i].isdigit():
                count_digit += 1
        if count_lower > 0 and count_upper > 0 and count_digit > 0:
            return True
        else:
            return False
    else:
        return False
# print(check_password(input('Введите пароль: ')))

# Task 4
def generator () -> str:
    new_password = ''
    attempt = 0
    while check_password(new_password) == False:
        new_password = random_password()
        attempt += 1
    return (f'Новый пароль: {new_password} \nПопытка номер {attempt}')

print(generator())