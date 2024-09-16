class MyClass:

    def func1(self):
        print('This is func1 method')

    def func2(self):
        print('This is the second method of Myclass')

    def func3(self):
        print('This is the last and third method of myclass')

class Student:
    def __init__(self, name, address):
        self.name=name
        self.address=address

    def student_details(self):
        print(f"His name is {self.name} and he is from {self.address}")

class Employee:
    def emp_details(self, name):
        print(f"my name is {name}")

