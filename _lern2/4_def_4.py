

def hello_world():
    print('Hello, world!')
hello_world()


#hello2 = hello_world() будет вызов функции
hello2 = hello_world #  присвоение перременной к функции
hello2()


# Функции можно возрощать из функции
def hello_world1():
    def internal():
        print(('Hello, world'))
        return internal

hello3 = hello_world1()


####
def say_somthing(func):
    func()
def hello_world3():
    print('Hello, world!')

say_somthing(hello_world3)


#декораторы
# Содержит в себе обертку \ врапер

def log_decorator(func):
    def wrap():
        print(f'Calling func {func}')
        func()
        print(f'Func {func} finish its work')
    return wrap

def hello():
    print('Hello, world')

wrapped_by_logger = log_decorator(hello)
wrapped_by_logger()


# декоратор
@log_decorator
def hello():
    print('hello, world')
hello()


# Декоратор Performence
from timeit import default_timer as timer
import math
import time

def measure_time(func):
    def inner(*args, **kwargs):
        start = timer()

        func(*args, **kwargs)

        end = timer()

        print(f'Functions {func.__name__} took {end-start} for execution')
    return inner

@measure_time
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))
factorial(100)



