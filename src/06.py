w1, b1, w2, b2 = 2, 3, 4, 5

def get_y2(x: float):
    y1: float = w1*x + b1
    y2: float = w2*y1 + b2
    return y2

print(w2*w1) # 8

small = 0.001

x = 0
dy2_dx = (get_y2(x+small) - get_y2(x))/small
print(dy2_dx) # 7.999999999999119 ≈ 8

x = 100
dy2_dx = (get_y2(x+small) - get_y2(x))/small
print(dy2_dx) # 8.000000000038199 ≈ 8

x = 1000
dy2_dx = (get_y2(x+small) - get_y2(x))/small
print(dy2_dx) # 7.999999999810825