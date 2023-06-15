# Les4_Hw by Podkovko Dmytro

# Написати функцію, що перевіряє чи число є простим


def is_simple(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
            if len(lst) == 3:
                break
    if len(lst) == 2:
        return print('Це просте число!')
    else:
        return print('Це непросте число!')


is_simple(23)


def is_simple_by_VBorovets(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_simple_by_VBorovets(101))


# Написати функцію, що рахує суму елементів по діагоналі в матриці
# (матриця це двомірний список)

def get_sum_diagonal_matrix(matrix):
    sum_diagonal = 0
    for i in range(len(matrix)):
        sum_diagonal += matrix[i][i]
    return sum_diagonal


print(get_sum_diagonal_matrix([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]))


# Написати функцію, що перевіряє чи є строка панаграмою
# (панаграма це та строка, яка містить всі букви алфавіту)

def is_str_panagram(input_str):
    input_str = input_str.lower()
    input_str = set(input_str)
    # input_str.remove(' ')
    if not set('abcdefghijklmnopqrstuvwxyz') - input_str:
        print('Це панаграма!')
    else:
        print('Це не панаграма!')


is_str_panagram('abcdefg hij klmnopqrstuvwxy zz')


# Написати функцію, за допомогою рекурсії порахувати суму елементів списку

def rec_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + rec_sum(lst[1:])


print(rec_sum([1, 2, 3, 4, 5, 6, 7]))
