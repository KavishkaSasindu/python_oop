class Person:
    def __init__(self, id:int, username:str, email:str, password: str, address:str):
        self.__id = id
        self.__username = username
        self.__email = email
        self.__password = password
        self.__address = address
        
        
    def person_name_and_email(self):
        return f"Person name is {self.__username} and my email is {self.__email}"
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id:int):
        self.__id = id
        
    @property
    def username(self):
        return self.__username
        
    @username.setter
    def username(self, username:str):
        self.__username = username
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email:str):
        self.__email = email
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password:str):
        self.__password = password
        
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address:str):
        self.__address = address
         