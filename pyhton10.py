#tehtävät 1, 2, 3


import random


class Elevator:
    def __init__(self, curr_floor=1, lowest_floor=1, highest_floor=10):
        self.curr_floor = curr_floor
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor

    def move(self, target_floor):
        if target_floor > self.curr_floor:
            self.floor_up(target_floor)

    def floor_up(self, target_floor):
        print(f"Heading up to floor {target_floor}")
        while self.curr_floor != target_floor:
            print(f"Current floor {self.curr_floor}")

    def floor_down(self, target_floor):
        print(f"Heading down to floor {target_floor}")
        while self.curr_floor != target_floor:
            print(f"Current floor {self.curr_floor}")
            self.curr_floor -= 1
        print(f"Floor {target_floor} reached\n")


class House:
    def __init__(self, lowest_floor=1, highest_floor=10,
              elevator_count=random.randint(1, 6), elevator_list=None):
        if elevator_list is None:
            elevator_list = []
        for i in range(0, elevator_count):
            elevator_list.append(Elevator(lowest_floor, lowest_floor, highest_floor))

    def move_elevator(self, elevator_id, target_floor):
        print(f"Elevator {elevator_id + 1}")
        self.elevator_list[elevator_id].move(target_floor)

    def fire_alarm(self):
        print(f"The fire alarm.\n")
        for i in range(0, self.elevator_count):
            self.move_elevator(0 + i, self.lowest_floor)



elevator = Elevator()
elevator.move(random.randint(2, 10))
elevator.move(1)


house = House(1, 10, 3)
house.move_elevator(0, random.randint(2, 10))
house.move_elevator(1, random.randint(2, 10))
house.move_elevator(2, random.randint(2, 10))
house.fire_alarm()







#tehtävä 4

import random


class Car:
    def __init__(self, plate, top_speed, curr_speed=0, dist=0):
        self.plate = plate
        self.top_speed = top_speed
        self.curr_speed = curr_speed
        self.dist = dist

    def accelerate(self, acc):
        self.curr_speed = self.curr_speed + acc
        if self.curr_speed > self.top_speed:
            self.curr_speed = self.top_speed
        elif self.curr_speed < 0:
            self.curr_speed = 0

    def travel(self, hour):
        self.dist = self.dist + self.curr_speed * hour


class Race:
    def __init__(self, race_name, race_dist, car_list):
        self.race_name = race_name

    def hour_pass(self):
        for car in cars:
            car.accelerate(random.randint(-15, 10))
            car.travel(1)

    def print(self):
        for car in cars:
            print(f"{car.plate}: top speed: {car.top_speed:.2f} km/h, ")
                  f"current speed: {car.curr_speed:.1f} km/h, distance: {car.dist:.1f} km")

    def race_over(self):
        for car in cars:
            car.accelerate(random.randint(-15, 10))

for i in range(1, 11):
    cars.append(Car("ABC-" + str(i), random.uniform(100, 200)))


while not is_race_over:
    if hours == 10:
        race.print()