from os import name


class Animal:
    def __init__(self, name, species, age, sound, color):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        self.color = color

def make_sound(self):
    print(f"{self.name} says {self.sound}!")

def description(self):
    print(f"This is {self.name}, a {self.color} {self.species} aged {self.age}.")

def change_color(self, new_color):
    self.color = new_color
    print(f"{self.name}'s new color is {self.color}.")

def __del__(self):
    print(f"{self.name} has been deleted.")

# Creating objects of the Animal class
animal1 = Animal("Fluffy", "Cat", 3, "Meow", "White")
animal2 = Animal("Rex", "Dog", 5, "Woof", "Brown")