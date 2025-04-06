def derivative1(x: float):
    return 2 * x

def y(x: float):
    return x*x

def derivative2(x):
    small: float = 1e-6
    return (y(x + small) - y(x))/small

x = 5
d1 = derivative1(x)
d2 = derivative2(x)
delta = d1 - d2
print(d1) # 10
print(d2) # 10.00000100148668
print(delta) # -1.0014866802521283e-06
print(delta < 1e-6) # True