# Les2_Hw1 by Podkovko Dmytro

# a=”10”, b=”15”, a і b – це строки, обчислити b/a
a = "10"
b = "15"
print(int(b) / int(a))

# створити словник, в якому вказати основні дані про себе,
# словник має містить ключі значенням, якого є інший словник, а також масив
my_family = {
    "first_name": "Name",
    "last_name": "Surname",
    "status": "married",
    "family": {
        "wife": ["Name", "Surname"],
        "son": ["Name", "Surname"]
    },
    "hobby": ["football", "rest", "sleep"]
}
print(my_family)

# створити масив з 10 елементів і перетворити його в tuple, вивісти зріз перших трьох елементів
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = tuple(my_list)
print(type(my_list))
print(my_list[:3])

# a, b – сторони прямокутника, знайти площу прямокутника.
# Якщо a = b, використати формулу площи квадрата.
a = 20
b = 30
if a == b:
    s = a ** 2
else:
    s = a * b
print(s)

# Є три числа, знайти найменше.
a = 20
b = 10
c = 30
if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)

# Є три числа A, B, C –
# якщо вони впорядковані по зростанню,
# то до кожного з них добавити 3 і вивести їх нові значення,
# якщо ні то вивести їх протилежне число ( помножити на -1 ).
a = 10
b = 20
c = 20
if a <= b and b <= c:
    a = a + 3
    b = b + 3
    c = c + 3
    print(a)
    print(b)
    print(c)
else:
    print(a * -1)
    print(b * -1)
    print(c * -1)

# Дано три числа. Знайти суму двох найбільших з них.
a = 30
b = 20
c = 40
if a < b:
    m = a
else:
    m = b
if c < m:
    m = c
s = a + b + c - m
print(s)

# Створити невпорядкований список з 10 елементів:
# знайти найбільший, найменший елементи, а також кількість елементів.
my_list2 = [2, 1, 4, 7, 5, 3, 6, 0, 9, 8]
print(max(my_list2))
print(min(my_list2))
print(len(my_list2))
