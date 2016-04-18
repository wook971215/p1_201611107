"""
@author JHU
@since 160418
"""


import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

t1.home()
t1.clear()

def drawSquareFrom():
	tracks=([100,0],[100,100],[0,100],[0,0])
	t1.pendown()
	for i in range(0,4):
		t1.goto(tracks[i])
        
def lab7():
    drawSquareFrom()
    wn.exitonclick()

def main():
    lab7()

if __name__=="__main__":
    main()
