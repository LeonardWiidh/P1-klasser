import os

class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def view_car(self):
        return f"{self.make} {self.model} ({self.color})."


def list_cars():
    for index, car in enumerate(cars, 1):
        print(f"{index} {car.view_car()}")

cars = []

while True:
    make = input("make ")
    model = input("model ")
    color = input("color ")

    cars.append(Car(make, model, color))

    list_cars()
