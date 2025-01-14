import serial
from settings import *
import time

# Replace with your SSC-32U's serial port (e.g., "COM3" on Windows or "/dev/ttyUSB0" on Linux)
serial_port = '/dev/tty.usbserial-AI049KG3'  # Example for Linux, use "COM3" or similar for Windows
baud_rate = 9600              # Default baud rate for SSC-32U

# Initialize serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=1)

def send_command(command):
    """
    Send a command to the SSC-32U and optionally print the command.
    """
    ser.write(command.encode())  # Send the command to the SSC-32U
    print(f"Sent command: {command.strip()}") 

def degrees_to_pw(degrees, center, multiplier):
    return center + degrees * multiplier * degree_to_pw

def degrees_to_pw_2(degrees, center, multiplier):
    return center + degrees * multiplier * degree_to_pw_2

def degrees_to_pw_3(degrees, center, multiplier):
    return center + degrees * multiplier * degree_to_pw_3

def degree_to_step(theta0, theta1, theta2, theta3):
    step0 = degrees_to_pw(theta0, servo_0_center, servo_0_direction)
    step1 = degrees_to_pw(theta1, servo_1_center, servo_1_direction)
    step2 = degrees_to_pw_2(theta2, servo_2_center, servo_2_direction)
    step3 = degrees_to_pw_3(theta3, servo_3_center, servo_3_direction)
    return step0, step1, step2, step3

def move(theta0, theta1, theta2, theta3, move_time):
    step0, step1, step2, step3 = degree_to_step(theta0, theta1, theta2, theta3)
    #send_command(f'#0 P{step0} #1 P{step1} #2 P{step2} #3 P{step3} T{move_time}\r')
    send_command(f'#0 P{step0} #1 P{step1} #2 P{step2} #3 P{step3} T500\r')
    time.sleep(1)