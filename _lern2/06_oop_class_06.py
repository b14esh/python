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

        def area(self):
            return self.width * self.height

        def perimetr(self):
            return 2*(self.width+self.height)
        def draw(self):
            print(f'Draw rectangle with width={self.width} and height={self.height}')

rect = Rectangle(10,15)

print(shape.area())

print(rect.area())
print(rect.perimetr())
print(rect.draw())

