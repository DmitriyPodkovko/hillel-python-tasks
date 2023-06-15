b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(b[:])

# 3 останіх
print(b[-3:])

# перша половина
# print(b[:5])
print(b[:len(b) // 2])
print(b[:int(len(b) / 2)])

# тільки парні
print(b[1::2])

# 4-5
print(b[3:5])

# у зворотньому порядку
print(b[::-1])


def name_of(a, b, c=5):
    return a**2, b**2, c**2


result = name_of(a=3, b=4)
a1, b1, c1 = result
print(result)
print(a1)
print(b1)
print(c1)


# def math(a, b, c):
#     d = b**2 - 4 * a * c
#     x1 = (-b + d**0.5) // 2 * a
#     x2 = (-b + d**0.5) // 2 * a
#     return x
#
#
# result = math(1, 2, 3)
# print(result)

def is_polidrom(string):
    return string[::] == string[::-1]


result = is_polidrom('abcdd')
print(result)


def lst(l=[]):
    l.append(1)
    print(l)


lst()
lst()


def lst(l=None):
    if l is None:
        l = []
    l.append(1)
    print(l)


lst()
lst()


a = [10, 30, 20, 50, 70, 90, 15, 101, 50, 17]
b = [101, 301, 201, 501, 701, 901, 151, 101, 501, 171]


def d(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result

def func(a, b):
    c = []

    for i in a:
        if i in b:
            c.append(i)

    return max(c)


a = d(16)
b = d(12)

print(func(a, b))


def nsd(a, b):

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


print(nsd(12, 16))


# def f1(l=[]):
#     for i in range(1, n + 1)
#
#     return
#
#
# def f2(l=[]):
#     pass


def fact(n):
    s = 1
    for i in range(1, n+1):
        s = s * i

    return s


print(fact(5))


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print(fact(5))


# a = [1, 2, 3  4]
#
# def sum(l=[]):
#
#     return


a = [1, 10, 3, 5]
b = [2, 3, 4, 7]

def func(a, b):
    return max(a, b)

result = map(func, a, b)
print(list(result))

#print(func(a))
print(max(a))

a = [1, 2, 3]

result = map(lambda x: x[::-1], a)

print(list(result))