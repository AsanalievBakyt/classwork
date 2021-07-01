


class Planet:

    def __init__(self, name):
        self.name = name
        self.temp = -273
        self.oxygen = False
        self.water = False
        self.humanity = False

    def populate(self):
        if self.humanity and self.oxygen:
            self.population = 0
            print('Планета пригодня для жизни')
        else:
            print('Планета не пригодня для жизни')
class Earth(Planet):

    def __init__(self,name):
        Planet.__init__(self,name)
        self.atmosphere = True
        self.temp = -10
        self.oxygen = True
        self.water = True
        self.humanity = True


class Gas(Planet):


    def __init__(self, name):
        Planet.__init__(self, name)
        self.gas_type = 'H'

a = Earth('Zemlya')


a.humanity = True
a.oxygen = True

a.populate()
