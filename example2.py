# Version 2

class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        self._name = name  # Private attribute with getter/setter
        self._date_of_birth = date_of_birth  # Private attribute, read-only
        self._place_of_birth = place_of_birth  # Private attribute, read-only
    
    #Properties for name (can be changed)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name.strip()
    
    # Properties for date_of_birth (read-only - you can't change when you were born!)
    @property
    def date_of_birth(self):
        return self._date_of_birth
    
    # Properties for place_of_birth (read-only - you can't change where you were born!)
    @property
    def place_of_birth(self):
        return self._place_of_birth
    
    def talk(self):
        return f"Hi, my name is {self.name} and I was born in {self.place_of_birth}."


class AdaStaff(Person):  # AdaStaff inherits from Person
    def __init__(self, name, date_of_birth, place_of_birth, employee_id, department):
        super().__init__(name, date_of_birth, place_of_birth)  # Call parent constructor
        self._employee_id = employee_id
        self._department = department
    
    @property
    def employee_id(self):
        return self._employee_id

    @property
    def department(self):
        return self._department

    def work(self):
        return f"{self.name} is working in the {self.department} department."
    
    def get_employee_info(self):
        return f"Employee ID: {self.employee_id}, Department: {self.department}"
    

# Create AdaStaff objects
teacher1 = AdaStaff("Alice Johnson", "15/05/1985", "Birmingham", "EMP001", "Education")
admin = AdaStaff("Zara Sharma", "22/09/1979", "Leeds", "EMP002", "Administration")
# # # Creating instances
# aqil = Person("Aqil Hussain", "01/01/2000", "Manchester")
steve = Person("Steve Rich", "06/06/1998", "London")



# # Test the objects
print(teacher1.talk())  # Inherited from Person
print(teacher1.work())  # New method in AdaStaff
# print(teacher.get_employee_info())








