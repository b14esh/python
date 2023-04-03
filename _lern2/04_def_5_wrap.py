# декоратор для написания декоратора.....
from functools import  wraps

def log_decoration(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(f'Calling func {func}')
        func(*args, **kwargs)
        print(f'Func {func} finished its work')
    return wrap


@log_decoration
def hello():
    '''  Super megsa hello'''
    print('Hellom, world')

hello()

help(hello)


