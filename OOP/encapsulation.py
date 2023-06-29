# abstraction, encapsulation, inheritance, and polymorphism.

"""""Encapsulation is the packing of data and functions that work on that data within a single object. By doing so, you can hide the internal state of the object from the outside. This is known as information hiding."""

"""""
Prefix an attribute with a single underscore (_) to make it private by convention.
Prefix an attribute with double underscores (__) to use the name mangling.
"""

class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0

counter = Counter()

counter.increment()
counter.increment()
counter.increment()

counter.current = -999
print(counter._Counter__current)

print(counter.value())