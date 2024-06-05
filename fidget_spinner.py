from turtle import *
state={'turn':0}

def spinner():
    #spinner design
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)
    update()
    
def animate():
    #animation of turning
    if state['turn']>0:
        state['turn']-=1
    spinner()
    ontimer(animate, 20)
    
def flick():
    state['turn']+=10
    
#main call
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()

#keep pressing space bar continuously to turn the fidget spinner
#the spinner will slow down and eventually stop when you release the space bar and stop pressing it