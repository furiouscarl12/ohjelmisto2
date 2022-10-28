#
class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.max_speed = max_speed
        self.odometer = 0
        self.speed = 0

    def print_info(self):
        print(f"Auton {self.register_number} "
              f"huippunopeus on {self.max_speed} km/h, "
              f"matkamittari: {self.odometer} km, "
              f"tämänhetkinen nopeus: {self.speed} km/h.")

    def get_info(self):
        car_info = f"Auton {self.register_number} " \
                   f"huippunopeus on {self.max_speed} km/h, " \
                   f"matkamittari: {self.odometer} km, " \
                   f"tämänhetkinen nopeus: {self.speed} km/h."
        return car_info


    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change < self.max_speed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0

    def kulje(self):


someCar = Car("ABC-1", 120)
otherCar = Car("ABC-2", 150)
otherCar.accelerate(2330)
otherCar.accelerate(15)
otherCar.print_info()
otherCar.accelerate(-200)
otherCar.print_info()

cars = []
for i in range(10):
    cars.append(Car("a-" + str(i), 10))

for car in cars:
    print(car.print_info())