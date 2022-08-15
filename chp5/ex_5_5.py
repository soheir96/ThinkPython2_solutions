import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n) # fd = turtle moves forward 
    t.lt(angle) # lt = turtle turns left 
    draw(t, length, n-1)
    t.rt(2*angle) # rt = turtle turns right 
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n) # bk = turtle moves backward 

bob = turtle.Turtle()
draw(bob, 10, 5)

