# import time
# def count_time(func):
#     def wrapper (*args, **kwargs):
#         start = time.time()
#         result = func(*args? **kwargs)


class Peoples:
    def __init__(self, age):
        self.age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0 or value > 100:
            print("Введите год человека от 0 до 100")
            self.__age = 0
        else:
            self.__age = value

    age = property(get_age, set_age)


Ivan = Peoples(50)
print(Ivan.age)


class Dog:

    def bark(self, n):
        print("Гав, гав ..." * n)



class Layka(Dog):

    def bark(self):
        print("Hello", end=' ')
        # d = Dog()
        # d.bark()
        super().bark(3)


Puf = Layka()
Puf.bark()

