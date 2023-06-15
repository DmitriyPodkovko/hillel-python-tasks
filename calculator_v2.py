# Homework_2 by Dmitriy Podkovko
# 2)


def question():
    while True:
        answer = input('Continue again? (Y/N): ').upper()
        if answer in ('Y', 'N'):
            return answer
        else:
            continue


def action(r):
    if r is None:
        a = float(input('Enter number = ').replace(',', '.'))
    else:
        a = r
    s = input('Enter operation (+,-,*,/,**,**mod): ')
    if s in ('+', '-', '*', '/', '**', '**mod'):
        b = float(input('Enter next number = ').replace(',', '.'))
        if s == '+':
            r = a + b
        elif s == '-':
            r = a - b
        elif s == '*':
            r = a * b
        elif s == '/':
            if b != 0:
                r = a / b
            else:
                print('Cannot be divided by 0!')
        elif s == '**':
            r = pow(a, b)
        elif s == '**mod':
            c = int(input('Enter mod (int) = '))
            if b >= 0:
                if c != 0:
                    r = pow(int(a), int(b), c)
                else:
                    print('mod cannot be 0!')
            else:
                print('degree cannot be negative!')

    else:
        print('Invalid operation!')
    return r


while True:
    try:
        result = None
        count = int(input('Enter element count: '))
        while count > 1:
            result = action(result)
            if result is not None:
                count -= 1
            else:
                break
        if result is not None:
            print('Result: %.2f' % result)
    except ValueError:
        print('Error entering number type!')
        if result is not None:
            print('Result: %.2f' % result)

    if question() == 'N':
        print('Bye!')
        break
