class User:
    def __init__(self, firstname:str, lastname:str, email:str):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def get_fullname(self):
        print(f"Full name is {self.firstname} {self.lastname}") 
        