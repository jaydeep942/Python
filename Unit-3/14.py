# Write a program to override the super class method in Subclass

# Superclass
class Animal:
    def sound(self):
        print("Animals make different sounds.")

# Subclass overriding the method
class Dog(Animal):
    def sound(self):
        print("Dog barks: Woof Woof!")

# Another Subclass
class Cat(Animal):
    def sound(self):
        print("Cat meows: Meow Meow!")

# Main Program
a = Animal()
d = Dog()
c = Cat()

print("Superclass method call:")
a.sound()

print("\nSubclass (Dog) overriding method call:")
d.sound()

print("\nSubclass (Cat) overriding method call:")
c.sound()
