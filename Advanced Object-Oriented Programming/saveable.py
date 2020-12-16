from abc import ABCMeta, abstractclassmethod

from database import Database

class Saveable:
    
    @abstractclassmethod
    def to_dict(self):
        pass

    def save(self):
        Database.insert(self.to_dict())

