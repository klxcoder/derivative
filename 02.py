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

# Define the width for each column
width_x = 25
width_degrees = 25
width_sin = 25
width_cos = 25

# Print the header
print(f"| {'x (radians)':<{width_x}} | {'x (degrees)':<{width_degrees}} | {'sin(x)':<{width_sin}} | {'cos(x)':<{width_cos}} |")

# Print the separator line
print("-" * (width_x + width_degrees + width_sin + width_cos + 13))

for x in x_radians:
    x_degrees = math.degrees(x)
    sin_x = math.sin(x)
    cos_x = math.cos(x)
    print(f"| {x:<{width_x}} | {x_degrees:<{width_degrees}} | {sin_x:<{width_sin}} | {cos_x:<{width_cos}} |")