from Shape import Shape
from Square import Square
from Rectangle import Rectangle
from Circle import Circle
from Ellipse import Ellipse

shape = Shape(4, 8)
square = Square(3, 7.9, 3)
rectangle = Rectangle(3, 5, 3, 5)
circle = Circle(3, 3, 1)
ellipse = Ellipse(-6, 9, 4, 2)
# создаем список фигур
shapes_list = [shape, square, rectangle, circle, ellipse]

file = "test.txt"
# очищаем файл
with open(file, "w") as f:
    pass
# отображаем в консоли фигуры из списка и сохраняем их в файл
for sh in shapes_list:
    print(sh.show())
    sh.save(file, "a")
print("LOAD...")
# создаем список классов фигур
sh_classes = [Shape, Square, Rectangle, Circle, Ellipse]
# загружаем фигуры из файла
new_shapes = []
for sh_cls in sh_classes:
    new_shapes += sh_cls.load(file)

for new_sh in new_shapes:
    print(new_sh.show())

