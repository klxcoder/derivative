import math

x_radians = [
    0,
    math.pi / 6,
    math.pi / 4,
    math.pi / 3,
    math.pi / 2,
    math.pi,
    3 * math.pi / 2,
    2 * math.pi,
]

for x in x_radians:
    x_degrees = math.degrees(x)
    sin = math.sin(x)
    cos = math.cos(x)
    print(f"| {x} | {x_degrees} | {sin} | {cos}")