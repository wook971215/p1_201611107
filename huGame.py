import turtle
import math
wn=turtle.Screen()
t1=turtle.Turtle()

def L(pos1,pos2):
    t1.penup()
    t1.setpos(pos1,pos2)
    t1.pendown()
    t1.right(90)
    t1.fd(60)
    t1.left(90)
    t1.fd(30)

def V(pos3,pos4):
    t1.penup()
    t1.setpos(pos3,pos4)
    t1.pendown()
    t1.right(77)
    t1.fd(64)
    t1.left(154)
    t1.fd(64)

def one(pos5,pos6):
    t1.penup()
    t1.setpos(pos5,pos6)
    t1.pendown()
    t1.setheading(0)
    t1.right(90)
    t1.fd(60)

def two(pos7,pos8):
    one(-210,250)
    t1.penup()
    t1.setpos(pos7,pos8)
    t1.pendown()
    t1.setheading(0)
    t1.right(90)
    t1.fd(60)

def three(pos9,pos10):
    two(-200,250)
    t1.penup()
    t1.setpos(pos9,pos10)
    t1.pendown()
    t1.setheading(0)
    t1.right(90)
    t1.fd(60)
    
def four():
    one(-210,250)
    t1.setheading(0)
    V(-200,250)
    
def five():
    t1.setheading(0)
    V(-210,250)

def stageOne():

    x=51200
    root=math.sqrt(x)

    t1.pencolor("Green")
    t1.speed(100)
    t1.penup()
    t1.setpos(80,-80)
    t1.pendown()
    t1.left(135)
    t1.fd(root)
    t1.left(135)
    t1.fd(160)
    t1.left(135)
    t1.fd(root)
    t1.right(135)
    t1.fd(160)
    t1.right(90)
    t1.fd(160)

    t1.pencolor("black")

    def k1():
        t1.forward(160)
    def k2():
        t1.left(45) 
    def k3():
        t1.right(45)
    def k4():
        t1.fd(root)

    wn.onkey(k1, "Up") 
    wn.onkey(k2, "Left")
    wn.onkey(k3, "Right")
    wn.onkey(k4, "Down")
    wn.listen()


def stageTwo():
    t1.pencolor("Green")
    t1.setheading(0)
    t1.speed(100)
    x=51200
    root=math.sqrt(x)
    t1.penup()
    t1.setpos(110,20)
    t1.pendown()
    for i in range(0,5):
        t1.right(144)
        t1.fd(root)

    t1.pencolor("black")

    def k1():
        t1.forward(160)
    def k2():
        t1.left(45) 
    def k3():
        t1.right(45)
    def k4():
        t1.fd(root)

    wn.onkey(k1, "Up") 
    wn.onkey(k2, "Left")
    wn.onkey(k3, "Right")
    wn.onkey(k4, "Down")
    wn.listen()


def stageThree():
    t1.pencolor("Green")
    t1.speed(100)
    t1.penup()
    t1.setpos(-60,60)
    t1.pendown()
    for i in range(0,6):
        t1.write(t1.pos())
        t1.fd(120)
        t1.right(60)
    t1.right(60)
    t1.fd(240)
    t1.setpos(60,60)
    t1.right(60)
    t1.fd(240)
    t1.setpos(-60,60)
    t1.setpos(-120,-43.92)
    t1.setheading(0)
    t1.fd(120)
    t1.write(t1.pos())
    t1.fd(120)

    t1.pencolor("black")

    def k1():
        t1.forward(160)
    def k2():
        t1.left(45) 
    def k3():
        t1.right(45)
    def k4():
        t1.fd(root)

    wn.onkey(k1, "Up") 
    wn.onkey(k2, "Left")
    wn.onkey(k3, "Right")
    wn.onkey(k4, "Down")
    wn.listen()

    
def stageFour():
    t1.pencolor("Green")
    t1.speed(100)
    t1.penup()
    t1.setpos(-60,60)
    t1.pendown()
    for i in range(0,6):
        t1.write(t1.pos())
        t1.fd(120)
        t1.right(60)
    t1.right(60)
    t1.fd(120)
    t1.write(t1.pos())
    t1.right(60)
    t1.fd(120)
    t1.setpos(-60,60)

    t1.pencolor("black")

    def k1():
        t1.forward(160)
    def k2():
        t1.left(45) 
    def k3():
        t1.right(45)
    def k4():
        t1.fd(root)

    wn.onkey(k1, "Up") 
    wn.onkey(k2, "Left")
    wn.onkey(k3, "Right")
    wn.onkey(k4, "Down")
    wn.listen()

    
def stageFive():
    t1.pencolor("Green")
    t1.speed(100)
    t1.penup()
    t1.setpos(-60,60)
    t1.pendown()
    for i in range(0,4):
        t1.fd(120)
        t1.right(90)
        t1.write(t1.pos())
    t1.penup()
    t1.setpos(-120,120)
    t1.pendown()
    for i in range(0,4):
        t1.fd(240)
        t1.right(90)
        t1.write(t1.pos())
    t1.penup()
    t1.setpos(-180,180)
    t1.pendown()
    for i in range(0,4):
        t1.fd(360)
        t1.right(90)
        t1.write(t1.pos())
    tracks=([-60,60],[60,60],[180,180],[180,-180],[60,-60],[-60,-60],[-180,-180],[-180,180])
    for a in range(0,8):
        t1.goto(tracks[a])
    t1.setpos(0,180)
    t1.write(t1.pos())
    t1.right(90)
    t1.fd(60)
    t1.write(t1.pos())
    t1.fd(60)
    t1.write(t1.pos())
    t1.fd(120)
    t1.write(t1.pos())
    t1.fd(60)
    t1.write(t1.pos())
    t1.fd(60)
    t1.write(t1.pos())

    t1.pencolor("black")

    def k1():
        t1.forward(60)
    def k2():
        t1.left(45) 
    def k3():
        t1.right(45)
    def k4():
        t1.back(60)

    wn.onkey(k1, "Up") 
    wn.onkey(k2, "Left")
    wn.onkey(k3, "Right")
    wn.onkey(k4, "Down")
    wn.listen()


def Score():
    global score
    score=score+10
    
    
def drawShapeInOnce():
	answer=raw_input("Are you ready to game? yes or no:")

	if(answer=="yes"):
		print "welcome to game world"

		print "This game is %s" %("[draw shape in once]")

	
		t1.shape("turtle")

		wn.bgpic("bg.gif")

		print "Level 1"
	
		L(-300,250)
		V(-270,250)
		one(-210,250)

	
		t1.penup()
		t1.home()
		t1.setheading(0)
		t1.pendown()

		stageFive()

		wn.exitonclick()

	elif(answer=="no"):
 		print "Bye Bye"


def main():
    drawShapeInOnce() 

if __name__=="__main__":
    main() 

raw_input()
