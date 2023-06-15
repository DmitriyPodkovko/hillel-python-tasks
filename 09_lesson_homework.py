# Les9_Hw by Podkovko Dmytro

# Створити класс людина, в якого є атрибут ріст -
# зробити неможливим введення невалідного росту
# ( валідним є від 40см до 240см )


class Peoples:
    def __init__(self, height):
        self.height = height

    def get_height(self):
        return self.__height

    def set_height(self, value):
        if value < 40 or value > 240:
            print("Введите рост человека от 40 см до 240 см")
            self.__height = 0
        else:
            self.__height = value

    height = property(get_height, set_height)


Ivan = Peoples(241)
print(Ivan.height)


# Написати декоратор який робить паузу в одну секунду перед виконанням функції

from time import sleep


def pause(func):
    def wrapper(*args, **kwargs):
        sleep(1)
        result = func(*args, **kwargs)
        return result

    return wrapper()


@pause
def some_func():
    print("I am something doing ...")


some_func
