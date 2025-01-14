import numpy as np
from settings import *

square_positions = np.zeros((8, 8, 2))

for i in range(8):
    for j in range(8):
        square_positions[i, j, 0] = x_0 + m + (i + 0.5) * l
        square_positions[i, j, 1] = y_0 + m + (j + 0.5) * l

def calculate_position(target_square_x, target_square_y):
    x_pos = a_0_x - target_square_x
    y_pos = target_square_y - a_0_y

    servo_0_angle = np.degrees(np.arctan(y_pos/x_pos))
    total_projection_distance = np.sqrt(x_pos**2 + y_pos**2)/1000

    return total_projection_distance, servo_0_angle

def calculate_relative_coordinates(x, y):
    [x_val, y_val] = square_positions[x, y, :]

    d, theta = calculate_position(x_val, y_val)

    return d, theta
