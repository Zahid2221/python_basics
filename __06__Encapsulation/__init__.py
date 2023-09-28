# __06__Encapsulation : binding/wrapping the data in a single class or a single entity
# we achieve encapsulation using private protected and public  __ means its private
class Myclass:
    __n=10
    def display(self):
        n=25
        print('The value of n in local ', n)
        print('The value on n in instance', self.__n)

obj=Myclass()
obj.display()
print(obj.__n)