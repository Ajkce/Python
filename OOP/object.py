# Everything in Python is an object including a class. In other words, a class is an object in Python.

class Person:
    pass

person = Person()

print(isinstance(person, Person))

print(type(Person))
Person.name = "Anymonus"
setattr(Person, 'age', 20)
delattr(Person, 'name')
print(Person)