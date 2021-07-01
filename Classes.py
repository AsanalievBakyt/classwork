

class Car:

    def __init__(self, model, year, hp):
        self.model = model
        self.year = year
        self.location = 0
        self.light = True
        self.hp = hp
        self.health = 100
    def crash(self, another_car):
        if self.hp > another_car.hp:
            another_car.health -= 50
        else:
            self.health -= 50
        return self.health, another_car.health

    def drive(self,num):
        self.location = num
        return self.location

Toyota = Car('camry', 2021, 200)
Toyota.drive(20)
Honda = Car('Civic', 2020, 150)
print(Toyota.crash(Honda))




