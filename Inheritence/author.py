from person import Person

class Author(Person):
    
    def details(self):
        print("I am an Author")

author = Author(1,"kavishka","user@gmail.com","123456","Backer St")
print(author.person_name_and_email())
print(author.username)
    