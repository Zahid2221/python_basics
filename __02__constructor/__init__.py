# constructors are used to initialize the variables to be used in the program

# without sending the arguments to the constructor

"""
class Student:
    def __init__(self):
        self.name='Zahid'
        self.age=23
        self.address='Bangalore'

    def display(self):
        print(f"My name is {self.name} and my age is {self.age} and i am from {self.address}")

obj=Student()
obj.display()
"""

# with sending arguments to the constructor
class Student:
    def __init__(self, name, age , address):
        self.name=name
        self.age=age
        self.address=address

    def display_details(self):
        print(f" Hey {self.name}, I know ur age is {self.age} and ur address is {self.address}")

s1=Student('Faiz',19,'Chickmagalore')
s1.display_details()

s2=Student('Safwan', 26,'Shivamogga')
s2.display_details()

