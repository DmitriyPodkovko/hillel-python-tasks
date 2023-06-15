# Les3_Hw by Podkovko Dmytro

# На вибір for або while:
# Задача яку обговорювали вкінці зайняття:
# зробити зі списка новий список елнментами якого будуть добуток всіх чисел масива крім поточного:
# [1,2,3,4] ---> [24, 12, 8, 6]

list_in = [1, 2, 3, 4]
list_out = []

x = 1
for i in list_in:
    if i != 0:
        x = x * i

for j in list_in:
    if j != 0 and 0 in list_in:
        list_out.append(0)
    elif j != 0:
        list_out.append(x // j)
    else:
        list_out.append(x)

print(list_out)
