# import car class here
from car import Car

class Person:

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation

    @property
    def name(self):
        return self._name

    @property
    def occupation(self):
        return self._occupation

    @classmethod
    def has_oldest_car(cls):
        oldest_year = min(list(map(lambda item: item.year, Car._all)))
        return list(filter(lambda item: item.year == oldest_year, Car._all))[0].owner.name

    @classmethod
    def drives_a(cls, type):
        empty = []
        for item in Car._all:
            if item.make == type:
                empty.append(item.owner.name)
        return empty
