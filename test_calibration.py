import numpy as np
from kinematics import transformation_matrix
from settings import *

theta0, theta1 = 90, 90
theta2 = 180 - theta0 - theta1

H0 = transformation_matrix(theta0, dz0, dy0)
H1 = transformation_matrix(theta1, dz1, dy1)
H2 = transformation_matrix(theta2, dz2, dy2)
H3 = np.array((dz3, dy3, 1)).T

H_combined = H0 @ H1 @ H2 @ H3

target_vector = [0, -0.078, 1]

print((target_vector[1]-H_combined[1])**2)

dH0_dtheta0 =  np.array([
        [-np.sin(np.radians(theta0)), np.cos(np.radians(theta0)), dz0],
        [np.cos(np.radians(theta0)),  -np.sin(np.radians(theta0)), dy0],
        [0, 0, 1]
    ])

partial_diff = -2*(target_vector-H_combined)[1]*(dH0_dtheta0 @ H1 @ H2 @ H3)[1]

print(partial_diff)

theta0_after = theta0 - 0.1*partial_diff

H0_after =  transformation_matrix(theta0_after, dz0, dy0)

H_combined_after = H0_after @ H1 @ H2 @ H3

target_vector = [0, -0.08, 1]

print(theta0_after, (target_vector[1]-H_combined_after[1])**2)
