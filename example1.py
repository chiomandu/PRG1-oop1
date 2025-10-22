class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
    
    def talk(self):
        return f"Hi, my name is {self.name} and I was born in {self.place_of_birth}."


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.fuel = 100

    def drive(self):
        self.fuel -= 10
        return f"The {self.make} {self.model} moves forward"
    
    # def stop(self):
    #     return f"The "
    

car1 = Car("Audi", "TT", 2016)
car2 = Car("Nissan", "Micra", 2005)
car3 = Car("Toyota", "Supra", 2010)

print(car1.drive())
print(car1.fuel)

car1.make = "Skoda"
print(car1.make)



# # Creating two instances of the Person class
# person1 = Person("Aqil Hussain", "01/01/2000", "Manchester")

# person2 = Person("Steve Rich", "06/06/1998", "London")


# # Using the objects
# print(steve.talk())
# print(aqil.talk())
# print(f"Name: {steve.name}")
# print(f"Date of birth: {steve.date_of_birth}")
# print(f"Place of birth: {steve.place_of_birth}")

# # We can change the name
# steve.name = "Stephen Rich"
# print(f"Updated name: {steve.name}")