#__05__Abstraction----> Hiding the functionality  but show essential details
from abc import abstractmethod

class A:
    @abstractmethod
    def my_abstarct_function(self):
        pass
    #abstact methods can only be declared but not defined
class B(A):
    def my_abstarct_function(self):
        print("This is my working code here")

obj=B()
obj.my_abstarct_function()