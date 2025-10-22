class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self._year = year
        self._fuel = 100

    @property
    def year(self):
        return self._year 

    @property
    def fuel(self):
        return self._fuel
    
    @fuel.setter
    def fuel(self, amount):
        self._fuel = amount    
    
    
    def set_fuel(self, amount):
        if (self._fuel + amount) > 100:
            self._fuel = 100
        else:
            self._fuel += amount
        return f"Fuel level is now {self.fuel}"
         
    def drive(self):
        self.fuel -= 10
        return f"The {self.make} {self.model} moves forward"
    
    # def stop(self):
    #     return f"The "
    

car1 = Car("Audi", "TT", 2016)
car2 = Car("Nissan", "Micra", 2005)
car3 = Car("Toyota", "Supra", 2010)



car1.make = "Skoda"
print(car1.fuel)
#print(car1.set_fuel(50))

car1.fuel = 1000
print(car1.fuel)