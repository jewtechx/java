from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return f"{self.name} car has started."

    def stop(self):
        return f"{self.name} car has stopped."

class Motorcycle(Vehicle):
    def start(self):
        return f"{self.name} motorcycle has started."

    def stop(self):
        return f"{self.name} motorcycle has stopped."

my_car = Car("Toyota")
my_motorcycle = Motorcycle("Honda")

print(my_car.start())
print(my_motorcycle.start())
