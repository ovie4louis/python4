class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()
       

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    # @classmethod
    # def add_person(cls):
    #     cls.number_of_people += 1

p1 = Person("ovie")
p2 = Person("louis")
p3 = Person("joy")
print(Person.number_of_people_( ))


