import serial

BAUD_RATE = 9600
PORT_NAME = "/dev/ttyACM0"

MESSAGE_SIZE = 8

MALFORMED_MESSAGE = '0'
CONNECTION_REQUEST = '1'
CONNECTION_ESTABLISHED_MESSAGE = "LOG: ARDUINO CONNECTION SUCCESFULLY ESTABLISHED"


def main():
    serial_port = serial.Serial(port=PORT_NAME, baudrate=BAUD_RATE)
    input_buffer = []
    output_buffer = []

    wait_for_connection(serial_port, input_buffer, output_buffer)

    while True:
        read_message(serial_port, input_buffer)
        input_buffer.clear()


def read_message(port, buffer):
    reading = True
    while reading:
        buffer.append(port.read())
        print(buffer)

        if len(buffer) < MESSAGE_SIZE:
            continue
        elif len(buffer) > MESSAGE_SIZE:
            buffer.clear()

        if buffer[0].decode("UTF-8") == 'MALFORMED_MESSAGE':
            buffer.clear()
            continue

        reading = False


def wait_for_connection(port, input_buffer, output_buffer):
    while True:
        read_message(port, input_buffer)

        if input_buffer[0].decode("UTF-8") == CONNECTION_REQUEST:
            print(CONNECTION_ESTABLISHED_MESSAGE)

            output_buffer.append(CONNECTION_REQUEST.encode("UTF-8"))
            port.write(b"".join(output_buffer))

            input_buffer.clear()
            output_buffer.clear()
            return


if __name__ == "__main__":
    main()
