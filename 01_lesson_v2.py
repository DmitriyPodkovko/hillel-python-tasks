# задание №1
a = "10"
b = "15"

a = int(a)
b = int(b)
print(a / b)

# задание №2
student = {
    "name": ["Andrey", "Oleg", "Leonid"],
    "age": [29, 39, 49],
    "mark": {
        5: "A",
        4: "B",
        3: "C",
        2: {2: "perezdacha",
            1: "otchislenie"

            }
        }
    }
print(student["mark"][2][2])

# задание №3
a = ["a", "b", "c", "d", "e", 1, 2, 3, 4, 5]
print(tuple(a[0:3]))

# задание №4 (corrected)
from math import pow

x = 5
y = 5

if x != y:
    print(x * y)
else:
    print(pow(x, 2))

# задание №5
a = 777
b = 333
c = 555

if a < b and a < c:
    print(a, "a - min")
elif b < a and b < c:
    print(b, "b - min")
else:
    print(c, "c min")

# задание №6 (corrected)
A = 7
B = 3
C = 55

if A > B > C:
    print(A + 3, B + 3, C + 3)
else:
    print(A * -1, B * -1, C * -1)

# задание №7
a = 10
b = 200
c = 30

if a > b > c:
    print(a + b)
elif c > b > a:
    print(c + b)
else:
    print(a + c)

# задание №8
a = [27, 5, 34, 9, 1, 17, 18, 54, 96, 48]
print(max(a))
print(min(a))
print(len(a))