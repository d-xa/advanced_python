# A decorator function takes another function as argument, 
# wraps its behaviour inside an inner function, and returns the wrapped function.
def decorater_function(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper


# To decorate another function say_hello()
# use the following syntax
@decorater_function
def say_hello():
    print("hello")

if __name__ == '__main__':
    say_hello()