# 1. Особливості python, в порівняні з іншими мовами програмування.
# Динамическая типизация данных - значение любого типа может быть назначено переменной.
# Массив может включать объекты различных типов.
# Полностью автоматическое управление памятью, что позволяет не задумываться про распределение или освобождение памяти.
# Выполнение операций осуществляется в более высоком уровне абстракций по причине архитектуры языка, -
# благодаря расширенной библиотеке кодов в Питон.
# Объединяется с написанными на С и С++ модулями.
# Легкий для обучения с нуля.
# Легко читаемый (блоки кода отделяются отступами). Это также дает преимущество по сравнению с другими языками
# легко поддерживать и обслуживать исходники написанные не ими.
# Работа с базами данными
# Создание GUI
#
# 2. Перетворення типів в python
# В Питоне легко осуществляется преобразование из одного типа данных в другой,
# с помощью методов/функций str(), int(), float(), list(), tuple()
# А также можно проверить тип с помощью type()
#
# 3. Робота з файлами в python
# Питон так же как и другие языки позволяет работать с файлами:
# Открывать их открывать закрывать, читать менять записывать копировать
# Кострукция with позволяет работать с файлом не переживая про его закрытие - делает закрытие самостоятельно
#
# 4. Описати сортування злиттям
# С помощью такого варианта список разбевается на две части, потом каждая разбивается ещё на две и т. д.
# Список разбивается пополам, пока не останутся единичные элементы.
# Соседние элементы становятся отсортированными парами.
# Потом эти пары объединяются и сортируются с другими парами.
# Этот процесс продолжается до тех пор, пока не отсортируются все элементы.
#
# Практичні питання:
# Що буде надруковано в консолі
# Будет напечатано все три приветствия 'Hello Jack' 'Hello Jill' 'Hello Bob'
#
# Выведет так:
# 1
# 2, 3, 1
# 1, 1
# 4, 1
# 1, 1, 1
# 1, 1, 1, 1

# Знайти найменше число в списку
list1 = [4, 7, 5, 3, 6, 9, 8]
print(min(list1))

# Вивести в циклі всі парні числа до 100, крім 6, 8, 86 якщо число 90 зустрінеться в
# списку то перервати його роботу


k = 100
for i in range(1, k + 1):
    if i == 90:
        break
    if i != 6 and i != 8 and i != 86:
        if i % 2 == 0:
            print(i)


# Скільки існує комбінацій пароля 4 символів,
# якщо відомо що друга цифра 4, 5 або
# 7, перша не 0, третя менша 6 а четверта більша 7

s = 0
for i in range(1, 10):
    for j in [4, 5, 7]:
        for k in range(0, 6):
            for n in range(8, 10):
                s += 1

print(s)

# За допомогою filter залишити в списку тільки парні числа
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def f1(n):
    return n % 2 == 0


print(list(filter(f1, list2)))

# Є файл з даними учнів у форматі Прізвище;ім’я;зріст
# Написати функцію що зчитує дані з файлу,
# функцію що добавляє учня до списку,
# функцію що перевіряє чи є валідним формат даних що вводить користувач,
# три функції що обчислюють
# максимальний, мінімальний і середній зріст.


def f_read(file_name):
    with open(file_name, 'r') as f:
        students = []
        for row in f.readlines():
            tmp = row.split(';')
            students.append({
                "name": tmp[1],
                "surname": tmp[0],
                "height": tmp[2].replace('\n', '')
            })
        return students


print(f_read('Students'))


def f_add(file_name, new_student):
    result = False
    with open(file_name, 'a') as f:
        for l in new_student:
            f.write(l["surname"] + ';' + l["name"] + ';' + l["height"] + '\n')
            result = True
    return result


print(f_add('Students', [{"name": "Igor", "surname": "Orlov", "height": "190"}]))


from re import compile


def is_valid_student(string):
    result = False
    pattern = compile("^[A-Za-z]+\;+[A-Za-z]+\;+[0-9]{3,3}$")
    is_valid = pattern.match(string)
    if is_valid:
        result = True
    return result


print(is_valid_student(input('''Введіть нового учня (у форматі Прізвище;ім’я;зріст): ''')))


lst_students = f_read('Students')


def max_height(students):
    lst_height = []
    for height in students:
        lst_height.append(height["height"])
    return max(lst_height)


print(max_height(lst_students))


def min_height(students):
    lst_height = []
    for height in students:
        lst_height.append(height["height"])
    return min(lst_height)


print(min_height(lst_students))


def avg_height(students):
    lst_height = []
    for height in students:
        lst_height.append(height["height"])
    return sum(map(int, lst_height))//len(lst_height)


print(avg_height(lst_students))
