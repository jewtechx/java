class Animal :
    def speak(self):
        pass

class Dog :
    def speak(self):
        return "I am a dog"

class Cat :
    def speak(self):
        return "I am a cat"

my_dog = Dog()
my_cat = Cat()

animals = [my_cat,my_dog]

for animal in animals:
    print(animal.speak())