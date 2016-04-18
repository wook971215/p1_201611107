import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def drawSquare(pos1,pos2,size):
    tracks=list()
    t1.penup()
    t1.goto(pos1,pos2)
    t1.pendown()
    for i in range(0,4):
        t1.forward(size)
        t1.right(90)    
        tracks.append(t1.pos())
    return tracks
    

def main():
    mytracks=drawSquare(0,0,90)
    print mytracks
    wn.exitonclick()


if __name__=="__main__":
    main()

