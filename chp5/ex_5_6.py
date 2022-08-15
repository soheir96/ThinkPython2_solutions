# To draw a Koch curve with length x, all you have to do is
# 1. Draw a Koch curve with length x/3.
# 2. Turn left 60 degrees.
# 3. Draw a Koch curve with length x/3.
# 4. Turn right 120 degrees.
# 5. Draw a Koch curve with length x/3.
# 6. Turn left 60 degrees.
# 7. Draw a Koch curve with length x/3.
# The exception is if x is less than 3: in that case, you can just draw a straight line with length x.

import turtle 

def koch(t, l):
    '''Draws a koch curve with length l'''
    if l < 3:
        t.fd(l)
        return
    koch_length = l / 3
    koch(t,koch_length)
    t.lt(60)
    koch(t,koch_length)
    t.rt(120)
    koch(t,koch_length)
    t.lt(60)
    koch(t,koch_length)

bob = turtle.Turtle()

def snowflake(t,l):
    '''Draws a snowflake (a triangle with a Koch curve for each side).'''
    for i in range(3):
        koch(t, l)
        t.rt(120)

bob.pu()
bob.goto(-150, 90)
bob.pd()
snowflake(bob, 300)

turtle.mainloop()