from abc import ABCMeta, abstractclassmethod

class Animals:
    def walk(self):
        print('Walking....')

    @abstractclassmethod
    def num_legs(self):
        pass


class Dog(Animals):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4
    
class Monkey(Animals):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2


animals = [Dog('rolf') , Monkey('Bob')]

for a in animals:
    print(isinstance(a, Animals))
    print(a.num_legs())