## Если два класса имеют одинаковые методы, то можно использовать Полемарфизм...

class Shape():
    def __init__(self):
        print('Shape createt')

    def draw(self):
        raise NotImplementedError("Can't instantiate an abstract class") # Наследники переопределят этот треш....
        #print('Drawin  a shape')

    def area(self):
        raise NotImplementedError("Can't instantiate an abstract class") # Наследники переопределят этот треш....
        #print('Calc area')

    def perimetr(self):
        raise NotImplementedError("Can't instantiate an abstract class") # Наследники переопределят этот треш....
        #print('Calc perimeter')

#shape = Shape() #тут будет ошибка
#shape.draw() #тут будет ошибка

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



import math
class Triangle(Shape):
    def __init__(self, a, b, c):
        Shape.__init__(self)

        self.a = a
        self.b = b
        self.c = c

        print('Triangle created')

    def  draw(self):
        print(f'Drawing triangle wiyh side: a={self.a} ; b={self.b} ; c={self.c}.')

    def area(self):
        s = (self.a + self.b + self.c)/2
        return math.sqrt(s*(s-self.a))*(s-self.b)*(s-self.c)

    def perimetr(self):
        return self.a+self.b+self.c

triangle = Triangle(10, 10, 10)

print(triangle.area())
print(triangle.perimetr())

rect = Rectangle(10,15)

for shape in [rect, triangle]:
    shape.draw()