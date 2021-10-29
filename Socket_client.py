import socket
from tkinter import *
LED_ON_VARDAGSRUM = False
LED_ON_RUM = False
LED_ON_BADRUM = False
LED_ON_KOK = False
LED_ON_HALL = False
TURN_OFF_ALL = False
TURN_ON_ALL = False
OPEN_DOOR = False
SAFE_MODE = False
HEADER = 64
PORT = 5051
SERVER = '192.168.137.101'
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):  
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

my_message = ""


def clicked_hall():
    global LED_ON_HALL
    if LED_ON_HALL == False:
        send("LED_ON_HALL")
        LED_ON_HALL = True

    else:
        send("LED_OFF_HALL")
        LED_ON_HALL = False


def clicked_turn_off_all():
    global TURN_OFF_ALL
    if TURN_OFF_ALL == False:
        send("LED_OFF_ALL")
        LED_ON_KOK = True


def clicked_turn_on_all():
    global TURN_ON_ALL
    if TURN_ON_ALL == False:
        send("LED_ON_ALL")
        LED_ON_KOK = True



def clicked_kok():
    global LED_ON_KOK
    if LED_ON_KOK == False:
        send("LED_ON_KOK")
        LED_ON_KOK = True
    else:
        send("LED_OFF_KOK")
        LED_ON_KOK = False

def clicked_badrum():
    global LED_ON_BADRUM
    if LED_ON_BADRUM == False:
        send("LED_ON_BADRUM")
        LED_ON_BADRUM = True
    else:
        send("LED_OFF_BADRUM")
        LED_ON_BADRUM = False


def clicked_vardagsrum():
    global LED_ON_VARDAGSRUM
    if LED_ON_VARDAGSRUM == False:
        send("LED_ON_VARDAGSRUM")
        LED_ON_VARDAGSRUM = True
 
    else:
        send("LED_OFF_VARDAGSRUM")
        LED_ON_VARDAGSRUM = False
 

def clicked_rum():
    global LED_ON_RUM
    if LED_ON_RUM == False:
        send("LED_ON_RUM")
        LED_ON_RUM = True

    else:
        send("LED_OFF_RUM")
        LED_ON_RUM = False

def clicked_open_door():
    global OPEN_DOOR
    if OPEN_DOOR == False:
        send("OPEN_DOOR")
        OPEN_DOOR = True

def clicked_close_door():
    global OPEN_DOOR
    if OPEN_DOOR == True:
        send("CLOSE_DOOR")
        OPEN_DOOR = False

def clicked_safe_mode():
    global SAFE_MODE
    if SAFE_MODE == False:
        send("SAFE_MODE")
    else:
        SAFE_MODE=True
        



window = Tk()
window.geometry('900x830+500+100')
window.title('Hemautomation')


frame = Frame(window).pack()
window.configure(bg='whitesmoke')

lbl = Label(frame, text="Control your home through this window", font=("Arial Bold",22), fg = "Blue" , borderwidth=2 , bg = 'Bisque' )
lbl.place(x=90,y=10)

btn = Button(frame, text = "Rum LED",height=0, border = (15),width=15, font=("Arial Bold",18), bg="skyblue", fg="Blue", command = clicked_rum)
btn.place(x=90,y=100)



btn2 = Button(frame, text = "Vardagsrum LED",border = (15),width=15, font=("Arial Bold",18), bg="skyblue", fg="Blue", command = clicked_vardagsrum)
btn2.place(x=90,y=200)

btn3 = Button(frame, text = "Badrum LED",border = (15),width=15, font=("Arial Bold",18), bg="skyblue", fg="Blue", command = clicked_badrum)
btn3.place(x=90,y=300)

btn4 = Button(frame, text = "Kök LED",border = (15),width=15, font=("Arial Bold",18), bg="skyblue", fg="Blue", command = clicked_kok)
btn4.place(x=90,y=400)

btn5 = Button(frame, text = "Hall LED",border = (15),width=15, font=("Arial Bold",18), bg="skyblue", fg="Blue", command = clicked_hall)
btn5.place(x=90,y=500)

btn6 = Button(frame, text = "OFF All LED", border = (15), width=15, font=("Arial Bold",18), bg="skyblue", fg="Blue", command = clicked_turn_off_all)
btn6.place(x=90,y=600)

btn7 = Button(frame, text = "On All LED",border = (15), width=15, font=("Arial Bold",18), bg="skyblue", fg="Blue", command = clicked_turn_on_all)
btn7.place(x=90,y=700)

btn8 = Button(frame, text = "Open Door",border = (15), width=15, font=("Arial Bold",18), bg="skyblue", fg="Blue", command = clicked_open_door)
btn8.place(x=420,y=100)

btn9 = Button(frame, text = "Close Door",border = (15), width=15, font=("Arial Bold",18), bg="skyblue", fg="Blue", command = clicked_close_door)
btn9.place(x=420,y=200)

btn10 = Button(frame, text = "Safe mode",border = (15), width=15, font=("Arial Bold",18), bg="skyblue", fg="Blue", command = clicked_safe_mode)
btn10.place(x=420,y=300)






window.mainloop()