import numpy as np
from scipy.optimize import minimize
from settings import *

def transformation_matrix(theta, dz, dy):
    return np.array([
        [np.cos(np.radians(theta)), -np.sin(np.radians(theta)), dz],
        [np.sin(np.radians(theta)),  np.cos(np.radians(theta)), dy],
        [0, 0, 1]
    ])

def objective_function(thetas, H_total):
    theta0, theta1 = thetas
    theta2 = 180 - theta0 - theta1

    H0 = transformation_matrix(theta0, dz0, dy0)
    H1 = transformation_matrix(theta1, dz1, dy1)
    H2 = transformation_matrix(theta2, dz2, dy2)
    H3 = transformation_matrix(0, dz3, dy3)

    H_combined = H0 @ H1 @ H2 @ H3

    error_z = H_combined[0, 2] - H_total[0, 2]
    error_y = H_combined[1, 2] - H_total[1, 2]
    return error_z**2 + error_y**2

def inverse_kinematics(z_val, y_val):

    # Overall transformation matrix from (z1, y1) to (z2, y2)
    H_total = np.array([
        [-1, 0, -z_val],
        [0, -1, -y_val],
        [0, 0, 1]
        ])
    # Initial guess for the angles
    initial_guess = [75, 75]
    # Define the bounds for each variable (angle in degrees)
    bounds = [(-180, 180), (-180, 180)]

    # Perform the optimization using the Nelder-Mead method
    result = minimize(objective_function, initial_guess, args=(H_total), bounds=bounds, method='Nelder-Mead')

    # Extract the optimized angles
    theta0, theta1 = result.x
    theta2 = 180 - theta0 - theta1

    return theta0, theta1, theta2
