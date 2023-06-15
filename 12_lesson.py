
class Unit:
    def __init__(self, h, p):
    
        self.health = h
        self._power = p
    
    @property
    def health(self):
        # print('in getter')
        return self._health
    
    @health.setter
    def health(self, h):
        # print('in setter')
        self._health = h
        
    def attack(self, enemy):
        enemy.health -= self._power
        
    def __str__(self):
        print('in str')
        return f'{self.health} -- {self._power}'

u1 = Unit(h=100, p=10)
u2 = Unit(h=100, p=10)

u1.attack(u2)
print(u2.health)
print(u2)


class CustomUnit(Unit):
    def __str__(self):
        return f'{self.health} +++ {self._power}'
    



class Peoples:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def __str__(self):
        return f'{self.health} -- {self.power}'

    def get_health(self):
        return self.__health

    # @property
    # def health(self):
    #     return self.__health
    #
    # @health.setter
    # def health(self, health):
    #     self._health = health

    def set_health(self, value):
        if value <= 0:
            print("Введите здоровье не меньше 0")
            self.__health = 0
        else:
            self.__health = value

    def get_power(self):
        return self.__power

    def set_power(self, value):
        if value <= 0 or value > self.health * 0.2:
            print("Здоровье не должно быть больше 20%")
            self.__power = 0
        else:
            self.__power = value

    health = property(get_health, set_health)
    power = property(get_power, set_power)

    def attack(self, enemy):
        enemy.health -= self.power



Ivan = Peoples(100, 20)
print(Ivan.health)
print(Ivan.power)

Petr = Peoples(100, 20)
print(Petr.health)
print(Petr.power)
print(Petr)

Ivan.attack(Petr)
print(Petr.health)