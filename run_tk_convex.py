#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon


def void_draw(self, tk):
    pass


def point_draw(self, tk, color):
    tk.draw_point(self.p, color)


def segment_draw(self, tk, color):
    tk.draw_line(self.p, self.q, color)


def polygon_draw(self, tk, color):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first(), color)
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)

tk = TkDrawer()
f = Void()
t = Void()
tk.clean()

print("Predefined triangle")
Figure.k = R2Point()
t = t.add(Figure.k)
t.draw(tk, "red")
Figure.n = R2Point()
t = t.add(Figure.n)
t.draw(tk, "red")
Figure.m = R2Point()
t = t.add(Figure.m)
t.draw(tk, "red")
print("\nPlane points")

try:
    while True:
        f = f.add(R2Point())
        tk.clean()
        t.draw(tk, "red")
        f.draw(tk, "black")
        print(f"S = {f.area()}, P = {f.perimeter()}, C = {f.vert_counter()}\n")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
