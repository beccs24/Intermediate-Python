from Animal import Animal

class AnimalShelter:
    # constructor
    def __init__(self):
        self.dict = {}

    # methods
    def addAnimal(self, animal):
        '''adds an Animal object to the AnimalShelter'''
        if self.dict.get(animal.species) == None:
            self.dict[animal.species] = [animal]
        elif not animal in self.dict.get(animal.species):
            self.dict[animal.species].append(animal)


    def removeAnimal(self, animal):
        if self.dict.get(animal.species) != None:
            for animal_inlist in self.dict.get(animal.species):
                if animal_inlist.name == animal.name and animal_inlist.weight == animal.weight and animal_inlist.age == animal.age:
                    self.dict[animal.species].remove(animal)
                            
        
    def removeSpecies(self, species):
        if self.dict.get(species.upper()) != None:
            self.dict.pop(species.upper())
            

    def getAnimalsBySpecies(self, species):
        if self.dict.get(species.upper()) == None:
            return ""
        else:
            end_str = ""
            for animal_inlist in self.dict.get(species.upper()):
                if animal_inlist == self.dict.get(species.upper())[-1]:
                    end_str += animal_inlist.toString()
                else:
                    end_str += animal_inlist.toString() + "\n"
            return end_str
                
        
    def doesAnimalExist(self, animal):
        if self.dict.get(animal.species) != None:
            for animal_inlist in self.dict.get(animal.species):
                if animal_inlist.name == animal.name and animal_inlist.weight == animal.weight and animal_inlist.age == animal.age:
                    return True
                else:
                    return False
            return False
        else:
            return False



