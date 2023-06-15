# Les6_Hw by Podkovko Dmytro

# Написати функції, що приймають назву файла і:
# читають файл
# повністю переписують його
# додають в нього отриману строку


def f_read(file_name):
    with open(file_name, 'r') as f:
        return f.read()


print(f_read('Test'))


def f_write(file_name, string):
    result = False
    with open(file_name, 'w') as f:
        f.write(string + '\n')
        result = True
    return result


print(f_write('Test', 'qwerty'))


def f_add(file_name, string):
    result = False
    with open(file_name, 'a') as f:
        f.write(string + '\n')
        result = True
    return result


print(f_add('Test', 'asdfg'))
