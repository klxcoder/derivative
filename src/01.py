def derivative1(x: float) -> float:
    return 2 * x

def y(x: float) -> float:
    return x*x

def derivative2(x: float) -> float:
    small: float = 1e-6
    return (y(x + small) - y(x))/small

x: float = 5
d1: float = derivative1(x)
d2: float = derivative2(x)
delta: float = d1 - d2
print(d1) # 10
print(d2) # 10.00000100148668
print(delta) # -1.0014866802521283e-06
print(delta < 1e-6) # True