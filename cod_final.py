from turtle import *    #importam modulul turtle
from random import randint    #importam modulul random

speed("fastest")

#personalizarea testoaselor
miSHELL = Turtle()
speedy = Turtle()
snappy = Turtle()
turtleContur = Turtle()
speedy.speed(0)
snappy.speed(0)
miSHELL.speed(0)

miSHELL.shape("turtle") #setam forma testoasei miSHELL
speedy.shape("turtle")  #setam forma testoasei speedy
snappy.shape("turtle")  #setam forma testoasei snappy

#personalizarea fundalului

bgcolor("mint cream")    #setarea culorii de fundal
setup(450, 450) #setarea dimenisunilor ecranului

#setam stiloul "up" pentru a ne deplasa fara trasare

miSHELL.penup()
speedy.penup()
snappy.penup()

#pozitionarea testoaselor

miSHELL.goto(400, 400)
speedy.goto(0, 0)
snappy.goto(0, 0)

miSHELL.hideturtle()
miSHELL.goto (-50,150)
miSHELL.write("together we can")
miSHELL.goto (400,400)

def dreptunghi(lungime, latime, culoareContur, culoareUmplere, trtl): #definim functia dreptunghi cu parametri pentru lungime, latime, culori si testoasa care va executa desenul
    trtl.pendown()
    trtl.color(culoareContur,culoareUmplere)
#    trtl.fillcolor(culoareUmplere)
    trtl.begin_fill()
    for _ in range(2):
        trtl.fd(lungime)
        trtl.lt(90)
        trtl.fd(latime)
        trtl.lt(90)
    trtl.end_fill()
#dreptunghi(50, 50, 30, 20, "pink", "yellow", speedy)

def triunghi(lungime, culoareContur, culoareUmplere, trtl): #definim functia dreptunghi cu parametri pentru lungime, latime, culori si testoasa care va executa desenul
    trtl.pendown()
    trtl.pencolor(culoareContur)
    trtl.fillcolor(culoareUmplere)
    trtl.begin_fill()
    for _ in range(3):
        trtl.fd(lungime)
        trtl.lt(120)
    trtl.end_fill()
#triunghi(100, 100, 30, "pink", "pink", snappy)


def cerc(x, y, culoareContur, culoareUmplere): #definim functia dreptunghi cu parametri pentru lungime, latime, culori si testoasa care va executa desenul
    turtleContur.pendown()
    turtleContur.pencolor(culoareContur)
    turtleContur.fillcolor(culoareUmplere)
    begin_fill()
    turtleContur.pendown()
    turtleContur.goto(x, y)
    for _ in range(180):
        trtl.fd(2)
        trtl.lt(2)
    end_fill()
#cerc(60, 60, "pink", "black")

    
def hexagon(x, y, lungime, culoareContur, culoareUmplere, trtl):
    trtl.pendown()
    trtl.pencolor(culoareContur)
    begin_fill()
    trtl.fillcolor(culoareUmplere)
    trtl.goto(x, y)
    for _ in range(6):
        trtl.fd(lungime)
        trtl.lt(60)
#hexagon(200, 200, 30, "green", "green", miSHELL)

#turtleContur.penup()
#turtleContur.goto(-100, -150)
#turtleContur.pendown()
#turtleContur.fd(200)

#for _ in range(3):
#    turtleContur.fd(20)
#    for _ in range(60):
#        turtleContur.fd(1)
#        turtleContur.lt(3)
#    turtleContur.fd(20)
#    turtleContur.lt(180)



#baza led

speedy.goto(-100, -150)
dreptunghi(30, 20, "black", "olive", speedy)
speedy.fd(30)
dreptunghi(50, 20, "black", "olive", speedy)
speedy.fd(50)
dreptunghi(20, 20, "black", "olive", speedy)
speedy.fd(20)
dreptunghi(70, 20, "black", "olive", speedy)
speedy.fd(70)
dreptunghi(30, 20, "black", "olive", speedy)
speedy.fd(30)
speedy.bk(200)

speedy.goto(-100, -130)
dreptunghi(50, 20, "black", "olive", speedy)
speedy.fd(50)
dreptunghi(40, 20, "black", "olive", speedy)
speedy.fd(40)
dreptunghi(10, 20, "black", "olive", speedy)
speedy.fd(10)
dreptunghi(40, 20, "black", "olive", speedy)
speedy.fd(40)
dreptunghi(60, 20, "black", "olive", speedy)
speedy.fd(60)
speedy.bk(200)

speedy.goto(-100, -110)
dreptunghi(40, 20, "black", "olive", speedy)
speedy.fd(40)
dreptunghi(60, 20, "black", "olive", speedy)
speedy.fd(60)
dreptunghi(20, 20, "black", "olive", speedy)
speedy.fd(20)
dreptunghi(20, 20, "black", "olive", speedy)
speedy.fd(20)
dreptunghi(60, 20, "black", "olive", speedy)
speedy.fd(60)
speedy.bk(200)





def tree(lungime,t):
    if lungime > 5:
        t.forward(lungime)
        t.right(20)
        tree(lungime-7,t)
        t.left(40)
        tree(lungime-7,t)
        t.right(20)
        t.backward(lungime)

def main():
    t = Turtle()
    t.speed(0)
    myWin = Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()



