# Decorators

def my_decorator(func):
    def wrapper():
        print('Hi this starts the decorator')
        func()
        print('This is end of the decorator')
    return wrapper

@my_decorator    # This is decorator function
def display():
    print('This is the decorator')
    print('Hello')
    print('How are u')

display()