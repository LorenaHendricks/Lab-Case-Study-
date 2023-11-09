class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile:
    def __init__(self, vehicle_type):
        super().__init__(vehicle_type)
        self.year = ""
        self.make = ""
        self.model = ""
        self.doors = ""
        self.roof = ""

    def display_data(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)
        car = Automobile("car")
        car.year = input("Enter the year: ")
        car.make = input("Enter the make: ")
        car.model = input("Enter the model: ")
        car.doors = input("Enter the number of doors (2 or 4): ")
        car.roof = input("Enter the type of roof (solid or sun roof): ")
        car.display_data()
