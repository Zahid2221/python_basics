from script import MyClass,Student,Employee

myclass_instance=MyClass()
myclass_instance.func1()
myclass_instance.func2()
myclass_instance.func3()

print('----------------------Main---------------------')

s1_instance=Student('Raam','Mumbai')
s1_instance.student_details()

s2_instance=Student('Ravi','Delhi')
s2_instance.student_details()

print('----------------Student---------------------------')

emp_instance=Employee()
emp_instance.emp_details('Salman Khan')
