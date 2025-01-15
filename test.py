"""
This script tests if the serial connection to the SSC-32U can be made from our local runtime.
"""
import serial
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
    print(f"Sent command: {command.strip()}")  # Print the command (without the newline character)

try:
    # Example: Move servo 0 to position 1500 over 1000ms
    send_command('#1 P640 T1000\r')
    time.sleep(2)  # Wait for the command to complete


    # You can add more commands here as needed
finally:
    ser.close()  # Close the serial connection when done
