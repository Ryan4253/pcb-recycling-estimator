import serial
import Constants

ser = serial.Serial(Constants.ARDUINO_PORT, Constants.ARDUINO_BAUD_RATE)

def setPower(power : int):
    ser.write((str(power) + '\n').encode())

if __name__ == '__main__':
    try:
        while True:
            choice = input('Input: ').lower()

            if choice == 'end':
                ser.close()
                break

            setPower(int(choice))
                
    except KeyboardInterrupt:
        ser.close()
