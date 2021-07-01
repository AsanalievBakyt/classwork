

class Item:

    def __init__(self, name, quality, armor=0, health=0, attack=0):
        self.name = name
        self.armor = armor
        self.health = health
        self.attack = attack
        self.__quality = quality
        self.__check_quality()

    def __repr__(self):
        return self.name

    def __check_quality(self):
        if self.__quality == 'rare':
            if isinstance(self, Weapon):
                self.attack += (self.attack * 0.2)
            elif isinstance(self, Armor):
                self.armor += (self.armor * 0.2)
                self.health += (self.health * 0.2)


class Weapon(Item):

    def __init__(self, name, attack: int, quality):
        Item.__init__(self,name, attack= attack, quality= quality)



class Armor(Item):

    def __init__(self, name, armor: int, health: int, quality):
        Item.__init__(self,name, armor= armor, health= health, quality=quality)



class Unit:
    counter = 0
    health_plus = 10
    armor_plus = 1
    attack_plus = 1

    def __init__(self, name= 'unit'):
        self.health = 100
        self.armor = 0
        self.attack = 5
        self.attack_type = 'melee'
        self.x_pos = 0
        self.y_pos = 0
        self.items = []
        Unit.counter += 1

    @property
    def attack_type(self):
        return self.__attack_type

    @attack_type.getter
    def attack_type(self):
        return f'{self.name} attack_type: {self.__attack_type}'

    @attack_type.setter
    def attack_type(self,value):
        if value in ['melee', 'ranged']:
            self.__attack_type = value
    @attack_type.deleter
    def attack_type(self):
        self.__attack_type = None
        print('Object attack type deleted (set None)')

    def __str__(self):
        return self.name

    def move(self, new_x, new_y):
        self.x_pos = new_x
        self.y_pos = new_y

    def armor_upgrade(self):
        self.health += self.health_plus
        self.armor += self.armor_plus

    def attack_upgrade(self):
        self.attack += self.attack_plus

    def equip_item(self, item):
        if len(self.items) == 6:
            return 'not enough space!'
        self.items.append(item)
        if isinstance(item, Weapon):
            self.attack += item.attack
        elif isinstance(item, Armor):
            self.armor += item.armor
            self.health += item.health

    def drop_item(self, item):
        if item in self.items:
            self.items.remove(item)
            if isinstance(item, Weapon):
                self.attack -= item.attack
            elif isinstance(item, Armor):
                self.armor -= item.armor
                self.health -= item.health

    def fight(self, other):
        while self.health >0 and other.health >0:
            other.health -= self.attack
            self.health -= other.attack
        print(f'Attacker health: {self.health}, Defender health: {other.health}')


class Warrior(Unit):
    health_plus = 20
    armor_plus = 2
    attack_plus = 3

    def __init__(self):
        self.name = f'warrior:{Unit.counter}'
        Unit.__init__(self, name=self.name)
        self.health = 200
        self.armor = 3
        self.attack = 20

class Hero(Unit):

    def __init__(self, name):
        Unit.__init__(self, name)
        self.level = 1

    def levelup(self, experience):
        table = {1:200, 2:1000, 3:1500}
        while experience > 0:
            if table[self.level] <= experience:
                experience -= table[self.level]
                self.level += 1
                self.health += 1
                self.attack += 1





helmet = Armor('helmet', 10,5, 'rare')
sword = Weapon('sword', 10, 'rare')
w1 = Warrior()

w1.equip_item(helmet)
w1.equip_item(sword)


w2 = Warrior()

w1.fight(w2)

# print(w1.attack_type)

h1 = Hero('Lotar')
print(h1.__dict__)
h1.levelup(1200)
print(h1.__dict__)