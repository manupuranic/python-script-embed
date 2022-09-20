import serial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

for i, port in enumerate(sorted(ports)):
    print(f"{(i+1)}: {port[0]} ")

selected = int(input("Enter the option number: "))
port_name = ports[selected - 1][0]
print(f"Connecting to: {port_name}...")

try:
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = port_name

    ser.open()
    if ser.is_open:
        print(f"Connected to {ser.portstr}\n")
    else:
        print(f"Failed to conect to {port_name}\n")
except AttributeError as e:
    print("There is no such attribute")

ready_command = input("Start? (ok or ready): ")
ready_command = ready_command.lower()
if ready_command == "ok" or ready_command == "ready":
    ser.write(bytearray(f"{ready_command}\n\r", 'utf-8'))
print("Receiving Data.")
string_read = ""
received = []
while string_read != "completed.":
    string_read = ser.readline().decode().replace("\n", "").replace("\r", "")
    if string_read != "completed.":
        received.append(string_read)
        ser.write(bytearray("U\n\r",'utf-8'))
        print(".", end=" ")

with open(".\\data.txt",'a') as f:
    for string in received:
        f.write(f"{string}\n")
print("\nDone.")
ser.close()

q = input()
if q:
    pass