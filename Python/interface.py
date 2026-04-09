import serial
import time

BAUD_RATE = 9600
PORT_NAME = "/dev/ttyACM0"

def main():
    serial_port = serial.Serial(port=PORT_NAME, baudrate=BAUD_RATE)

    wait_for_ready(serial_port)

def wait_for_ready(port):
    while True:
        bytes = port.read_all().decode("UTF-8")
        print(bytes)
        time.sleep(1)

if __name__ == "__main__":
    main()
