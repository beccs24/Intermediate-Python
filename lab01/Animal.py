class Animal:
    # constructor
    def __init__(self, species = None, weight = None, age = None, name = None):
        if species == None:
            self.species = species
        else:
            self.species = species.upper()
        self.weight = weight
        self.age = age
        if name == None:
            self.name = name
        else:
            self.name = name.upper()
    
    # setter methods
    def setSpecies(self, species):
        '''uppercase str that represents the species of the animal'''
        self.species = species.upper()

    def setWeight(self, weight):
        '''float that represents the weight (in lbs) of an animal'''
        self.weight = weight

    def setAge(self, age):
        '''int that represents the age (in years) of an animal'''
        self.age = age

    def setName(self, name):
        '''uppercase str that represents the name of the animal'''
        self.name = name.upper()

    def toString(self):
        '''returns a str with all the animal attributes'''
        return f'Species: {self.species}, Name: {self.name}, Age: {self.age}, Weight: {self.weight}'
        

#a = Animal("dog", 12.2, 2, "Ruffles")
#print(a.toString())
