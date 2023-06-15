# Homework_2 by Dmitriy Podkovko
# 1)


def question():
    while True:
        answer = input('Continue again? (Y/N): ').upper()
        if answer in ('Y', 'N'):
            return answer
        else:
            continue


while True:
    try:
        a = float(input('Enter number a = ').replace(',', '.'))
        b = float(input('Enter number b = ').replace(',', '.'))
        s = input('Enter operation (+,-,*,/,**,**mod): ')
        if s in ('+', '-', '*', '/', '**', '**mod'):
            if s == '+':
                print('%.2f' % (a+b))
            elif s == '-':
                print('%.2f' % (a-b))
            elif s == '*':
                print('%.2f' % (a*b))
            elif s == '/':
                if b != 0:
                    print('%.2f' % (a/b))
                else:
                    print('Cannot be divided by 0!')
            elif s == '**':
                print('%.2f' % pow(a, b))
            elif s == '**mod':
                c = int(input('Enter mod (int) = '))
                if b >= 0:
                    if c != 0:
                        print('%.2f' % pow(int(a), int(b), c))
                    else:
                        print('mod cannot be 0!')
                else:
                    print('degree cannot be negative!')
        else:
            print('Invalid operation!')
    except ValueError:
        print('Error entering number type! Try again')

    if question() == 'N':
        print('Bye!')
        break
