# Les12_Hw by Podkovko Dmitriy

from random import choices


class Validator:

    @staticmethod
    def is_int(value, prm):
        if isinstance(value, int):
            return value
        else:
            print(f'Не правильное значение {prm} Воина: {value}! Введите целое число!')
            return 0

    @staticmethod
    def is_str(value, prm):
        if isinstance(value, str):
            return value
        else:
            print(f'Не правильное {prm} Воина: {value}! Имя Воина должна быть строка!')
            return False


class Warrior:
    def __init__(self, nm, hlh, pwr, arm):
        self.name = Validator.is_str(nm, 'Имя')
        self.health = Validator.is_int(hlh, 'Здоровье')
        self.power = Validator.is_int(pwr, 'Сила')
        self.armor = Validator.is_int(arm, 'Броня')

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, hlh):
        if hlh <= 0:
            print(f'Здоровье Воина: {self.name} 0')
            self._health = 0
        else: self._health = int(hlh)

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, pwr):
        if pwr > self.health * 0.2:
            print(f'Сила Воина: {self.name} не должна превышать здоровье более чем на 20%')
            self._power = int(self.health * 0.2)
        elif pwr < 0: self._power = 0
        else: self._power = int(pwr)

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, arm):
        if arm <= 0:
            self._armor = 0
        else: self._armor = arm

    def attack(self, enemy):
        if enemy.armor > 0:
            enemy.armor -= self.power
            if enemy.armor < 0:
                enemy.health += enemy.armor
                enemy.armor = 0
        else:
            enemy.health -= self.power
            if enemy.health <= 0: enemy.power = 0


class Battle:
    def __init__(self, war1, war2):
        if isinstance(war1, Warrior) and isinstance(war2, Warrior):
            self.warrior1 = war1
            self.warrior2 = war2

    def fight(self):
        if choices([False, True]): # почему-то эта конструкция, несмотря на то что choices выбрал False работает как True
        # is_first = choices([False, True])
        # print(is_first)
        # if is_first:
            attacker, defender = self.warrior1, self.warrior2
        else:
            attacker, defender = self.warrior2, self.warrior1

        while attacker.health > 0 and defender.health > 0 and (attacker.power > 0 or defender.power > 0):
            print(f'Воин: {attacker.name} {attacker.health}/{attacker.power}/{attacker.armor}'\
                  f' атакует воина: {defender.name} {defender.health}/{defender.power}/{defender.armor}')
            attacker.attack(defender)
            print(f'Нанесен урон: {attacker.power}' \
                  f' Воин: {defender.name} {defender.health}/{defender.power}/{defender.armor}')

            if defender.health > 0:
                print(f'Воин: {defender.name} {defender.health}/{defender.power}/{defender.armor}'\
                      f' атакует воина: {attacker.name} {attacker.health}/{attacker.power}/{attacker.armor}')

                defender.attack(attacker)
                print(f'Нанесен урон: {defender.power}' \
                      f' Воин: {attacker.name} {attacker.health}/{attacker.power}/{attacker.armor}')


Ivan = Warrior('Иван', 100, 10, 80)

Petr = Warrior('Петр', 100, 20, 70)

bat1 = Battle(Ivan, Petr)

bat1.fight()
