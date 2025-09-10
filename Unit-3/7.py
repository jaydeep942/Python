# Write a program to access the base class constructor and method in a sub class by using super().
# inheritance 

class Car:
	def __init__(self,carName,carModel,carFuel):
		self.carName = carName
		self.carModel = carModel
		self.carFuel = carFuel

	def display(self):
		print(f"Your car name : {self.carName} \n Your car model is : {self.carModel} \n Your car fuel : {self.carFuel}")




class Electric_Car(Car):
    def __init__(self, carName, carModel, battery_capacity):
        # Call base class constructor using super()
        super().__init__(carName, carModel, "Electric")
        self.battery_capacity = battery_capacity

    def display(self):
        # Call parent display method also
        super().display()
        print(f"Your battery capacity : {self.battery_capacity}")

car_1 = Car("Mahindra","XUV700","diesel")
car_1.display()
print("\n---- Electric Car ----")
car_2 = Electric_Car("Tesla","Model S","100kwh")
car_2.display()