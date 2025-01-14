
from dynamics import calculate_relative_coordinates
from kinematics import inverse_kinematics
from settings import *
from serial_interface import *

test_moves = [[[0, 0], [7, 7]],
              [[6, 1], [5, 3]],
              [[4, 1], [5, 5]],
              [[3, 3], [2, 5]]
              ]


def game(moves):
    for move_start, move_finish in moves:
        total_projection_distance_start, theta3 = calculate_relative_coordinates(move_start[0], move_start[1])

        #go to position above start
        theta0, theta1, theta2 = inverse_kinematics(total_projection_distance_start, moving_height)

        move(theta0, theta1, theta2, theta3, move_time)

        #go to start position
        theta0, theta1, theta2 = inverse_kinematics(total_projection_distance_start, set_height)

        move(theta0, theta1, theta2, theta3, move_time)

        #go to position above start
        theta0, theta1, theta2 = inverse_kinematics(total_projection_distance_start, moving_height)

        move(theta0, theta1, theta2, theta3, move_time)
        
        #finish position
        total_projection_distance_start, theta3 = calculate_relative_coordinates(move_finish[0], move_finish[1])

        #go to position above finish
        theta0, theta1, theta2 = inverse_kinematics(total_projection_distance_start, moving_height)

        move(theta0, theta1, theta2, theta3, move_time)

        #go to finish position
        theta0, theta1, theta2 = inverse_kinematics(total_projection_distance_start, set_height)

        move(theta0, theta1, theta2, theta3, move_time)

        #go to position above finish
        theta0, theta1, theta2 = inverse_kinematics(total_projection_distance_start, moving_height)

        move(theta0, theta1, theta2, theta3, move_time)

if __name__ == "__main__":
    game(test_moves)
    ser.close()