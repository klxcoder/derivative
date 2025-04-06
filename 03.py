import math

def derivative1(x: float) -> float:
    return math.cos(x)

def y(x: float) -> float:
    return math.sin(x)

def derivative2(x: float) -> float:
    small: float = 1e-6
    return (y(x + small) - y(x))/small

x: float = 0
d1: float = derivative1(x)
d2: float = derivative2(x)
delta: float = d1 - d2
print(d1) # 1.0
print(d2) # 0.9999999999998334
print(delta) # 1.66644475996236e-13
print(delta < 1e-6) # True