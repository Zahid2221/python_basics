# Inheritance -- Inheriting property of one class to another class
# 1. single Level Inheritance  2. Multilevel  3. Multiple

#single Level: Father son relationship
class Father:
    def f_display(self):
        print('This is father class')
class Son(Father):
    def c_display(self):
        print('This is from child class')

obj=Son()
obj.f_display()

print('----------------------------------------')
# Multi level

class GrandF:
    def gf_display(self):
        print('This is from grandfather')

class Father(GrandF):
    def f_display(self):
         print('This is from father')
class Son(Father):
    def s_display(self):
        print('This is from son')

obj=Son()
obj.gf_display()
obj.f_display()
obj.s_display()

print('----------------------------------------')

class Father:
    def f_display(self):
        print('The father property')

class Mother:
    def m_display(self):
        print('The mother property')

class Son(Father, Mother):
    def c_display(self):
        print('This is child property')

obj=Son()
obj.f_display()
obj.m_display()
obj.c_display()

