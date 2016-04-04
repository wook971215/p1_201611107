import turtle
wn=turtle.Screen()

print "Draw star triangle!"
print "input size"

nMax=raw_input("size:")
nMax=int(nMax)

for i in range(nMax):
    print " "*(nMax-i)+"*"*(i*2-1)

wn.exitonclick()