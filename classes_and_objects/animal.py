from person import Person,person

class Animal:
    
    name:str
    species:str
    owner:Person
    
    def __init__(self, name:str, species:str, owner:Person):
        self.name = name
        self.species = species
        self.owner = owner
        
        
animal = Animal("Liya","Dog", person)   # like this we can pass objects too

print(animal.owner.name)
print(animal.owner.email)