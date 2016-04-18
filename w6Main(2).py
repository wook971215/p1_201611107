def drawSquare(pos1,pos2,size):
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    t1.home()
    t1.clear()
    tracks=list()
    t1.penup()
    t1.goto(pos1,pos2)
    t1.pendown()
    for i in range(0,4):
        t1.forward(size)
        t1.right(90)    
        tracks.append(t1.pos())
    return tracks
    print tracks
    
    wn.exitonclick()


def main():
    drawSquare(0,0,100)

if __name__=="__main__":
    main()

