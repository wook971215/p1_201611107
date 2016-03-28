import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def makeSwirlSquare(size,bigger,sides,angle):
     for i in range(0,sides):
          if(i%2):
              size=size+bigger
          t1.fd(size)
          t1.right(90)

makeSwirlSquare(10,10,20,90)

wn.exitonclick()