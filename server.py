import socket
import keyboard
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6300))
s.listen(1)

speed = 0; 

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    while 1:
        if keyboard.is_pressed("1"):
            speed = 51
            clientsocket.send(bytes("Speed set to  " + str(speed), "utf-8"))
            time.sleep(1)
        elif keyboard.is_pressed("2"):
            speed = 102
            clientsocket.send(bytes("Speed set to " + str(speed), "utf-8"))
            time.sleep(1)
        elif keyboard.is_pressed("3"):
            speed = 153
            clientsocket.send(bytes("Speed set to " + str(speed), "utf-8"))
            time.sleep(1)
        elif keyboard.is_pressed("4"):
            speed = 204
            clientsocket.send(bytes("Speed set to " + str(speed), "utf-8"))
            time.sleep(1)
        elif keyboard.is_pressed("5"):
            speed = 255
            clientsocket.send(bytes("Speed set to " + str(speed), "utf-8"))
            time.sleep(1)

        if keyboard.is_pressed("w"):
            clientsocket.send(bytes("f["+str(speed) +"]" + "f["+str(speed) +"]" + "f["+str(speed) +"]" + "f["+str(speed) +"]", "utf-8"))
            time.sleep(1)
        elif keyboard.is_pressed("a"):
            clientsocket.send(bytes("r["+str(speed) +"]" + "r["+str(speed) +"]" + "f["+str(speed) +"]" + "f["+str(speed) +"]", "utf-8"))
            time.sleep(1)
        elif keyboard.is_pressed("s"):
            clientsocket.send(bytes("r["+str(speed) +"]" + "r["+str(speed) +"]" + "r["+str(speed) +"]" + "r["+str(speed) +"]", "utf-8"))
            time.sleep(1)
        elif keyboard.is_pressed("d"):
            clientsocket.send(bytes("f["+str(speed) +"]" + "f["+str(speed) +"]" + "r["+str(speed) +"]" + "r["+str(speed) +"]", "utf-8"))
            time.sleep(1)