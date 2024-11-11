# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("Meow")


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("Bark")

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I dont know what I say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old I am {self.color}")

    def speak(self):
        print("Meow")

class Fish(Pet):
    pass
      
class Dog(Pet):

    def speak(self):
        print("Bark")


p = Pet("ovie", 20)
p.show()
c = Cat("Bill", 34, "brown")
c.show()
d = Dog("Jill", 25)
d.show()
f = Fish("fish", 10)
f.speak()

print("\n")
p.speak()
c.speak()
d.speak()
