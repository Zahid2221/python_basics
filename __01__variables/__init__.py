myglobalvar='python'
class Student:
    name='Zahid'  #instance variable
    def display(self):
        x='coding'
        print('This is instance variable ', self.name)
        print('This is local variable', x)
        print('This is global __01__variables', myglobalvar)
# create an object to call the methods of a class
obj=Student()
obj.display()



