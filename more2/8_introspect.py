# Интроспекция

print(issubclass.__doc__)
help(issubclass)

class Shape:
    pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

circle = Circle(10)

print((issubclass(Circle, Shape)))

print(isinstance(circle, Circle))
print(isinstance(circle, Shape))

print(isinstance(12, int))
print(isinstance("hello", str))
print(isinstance("world", float))

print(callable(circle))
print(callable(print))

if hasattr(circle, 'radius'):
    print(getattr(circle, 'radius'))
    setattr(circle, 'radius', 20)
    print(getattr(circle, 'radius'))

dir(circle)  # dir - посмотреть атрибуты обьекта

print(Circle.__dict__)
print(Circle.__name__)

print(type(circle))

circle2 = circle

print(id(circle))
print(id(circle2))

print(repr(circle))
