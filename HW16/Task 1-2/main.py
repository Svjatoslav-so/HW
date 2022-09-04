from Circle import Circle
from Figure import Figure
from Rectangle import Rectangle
from RightTriangle import RightTriangle
from Trapezoid import Trapezoid

fig = Figure()
rect = Rectangle(5, 8)
circ = Circle(4)
r_tri = RightTriangle(3, 4)
trapez = Trapezoid(2, 5, 3)

fig_list = [fig, rect, circ, r_tri, trapez]

for f in fig_list:
    print("figura:           ", f)
    print("figura.get_square:", f.get_square())
    print("int(figura):      ", int(f))
