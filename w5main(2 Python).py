import turtle
wn=turtle.Screen()
print "Rock Scissors Paper Games!"
print "Input R,S,P"

def gawibawibo():
    UserX = raw_input("Ux : ")
    UserY = raw_input("Uy : ")

    S="Scissors"
    R="Rock"
    P="Paper"

    if(UserX==UserY):
        print "Draw"
    
    elif(UserX=="S"):
        if(UserY=="P"):
            print 'S Win'
        elif(UserY=="R"):
            print 'R Win'
        
    elif(UserX=="R"):
        if(UserY=="P"):
            print 'P Win'
        elif(UserY=="S"):
            print 'R Win'  
        
    elif(UserX=="P"):
        if(UserY=="S"):
            print 'S Win'
        elif(UserY=="R"):
            print 'P Win' 
    else:
        print 'Input Error'

def replay():
	sel=raw_input("Do you want one more time? y or n :")
	if(sel=='y'):
		rsp()
	else:
		print "Click white Screen! Good Bye~"
def rsp():
	gawibawibo()
	replay()
rsp()

wn.exitonclick()