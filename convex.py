from deq import Deq
from r2point import R2Point


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0

    def vert_counter(self):
        return 0


class Void(Figure):
    """ "Hульугольник" """

    def add(self, p):
        return Point(p)



class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p):
        self.p = p

    def add(self, q):
        return self if self.p == q else Segment(self.p, q)

    def vert_counter(self):
        if R2Point.is_outside_triangle(self.p, self.k, self.l, self.m):
            return 1
        else:
            return 0



class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q):
        self.p, self.q = p, q

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    # Вхождение двуугольника в треугольник (надо ли оно)
    def vert_counter(self):
        if R2Point.is_outside_triangle(self.p, self.k, self.l, self.m) and \
            not(R2Point.is_outside_triangle(self.q, self.k, self.l, self.m)) or \
            not(R2Point.is_outside_triangle(self.p, self.k, self.l, self.m)) and \
            R2Point.is_outside_triangle(self.q, self.k, self.l, self.m):
            return 1
        elif R2Point.is_outside_triangle(self.p, self.k, self.l, self.m) and R2Point.is_outside_triangle(self.q, self.k, self.l, self.m):
            return 2
        else:
            return 0

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r)
        elif self.q.is_inside(self.p, r):
            return Segment(self.p, r)
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q)
        else:
            return self


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c):
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))
        # Инитиализация счетчика вершин в многоугольнике ()
        self._vert_counter = R2Point.counter(a, b, c, self.k, self.l, self.m)

    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    # Вызов счетчика ()
    def vert_counter(self):
        return self._vert_counter

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))
            # ()

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))
                # ()
                if R2Point.is_outside_triangle(p, self.k, self.l, self.m) == 1:
                    self._vert_counter -= 1
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._perimeter -= p.dist(self.points.last())
                self._area += abs(R2Point.area(t, p, self.points.last()))
                # ()
                if R2Point.is_outside_triangle(p, self.k, self.l, self.m) == 1:
                    self._vert_counter -= 1
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())
            # ()
            self._vert_counter += R2Point.is_outside_triangle(t, self.k, self.l, self.m)
            self.points.push_first(t)

        return self


if __name__ == "__main__":
    print("Заданный треугольник")
    Figure.k = R2Point()
    Figure.l = R2Point()
    Figure.m = R2Point()
    print("\nТочки плоскости")
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, -6.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(6.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(-1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(-1.0, -1.0))
    print(type(f), f.__dict__)
