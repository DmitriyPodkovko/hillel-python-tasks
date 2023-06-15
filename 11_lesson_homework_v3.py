# Les11_Hw by Podkovko Dmitriy

# Модифицировать функцию input_int следуюим образом:
# добавить возможность задавать количество попыток ввода
# (передать в функцию необязательный аргумент, отвечающий за количество попыток).
# Если аргумент передан - за паршивть указанное количество раз и сообщать об оставшемся количестве попыток,
# если не передан - запрашивать бесконечно.
# 1* (необязательное) Добавить вопрос о желании пользователя подолжать выполнение программы.
# После неправильного ввода числа спросить, хочет ли пользователь продолжить выполнение (Y/N),
# обработать оба варианта, а также добиться павильного ввода ответа (после неправильного - переспросить).


def input_int(counter=None):
    while True:
        if counter == 0:
            print('Attempts Ended!!!')
            return
        try:
            if counter: return int(input(f'Enter int. You have {str(counter)} attempts: '))
            else: return int(input('Enter int: '))
        except Exception as e:
            if counter is not None: counter -= 1
            if counter != 0:
                print('Wrong! Try again')
                while True:
                    answer = input('Keep trying? Enter Y or N: ').upper()
                    if answer == 'Y': break
                    elif answer == 'N':
                        print('Bye!')
                        return


print(input_int(3))

# Написать парсер строки, сожержащей email (проверить, является ли переданная строка email-ом).
#  Проверки:
#  - наличие не более одного символа '@' строке, символ не в начале и не в конце
#  - длина имени email-а (то что до @) не менее 3 символа, не более 64 символа
#  - домен email-а (то что после @) содержит точку (".")
#  - первая часть домена не менее 1 не более 10, вторая часть не менее 2 не более 10


def is_valid_mail(mail):
    s = mail
    if s.count('@') == 1:
        n = s.find('@')
        s1 = s[:n]
        s2 = s[n + 1:]
        if 2 < len(s1) < 65 and s2.count('.') == 1:  # + дополнительно проверили, чтоб точка была одна
            m = s2.find('.')
            s3 = s2[:m]
            s4 = s2[m + 1:]
            if 0 < len(s3) < 11 and 1 < len(s4) < 11:
                return True


print(is_valid_mail(input('Enter mail: ')))