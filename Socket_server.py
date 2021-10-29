import socket
import threading
import serial

HEADER = 64
PORT = 5051
SERVER = '192.168.137.101'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
    ser.flush()

def send_to_arduino(msg):
    ser.write((msg + '\n').encode(FORMAT))
    
def handle_client(conn,addr):
    print(f"[NEW_CONNECTION] {addr} connected.")
    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"{addr}, {msg}")
            send_to_arduino(msg)
            conn.send("Msg recived".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LESTENING] server is lestining on {SERVER}")
    while True:
        conn,addr =server.accept()
        thread =  threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE_CONNECTIONS] {threading.activeCount() -1}")
    

print("[STARTING] server is starting ..... ")
start()