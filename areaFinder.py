import math
from typing import List


def right_ang_triag(a, b, c) -> float:

    if a * a + b * b == c * c:
        return 0.5 * a * b
    elif c * c + b * b == a * a:
        return 0.5 * c * b
    else:
        return 0.5 * a * c


class areaFinder():

    def circle_area(self, radius: float) -> float:
        if radius <= 0:
            print("Неверная круг")
            return -1.0
        else:
            return math.pi * radius ** 2

    def triangle_area(self, sides: List[float]) -> float:
        if any(i <= 0.0 for i in sides):  # Negative sides or 0 are not valid
            print("Неверная фигура")
            return -1.0
        a, b, c = sides[0], sides[1], sides[2]
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            print("Неверный треугольник")
            return -1.0
        if (a * a + b * b == c * c) or (c * c + b * b == a * a) or (a * a + c * c == b * b):  # Right-angled
            return right_ang_triag(a, b, c)
        else:
            s = (a + b + c) / 2.0
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def rectangle_area(self, sides: List[float]) -> float:
        if any(i <= 0 for i in sides): # Negative sides or 0 are not valid
            print("Неверная фигура")
            return -1.0
        sides.sort()
        a, b, c, d = sides[0], sides[1], sides[2], sides[3]
        if a == b and c == d:
            return min(sides) * max(sides)  # For rectangle we multiply width and length, also works for square
        else:
            print("Неверная фигура")
            return -1.0

    def find_area(self, sides: List[float]) -> float:  # when we have only sides, not figure itself
        n = len(sides)
        if any(i <= 0 for i in sides):  # Negative sides or 0 are not valid
            print("Неверная фигура")
            return -1.0
        match n:
            case 1:  # One side = radius of circle
                return math.pi * sides[0] ** 2
            case 3:  # Three sides = triangle
                return self.triangle_area(sides)
            case 4:  # Four sides = rectangle or square. We can't count rhombus because we don't have angles
                return self.rectangle_area(sides)
