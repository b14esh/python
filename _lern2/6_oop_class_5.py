# Наследование
class Shape():
    def __init__(self):
        print('Shape createt')

    def draw(self):
        print('Drawin  a shape')

    def area(self):
        print('Calc area')

    def perimetr(self):
        print('Calc perimeter')

shape = Shape()

class Rectangle(Shape):  # собственно наследование ....
        def __init__(self, width, height ):
            Shape.__init__(self)

            self.width = width
            self.height = height

            print('Rectangle created')


rect = Rectangle(10,15)

print(shape.area())