from Animal import Animal

class Cow(Animal):
    def __init__(self, species = None, name = None, sound = None):
        #super().__init__(species, name)
        Animal.__init__(self, species, name)
        self.sound = sound
    
    # Available method for the Cow Class 
    def setSound(self, sound):
        self.sound = sound

    def getSound(self):
        s = 'Using super class getSound method\n'
        # s += super().getSound() + '\n'
        s += Animal.getSound(self) + '\n'
        s += 'Extending it with our own method\n'
        s += self.sound
        return s
    
	# return "{}!".format(self.sound)

'''
c = Cow("Cow", "Betsy", "Moo")
print(c.getAttributes())
c.setSound("Moo") # Sets a Cow sound attribute to "Moo"
print(c.getSound()) # I’m an Animal!!! (calls the Animal.getSound method)
'''

c = Cow("Cow", "Betsy", "Moo") # Passes in data for Animal AND Cow
a = Animal("Unicorn", "Lala")

zoo = [c, a]

for i in zoo:
    print(i.getAttributes())
    print(i.getSound())
    print("---")
