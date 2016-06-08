import turtle
import math
import time
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()

x=float()
y=float()
point=float()
point = 0

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
    two(-190,250)
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

    t1.speed(100)
    t2.penup()
    t1.penup()
    t1.setpos(80,-80)
    t1.pencolor("White")
    t1.write("★")
    t1.pencolor("Green")
    t1.pendown()
    t1.left(135)
    t1.fd(root)
    t1.pencolor("White")
    t1.write("★")
    t1.pencolor("Green")
    t1.left(135)
    t1.fd(160)
    t1.pencolor("White")
    t1.write("★")
    t1.pencolor("Green")
    t1.left(135)
    t1.fd(root)
    t1.pencolor("White")
    t1.write("★")
    t1.pencolor("Green")
    t1.right(135)
    t1.fd(160)
    t1.pencolor("White")
    t1.write("★")
    t1.pencolor("Green")
    t1.right(90)
    t1.fd(160)
    t1.pencolor("White")
    t1.write("★")
    t1.pencolor("Green")

    t1.penup()
    t2.shape("turtle")
    t2.setpos(-80,-80)
    t2.penup()
    t2.pendown()
    t2.setheading(0)

    def k1():
    	t2.fd(160)
	(x,y)=t2.pos()
	global point
	if 60<=x<=100 and 60<=y<=100:
		point=point+10
		print "Your point is %d !" % point
	if -100<=x<=-60 and 60<=y<=100:
		point=point+10
		print "Your point is %d !" % point
	if -100<=x<=-60 and -100<=y<-60:
		point=point+10
		print "Your point is %d !" % point
	if 60<=x<=100 and -100<=y<-60:
		point=point+10
		print "Your point is %d !" % point
	if point==50:
		print"-----------------------------------"
		print"You Win, Go next stage!"
		t1.clear()
		t2.clear()
		point=0

		stageTwo()
	if point>50:
		print"-----------------------------------"
		print"Game over! Press Q"
    
    def k2():
        t2.left(45)
    def k3():
        t2.right(45)
    def k4():
        t2.fd(root)
	(x,y)=t2.pos()
	global point
	if 60<=x<=100 and 60<=y<=100:
		point=point+10
		print "Your point is %d !" % point
	if -100<=x<=-60 and 60<=y<=100:
		point=point+10
		print "Your point is %d !" % point
	if -100<=x<=-60 and -100<=y<-60:
		point=point+10
		print "Your point is %d !" % point
	if 60<=x<=100 and -100<=y<-60:
		point=point+10
		print "Your point is %d !" % point
	if point==50:
		print"-----------------------------------"
		print"You Win, Go next stage!"
		t1.clear()
		t2.clear()
		stageTwo()
		point=0
	if point>50:
		print"-----------------------------------"
		print"Game Over! Press Q"

    wn.onkey(k1, "Up") 
    wn.onkey(k2, "Left")
    wn.onkey(k3, "Right")
    wn.onkey(k4, "Down")
    wn.listen()


def stageTwo():

    print "Move Only 5"
    print "Level 2"
    global point
    t1.setheading(0)
    t1.pencolor("black")
    L(-300,250)
    V(-270,250)
    two(-190,250)
    t1.pencolor("Green")
    t1.setheading(0)
    t1.speed(100)
    x=51200
    root=math.sqrt(x)
    t1.penup()
    t1.setpos(110,20)
    t2.setheading(0)
    t1.pendown()
    for i in range(0,5):
	t1.pencolor("White")
        t1.write("★")
        t1.pencolor("Green")
        t1.right(144)
        t1.fd(root)

    t1.pencolor("black")

    t2.penup()
    t2.setpos(110,20)
    t2.pendown()

    def k1():
        t2.forward(root)
	(x,y)=t2.pos()
	global point
	if 90<=x<130 and 0<=y<=40:
		point=point+10
		print "Your point is %d !" % point
        if -93<=x<=-53 and -133<=y<=-93:
		point=point+10
		print "Your point is %d !" % point
	if -23<=x<=17 and 82<=y<=122:
		point=point+10
		print "Your point is %d !" % point
	if 46<=x<=86 and -133<=y<=-93:
		point=point+10
		print "Your point is %d !" % point
	if -136<=x<=-96 and 0<=y<=40:
		point=point+10
		print "Your point is %d !" % point
	if point==50:
		print"-----------------------------------"
		print"You Win, Go next stage!"
		t1.clear()
		t2.clear()
		point=0
		stageFour()
	if point>50:
		print"-----------------------------------"
		print"Game Over! Press Q"

	
    def k2():
        t2.left(144) 
    def k3():
        t2.right(144)

    wn.onkey(k1, "Up") 
    wn.onkey(k2, "Left")
    wn.onkey(k3, "Right")
    wn.listen()


def stageThree():

    global point
    t1.setheading(0)
    t1.pencolor("black")
    L(-300,250)
    V(-270,250)
    three(-170,250)

    t1.setheading(0)
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
        t2.forward(160)
	(x,y)=t2.pos()
	global point
    def k2():
        t2.left(45) 
    def k3():
        t2.right(45)
    def k4():
        t2.fd(root)

    wn.onkey(k1, "Up") 
    wn.onkey(k2, "Left")
    wn.onkey(k3, "Right")
    wn.onkey(k4, "Down")
    wn.listen()

    
def stageFour():

    L(-300,250)
    V(-270,250)
    three(-170,250)
    global point
    x=19200
    root=math.sqrt(x)
    print"-----------------------------------"
    print "Move Only 5"
    print "Level 3"
    t1.setheading(0)
    t1.pencolor("Green")
    t1.speed(100)
    t1.penup()
    t1.setpos(-60,60)
    t1.pendown()
    for i in range(0,6):
        t1.write(t1.pos())

    	t1.pencolor("White")
 	t1.write("★")
    	t1.pencolor("Green")

        t1.fd(120)
        t1.right(60)

    t1.setpos(-60,-147)
    t1.pencolor("White")
    t1.write("★")
    t1.pencolor("Green")


    t1.pencolor("black")
    t2.penup()
    t2.setpos(-60,60)
    t2.pendown()
    t2.setheading(0)

    def k1():
        t2.forward(120)

	(x,y)=t2.pos()
	if -80<x<-40 and 40<y<80:
		point=point+10	
		print "Your point is %d !" % point
	if -140<x<100 and -63<y<-23:
		point=point+10
		print "Your point is %d !" % point
	if -80<x<-40 and -167<y<-127:
		point=point+10
		print "Your point is %d !" % point
	if 40<x<80 and 40<y<80:
		point=point+10
		print "Your point is %d !" % point
	if 100<x<140 and -63<y<-23:
		point=point+10
		print "Your point is %d !" % point
	if 40<x<80 and -167<y<-127:
		point=point+10
		print "Your point is %d !" % point
	if point==70:
		print"-----------------------------------"
		print"You Win, End game~"
	if point>70:
		print"-----------------------------------"
		print"Game Over! Press Q"
    def k2():	
        t2.left(60) 
    def k3():
        t2.right(60)
    def k4():
        t2.fd(83)

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
    global point
    played=open('save.txt', 'a')
    if point==170:
        name = raw_input("Put in your name: ")
        msg='played {0}'.format(name + '\t' + time.strftime('%Y.%m.%d , %H:%M:%S'))
        print("End Game"+'\n'+'Score' + '\t'+ str(result) +'\t' + msg)
        played.write('\n' + 'Score' + '\t'+ str(result) +'\t' + msg)
        played.close()
        print("Click Screen")
    
    
def drawShapeInOnce():
	answer=raw_input("Are you ready to game? yes or no:")

	if(answer=="yes"):
		print "welcome to game world"

		print "This game is %s" %("[draw shape in once]")

		print "Move Only 5"
	
		t1.shape("turtle")

		wn.bgcolor("Lightpink")

		print "Level 1"
	
		L(-300,250)
		V(-270,250)
		one(-210,250)

	
		t1.penup()
		t1.home()
		t1.setheading(0)
		t1.pendown()

		stageOne()


	elif(answer=="no"):
 		print "Bye Bye"



def main():
    drawShapeInOnce() 

if __name__=="__main__":
    main()
    turtle.mainloop()
