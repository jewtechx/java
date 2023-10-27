class Car:
    def __init__(self, make, model):
        self._make = make  # Protected attribute
        self.__model = model  # Private attribute

    def display_info(self):
        print(f"This is a {self._make} {self.__model}.")

my_car = Car("Toyota", "Camry")
my_car.display_info()
print(my_car._make)  # Accessing a protected attribute
# print(my_car.__model)  # This will result in an error because __model is private.
