import math

def derivative1(x: float) -> float:
    return math.cos(x*x)*2*x

def y(x: float) -> float:
    return math.sin(x*x)

def derivative2(x: float) -> float:
    small: float = 1e-9
    return (y(x + small) - y(x))/small

x: float = 2 * math.pi

d1: float = derivative1(x)
d2: float = derivative2(x)
delta: float = d1 - d2
print(delta < 1e-6) # True