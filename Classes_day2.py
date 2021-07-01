


class Cat:

    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.color = 'black'
        self.ears = 'normal'
        Cat.counter += 1

    def __str__(self):
        # works with print() str()
        return f'STR: {self.name}'


    def __repr__(self):
        # all other
        return f'REPR: {self.name}'

class EgyptCat(Cat):

    def __init__(self, name, age, province):
        Cat.__init__(self,name,age)
        self.province = province
        self.color = 'white'

class ScotlandCat(Cat):


    def __init__(self, name, age):
        Cat.__init__(self,name,age)
        self.ears = 'cute'