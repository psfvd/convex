from math import sqrt


class R2Point:
    """ Точка (Point) на плоскости (R2) """

    # Конструктор
    def __init__(self, x=None, y=None):
        if x is None:
            x = float(input("x -> "))
        if y is None:
            y = float(input("y -> "))
        self.x, self.y = x, y

    # Площадь треугольника
    @staticmethod
    def area(a, b, c):
        return 0.5 * ((a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x))

    # Лежит ли точка вне треугольника? ()
    @staticmethod
    def is_outside_triangle(d, a, b, c):
        s1 = abs(R2Point.area(a, b, d))
        s2 = abs(R2Point.area(b, c, d))
        s3 = abs(R2Point.area(c, a, d))
        return not (abs(R2Point.area(a, b, c)) == s1 + s2 + s3)

    # Количество вершин, лежащих вне треугольника ()
    @staticmethod
    def counter(a, b, c, k, n, m):
        return R2Point.is_outside_triangle(a, k, n, m) + \
                R2Point.is_outside_triangle(b, k, n, m) + \
                R2Point.is_outside_triangle(c, k, n, m)

    # Лежат ли точки на одной прямой?
    @staticmethod
    def is_triangle(a, b, c):
        return R2Point.area(a, b, c) != 0.0

    # Расстояние до другой точки
    def dist(self, other):
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    # Лежит ли точка внутри "стандартного" прямоугольника?
    def is_inside(self, a, b):
        return (((a.x <= self.x and self.x <= b.x) or
                 (a.x >= self.x and self.x >= b.x)) and
                ((a.y <= self.y and self.y <= b.y) or
                 (a.y >= self.y and self.y >= b.y)))

    # Освещено ли из данной точки ребро (a,b)?
    def is_light(self, a, b):
        s = R2Point.area(a, b, self)
        return s < 0.0 or (s == 0.0 and not self.is_inside(a, b))

    # Совпадает ли точка с другой?
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False


if __name__ == "__main__":
    x = R2Point(1.0, 1.0)
    print(type(x), x.__dict__)
    print(x.dist(R2Point(1.0, 0.0)))
    x, y, z, a, b, c = R2Point(1.0, 0.0), R2Point(0.0, 1.0),
    R2Point(0.0, 1.0), R2Point(-5.0, -5.0),
    R2Point(0.0, 4.0), R2Point(3.0, -4.0)
    print(R2Point.is_outside_triangle(x, a, b, c))
