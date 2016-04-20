def saveTracks():
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    t1.speed(3)
    t1.penup()
    mT=list()
    t1.goto(-300,300)
    t1.pendown()
    t1.setheading(0)
    t1.fd(100)
    mT.append(t1.pos())
    t1.right(90)
    t1.fd(100)
    mT.append(t1.pos())
    t1.left(90)
    t1.fd(100)
    mT.append(t1.pos())
    t1.right(90)
    t1.fd(300)
    mT.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    mT.append(t1.pos())
    t1.left(90)
    t1.fd(100)
    mT.append(t1.pos())
    t1.right(90) 
    t1.fd(100)
    mT.append(t1.pos())
    t1.right(90)
    t1.fd(350)
    mT.append(t1.pos())
    return mT

def replayTracks(mT):
    for i in mT:
        print i


def lab7():
    mT=saveTracks()
    replayTracks(mT)

def main():
    lab7()
    raw_input()
if __name__=="__main__":
    main()