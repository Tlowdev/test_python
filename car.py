class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def car_description(self):
        """Return car description neately formatted"""
        kind = f"{self.year} {self.make} {self.model}"
        return kind.title()
    
    def update_odometer(self, mileage):
        """Sets odometer to given value.
            Rejects if it attempts to roll odometer back
        """
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You cant roll back the odometer.") 
    
    def read_odometer(self):
        """Reads odometer and prints to console"""
        print(f"This car has {self.odometer} miles.")

#Make an instance of a car
my_car = Car('honda', 'accord', 2016)
print(my_car.car_description())
my_car.update_odometer(23999)
my_car.read_odometer()
#Attempt to lower odometer
my_car.update_odometer(10)
#New updated odometer
my_car.update_odometer(50000)
my_car.read_odometer()
