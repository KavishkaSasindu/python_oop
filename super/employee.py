from user import User

class Employee(User):
    def __init__(self, employe_id:int, department:str, firstname:str, lastname:str, email:str):
        super().__init__(firstname,lastname,email)
        self.employe_id = employe_id
        self.department = department

    def get_employee_details(self):
        print(f"Employee ID is {self.employe_id} and department is {self.department}")
        

employee = Employee(1,"IT","Kavishka","Sasindu","user@gmail.com")
employee.get_fullname()
employee.get_employee_details()