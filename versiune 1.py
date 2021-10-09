from turtle import *    #importam modulul turtle
from random import randint    #importam modulul random

#personalizarea testoaselor
miSHELL = Turtle()
speedy = Turtle()
snappy = Turtle()

miSHELL.shape("turtle") #setam forma testoasei miSHELL
speedy.shape("turtle")  #setam forma testoasei speedy
snappy.shape("turtle")  #setam forma testoasei snappy

#personalizarea fundalului
bgcolor("white")    #setarea culorii de fundal
setup(450, 450) #setarea dimenisunilor ecranului

#setam stiloul "up" pentru a ne deplasa fara trasare
miSHELL.penup()
speedy.penup()
snappy.penup()

#pozitionarea testoaselor
miSHELL.goto(randint(-100, +100), randint(-100, 100))
speedy.goto(randint(-200, 200), randint(-200, 200))
snappy.goto(randint(-200, 200), randint(-200, 200))

def dreptunghi(lungime, latime, culoare_contur, culoare_umplere, trtl): #definim functia dreptunghi cu parametri pentru lungime, latime, culori si testoasa care va executa desenul
    trtl.pendown()
    trtl.pencolor(culoare_contur)
    trtl.fillcolor(culoare_umplere)
    begin_fill()
    for _ in range(2):
        trtl.fd(lungime)
        trtl.lt(90)
        trtl.fd(latime)
        trtl.lt(90)
    end_fill()
dreptunghi(30, 20, "pink", "yellow", speedy)
