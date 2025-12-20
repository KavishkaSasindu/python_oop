from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("Car is started")

    def stop(self):
        print("Car is stopped")

car = Car()

car.go()
car.stop()