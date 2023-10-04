#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Figure, Void

f = Void()
t = Void()

print("Predefined triangle")
Figure.k = R2Point()
t = t.add(Figure.k)
Figure.n = R2Point()
t = t.add(Figure.n)
Figure.m = R2Point()
t = t.add(Figure.m)
print("\nPlane points")

try:
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}, C = {f.vert_counter()}")
        print()
except (EOFError, KeyboardInterrupt):
    print("\nStop")
