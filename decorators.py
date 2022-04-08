# A decorator function takes another function as argument, wraps its behaviour inside
# an inner function, and returns the wrapped function.
def decorater_function(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper


# Another function say_hello() can be decorated with the decorater_function
@decorater_function
def say_hello():
    print("hello")


say_hello()