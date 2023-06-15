# Les11_Hw by Podkovko Dmitriy

# Модифицировать функцию input_int следуюим образом:
# добавить возможность задавать количество попыток ввода
# (передать в функцию необязательный аргумент, отвечающий за количество попыток).
# Если аргумент передан - за паршивть указанное количество раз и сообщать об оставшемся количестве попыток,
# если не передан - запрашивать бесконечно.
# 1* (необязательное) Добавить вопрос о желании пользователя подолжать выполнение программы.
# После неправильного ввода числа спросить, хочет ли пользователь продолжить выполнение (Y/N),
# обработать оба варианта, а также добиться павильного ввода ответа (после неправильного - переспросить).

from tkinter import messagebox as mb


def input_int(counter=0):
    if counter:
        while counter >= 0:
            try:
                if counter == 0:
                    return print('Attempts Ended!!!')
                return int(input('Enter int. You have ' + str(counter) + ' attempts: '))
            except Exception as e:
                counter -= 1
                if counter != 0:
                    print('Wrong! Try again')
                    answer = mb.askyesno(message="Keep trying?")
                    if answer: continue
                    else: return print('Bye!')

    else:
        while True:
            try:
                return int(input('Enter int: '))
            except Exception as e:
                print('Wrong! Try again')
                answer = mb.askyesno(message="Keep trying?")
                if answer: continue
                else: return print('Bye!')


print(input_int(3))

# Написать парсер строки, сожержащей email (проверить, является ли переданная строка email-ом).
#  Проверки:
#  - наличие не более одного символа '@' строке, символ не в начале и не в конце
#  - длина имени email-а (то что до @) не менее 3 символа, не более 64 символа
#  - домен email-а (то что после @) содержит точку (".")
#  - первая часть домена не менее 1 не более 10, вторая часть не менее 2 не более 10


def is_valid_mail(mail):
    result = False
    s = mail.strip() # избавляемся от пробелов в начале и в конце строки
    s = mail.replace(" ", "") # вместо strip, если пользователь совсем тупой и вводит пробелы в середине
    if s.count("@") == 1:
        if 2 < len(s[:s.find("@")]) < 65:
            if s[s.find("@") + 1:].count(".") == 1: # + дополнительно проверили, чтоб точка была одна
                if 0 < len(s[s.find("@") + 1:s.find(".")]) < 11:
                    if 1 < len(s[s.find(".") + 1:]) < 11:
                        result = True
    return result


print(is_valid_mail(input("Enter mail: ")))
