# Les8_Hw by Podkovko Dmytro

# Зробити схему класів для довільної теми,
# схема означає що не потрібно прописувати методи і атрибути
# досить просто їх оголосити і встановити залежності між класами.


# животные
class Animals:
    pass


# млекопитающие
class Mammals(Animals):
    pass


# пресмыкающиеся
class Reptiles(Animals):
    pass


# земноводные
class Amphibians(Animals):
    pass


# дикие
class Wild(Mammals):
    pass


class Wolf(Wild):
    pass


class Fox(Wild):
    pass


class Bear(Wild):
    pass


class Tiger(Wild):
    pass


# домашние
class Pet(Mammals):
    pass


class Dog(Pet):
    pass


class Cat(Pet):
    pass


# цирковой медведь
class CircusBear(Wild, Pet):
    pass


# цирковой тигр
class CircusTiger(Wild, Pet):
    pass


barsick = Cat()
print(type(barsick))

sharkhan = Tiger()
print(type(sharkhan))

misha = CircusBear()
print(type(misha))

sharkhan_advanced = CircusTiger()
print(type(sharkhan_advanced))

