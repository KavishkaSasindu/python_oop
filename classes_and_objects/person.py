class Person:      # define class as like this
    
    name:str           #attributes
    email:str
    
    def __init__(self, name:str, email:str):        #__init__()  it is a method that trigger automatically and initialize the objects
        self.name = name                            # act like a constructor
        self.email = email
        
person = Person("Kavishka", "user@gmail.com")       # creation of object