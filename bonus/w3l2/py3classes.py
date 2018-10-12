class Pet():

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def __str__(self):
        return f'{self.name} is {self.species}'


class Cat(Pet):

    def __init__(self, name, species, weight):
        Pet.__init__(self, name, species)
        self.weight = weight

    def voice(self):
        print("Miauuu")


class Dog(Pet):

    def __init__(self, name, species, weight):
        Pet.__init__(self, name, species)
        self.weight = weight

    def voice(self):
        print("woof")


class CatDogMonster(Cat, Dog):
    pass


class ClassName(object):
    """docstring for ClassName"""

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg


class CatPack():
    cat_arr = []

    def __add__(self, cat):
        self.cat_arr.append(cat)
        return self

    def __len__(self):
        return len(self.cat_arr)

    def __str__(self):
        cat_names = [cat.name for cat in self.cat_arr]
        return 'cats in pack {}'.format(cat_names)

    def __call__(self):
        return 'Hello'.format(len(self))
