# Les1_Hw1 by Podkovko Dmytro

# Знайти остачу від ділення 121 на 12, і скільки націло поділиться 134 на 7
a = 121 % 12
print(a)

b = 134 // 7
print(b)
# або
c = int(134 / 7)
print(c)

# Обчислити 4 в степені 7
d = 4 ** 7
print(d)

# Зробити зріз другої половини довільного списку
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[(len(my_list) // 2):])

# зробити зріз з 4го по 8й елемент списку
print(my_list[3:8])

# дістати зі списку остатній елемент і помножити його на 10
last_value = my_list[len(my_list) - 1]
print(last_value * 10)

# видалити 3й елемент списка і вивести його на екран
third_value = my_list.pop(2)
print(third_value)

# добавити в середину списку новий елемент зі значенням 100
my_list.insert(len(my_list) // 2, 100)
print(my_list)

# зробити щоб дві змінні посилалися на один список
my_list1 = my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list2[0] = 100
print(my_list1)
print(my_list2)
