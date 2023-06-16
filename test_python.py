# mon programme permet de lancer le module turtle et de tracer des segments


from turtle import *

def carre():
    #reset()
    i=1
    while i<=4:
        forward(100)
        left(90)
        i=i+1


    def serieCarre():
         reset()
    up()
    color("red")
    down()
    i=1
    d=10
    while i<=n:
        carre()
        up()
        forward(100+d)
        down()
        i=i+1

    serieCarre()