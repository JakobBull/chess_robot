"""
This script is used for further callibration, mapping what physical rotations various combinations of pulsewidth lead to.
"""
import csv
from settings import *
from serial_interface import *
import time

import numpy as np
servo_0_test_list = np.arange(0, 130, 5)
servo_1_test_list = np.arange(0, 110, 5)
servo_2_test_list = np.arange(-30, 30, 5)

servo_0_rest_position = 0
servo_1_rest_position = 0
servo_2_rest_position = 0
servo_3_rest_position = 0
#servo_3_test_list = [-15, 0, 15]

#send_command(f"#0 P2430 #1 P620 #2 P1380 #3 P1420 T1000\r")
#time.sleep(2)

with open('callibration.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["servo", "pw", "theta_true"])

    for theta in servo_0_test_list:
        move(theta, servo_1_rest_position, servo_2_rest_position, servo_3_rest_position, move_time=1000)
        print("Hello")
        while True:
            
            user_input = input("Enter theta_true_0:\n")
            theta_true_0 = float(user_input)

            if (theta_true_0 >= -5 and theta_true_0 < 150):
                break
            else:
                print("The input is not correct.")

            pw_0 = degrees_to_pw(theta, servo_0_center, servo_0_direction)
            writer.writerow(["0", pw_0, theta_true_0])

    for theta in servo_1_test_list:
        move(servo_0_rest_position, theta, servo_2_rest_position, servo_3_rest_position, move_time=1000)
        while True:
            user_input = input("Enter theta_true_1:\n")
            theta_true_1 = float(user_input)

            if (theta_true_1 >= -5 and theta_true_1 < 150):
                break
            else:
                print("The input is not correct.")

            pw_1 = degrees_to_pw(theta, servo_1_center, servo_1_direction)
            writer.writerow(["1", pw_1, theta_true_1])

    for theta in servo_2_test_list:
        move(servo_0_rest_position, servo_1_rest_position, theta, servo_3_rest_position, move_time=1000)
        while True:
            user_input = input("Enter theta_true_2:\n")
            theta_true_2 = float(user_input)

            if (theta_true_2 >= -50 and theta_true_2 < 50):
                break
            else:
                print("The input is not correct.")

            pw_2 = degrees_to_pw(theta, servo_2_center, servo_2_direction)
            writer.writerow(["2", pw_2, theta_true_2])

print("Done.")