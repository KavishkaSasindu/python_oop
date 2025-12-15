class Person:
    id:int
    name:str
    email:str
    
    def __init__(self, id:int, name:str, email:str):
        self.__id = id
        self.__name = name
        self.__email = email
        
# traditional way of creating getter and setter

    #getters
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    #setters
    def set_id(self, id:int):
        self.__id = id
        
    def set_name(self, name:str):
        self.__name = name
        
    def set_email(self, email:str):
        self.__email = email
        
person = Person(1,"Kavishka","user@gmail.com")

print(person.get_name())
print(person.get_email())

person.set_name("Kavishka Sasindu")
print(f"New name is {person.get_name()}")