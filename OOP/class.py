class Person:
    # Thuis is a class attribute that is shared by all instance of this class
    # Class variable
    counter = 0
    
    
    def __init__(self, name, age):
        # These are instances attributes
        self.name = name
        self.age = age
        Person.counter += 1
    
    # This is instance method
    def greet(self):
        print(f"My name is {self.name}")
        
    # This is class method
    # It is also shared by all instances of the class
    @classmethod
    def create_anymonous(cls):
        return Person("Anymonus", 22)
    

# person1 = Person("Ajaya", 24)

# person1.greet()
# print(person1.counter)

# anymous = Person.create_anymonous()
# print(anymous.name)

class Employee(Person):
    def __init__(self, name, age, empId):
        super().__init__(name, age)
        self.empId = empId
    
    def greet(self):
        print(f"Hello, I am {self.name} and my EmpId is {self.empId}")
        
emp1 = Employee("John", 26, 'L55436')

emp1.greet()