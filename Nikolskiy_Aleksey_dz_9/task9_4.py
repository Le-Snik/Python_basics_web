class Car:
    is_police = False

    def __init__(self, name, color='red'):
        self.name = name
        self.color = color
        self.speed = 0

    def go(self, speed):
        self.speed = speed
        print(f"car {self.name} is ride by {self.speed} km/h")

    def stop(self):
        print(f"car {self.name} is stopped")
        Car.speed = 0

    def turn(self, direction):
        print(f"car {self.name} turned at {direction}")

    def show_speed(self):
        print(f"speed of {self.name} = {self.speed}")


class PoliceCar(Car):
    is_police = True


class TownCar(Car):
    max_speed = 60

    def show_speed(self):
        print(f"speed of {self.name} = {self.speed}")
        if self.speed > self.max_speed:
            print(f"{self.name} Overspeed!")

    def change_max_speed(self, new_val):
        TownCar.max_speed = new_val


class WorkCar(TownCar):
    max_speed = 40

    def change_max_speed(self, new_val):
        WorkCar.max_speed = new_val


bus = TownCar(name='Bus', color='red')
taxi = TownCar(name='taxi', color='yellow')
bus.go(70)
bus.show_speed()
print(f' bus max speed = {bus.max_speed} \n taxi max speed = {taxi.max_speed}  \n')
bus.change_max_speed(100)
print(f' bus max speed = {bus.max_speed} \n taxi max speed = {taxi.max_speed} \n ')

bulldozer = WorkCar(name='bulldozer', color='black')
bulldozer.go(50)
bulldozer.show_speed()
bulldozer.change_max_speed(10)
print(f' bus max speed = {bus.max_speed} \n taxi max speed = {taxi.max_speed} \n')

#
# my_car = Car(name='rambler', color='silver')
# my_car.go(50)
# my_car.show_speed()
