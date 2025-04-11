import numpy as np

x = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]) # shape (3, 4)

w = np.array([
    [13, 14],
    [15, 16],
    [17, 18],
    [19, 20],
]) # shape (4, 2)

b = np.array([
    [21, 22],
    [23, 24],
    [25, 26],
]) # shape (3, 2)

def get_y(x, w, b):
    return x @ w + b

y = get_y(x, w, b)

print(y)
"""
[[191 202]
 [449 476]
 [707 750]]
"""