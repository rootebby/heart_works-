import turtle
import os
import time

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)



def duygu():
    turtle.speed(5)
    turtle.bgcolor("black")

    turtle.color("red", "pink")        

    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(111.65)
    curve()

    turtle.left(120)
    curve()
    turtle.forward(111.65)
    turtle.end_fill()
    turtle.hideturtle()

def sorry():
    if os.name == "posix":    
        os.system("shutdown -P now")
    elif os.name == "nt":
        os.system("shutdown -s -f -t 5")
    else:
        pass
    
while True:
    print("""
            *************************
            | SENİ ÇOOK SEVİYORUMM !|
            *************************
            | 1. BENDE SENİ <3      |
            *************************
            | 2. ÜZGÜNÜM ... :(     |
            *************************

    """)

    x = int(
        input("==>>> ")
    )

    if x == 1:
        duygu()

    elif x == 2:
        sorry()

    else:
        print("üf uğraştırma !!!")







