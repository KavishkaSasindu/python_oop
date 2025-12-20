from person import Person
from super_admin import SuperAdmin

class Admin(Person,SuperAdmin):
    pass

admin = Admin(2,"admin","admin@gmail.com","123456","Homagama")

print(admin.person_name_and_email())
admin.super_admin()