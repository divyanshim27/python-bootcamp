class Animal:
    def eat(self):
        print("Eating food...")

# Child class inherits eat() automatically
class Dog(Animal):
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.eat()   # Output: Eating food... (inherited from Animal)
my_dog.bark()  # Output: Woof! (Dog's own action)