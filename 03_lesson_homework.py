# Les3_Hw by Podkovko Dmytro

# За допомогою циклу for & while розв'язати наступні задачі:
# Знайти максимальне число в списку
a = [10, 30, 20, 50, 70, 90, 15, 101, 50, 17]

max_int = a[0]
for i in a:
    if i > max_int:
        max_int = i
print(max_int)

max_int = a[0]
i = 0
while i < len(a):
    if a[i] > max_int:
        max_int = a[i]
    i = i + 1
print(max_int)

# знайти суму всіх чисел в списку що діляться на 3
s = 0
for i in a:
    if i % 3 == 0:
        s = s + i
print(s)

s = 0
i = 0
while i < len(a):
    if a[i] % 3 == 0:
        s = s + a[i]
    i = i + 1
print(s)

# знайти суму простих чисел у списку
s = 0
for i in a:
    k = 0
    for j in range(1, i + 1):
        if i % j == 0:
            k = k + 1
    if k == 2:
        s = s + i
print(s)

s = 0
i = 0
while i < len(a):
    k = 0
    for j in range(1, a[i] + 1):
        if a[i] % j == 0:
            k = k + 1
    if k == 2:
        s = s + a[i]
    i = i + 1
print(s)

s = 0
i = 0
while i < len(a):
    k = 0
    j = 1
    while j < a[i] + 1:
        if a[i] % j == 0:
            k = k + 1
        j = j + 1
    if k == 2:
        s = s + a[i]
    i = i + 1
print(s)

# На вибір for або while:
# Задача яку лбшоворювади вкінці зайняття:
# зробити зі списка новий список елнментами якого будуть добуток всіх чисел масива крім поточного:
# [1,2,3,4] ---> [24, 12, 8, 6]
list_in = [1, 2, 3, 4]
list_out = []
i = 0
while i < len(list_in):
    temp = list_in.pop(0)
    x = 1
    j = 0
    while j < len(list_in):
        x = x * list_in[j]
        j = j + 1
    list_out.append(x)
    list_in.append(temp)
    i = i + 1
print(list_in)
print(list_out)

# за допомогою for знайти перші 100 чисел фібоначи
f = [0, 1]
for i in range(98):
    f.append(f[-1] + f[-2])
for j in f:
    print(j)
