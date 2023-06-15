 # Les5_Hw by Podkovko Dmytro

# за допомогою map перетворити числа в списку на їх дзеркальні 123 -> 321
a = [123, 456, 789]

print(list(map(lambda x:
               int(''.join(reversed(str(x)))), a)))


# за дрпомогою filter залишити в списку слова, довжина яких більше 5 букв
a = ['qwerty', 'asdf', 'zxcvbn', 'qazwsxedc', 'plfb']


def func2(lst):
    return len(lst) > 5


print(list(filter(func2, a)))
