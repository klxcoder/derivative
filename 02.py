import math

x_radians: list[float] = [
    0,
    math.pi / 6,
    math.pi / 4,
    math.pi / 3,
    math.pi / 2,
    math.pi,
    3 * math.pi / 2,
    2 * math.pi,
]

# Define the width for each column
width_x: int = 25
width_degrees: int = 25
width_sin: int = 25
width_cos: int = 25

# Print the header
print(f"| {'x (radians)':<{width_x}} | {'x (degrees)':<{width_degrees}} | {'sin(x)':<{width_sin}} | {'cos(x)':<{width_cos}} |")

# Print the separator line
print("-" * (width_x + width_degrees + width_sin + width_cos + 13))

for x in x_radians:
    x_degrees: float = math.degrees(x)
    sin_x: float = math.sin(x)
    cos_x: float = math.cos(x)
    print(f"| {x:<{width_x}} | {x_degrees:<{width_degrees}} | {sin_x:<{width_sin}} | {cos_x:<{width_cos}} |")