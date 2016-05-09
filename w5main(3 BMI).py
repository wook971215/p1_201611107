"""
@author huj
@since 160404
"""
import turtle
wn=turtle.Screen()

print "Let's measure BMI"
print "Input your height,weight with float please!"

height=raw_input("input your height:")
weight=raw_input("input your weight:")

height=float(height)
weight=float(weight)

def computerBMI(height,weight):

    bmi=weight/height*height

    print bmi

    if bmi>=18.5 and bmi<25.0:
        print "NormalWeight"
    elif bmi>=25.0 and bmi<=30.0:
        print "OverWeight"
    elif bmi<18.5:
        print "UnderWeight"
    elif bmi>=30.0:
        print "Obesity"
    else:
        print "Error!"

def lab5():
    computerBMI(height,weight)

def main():
    lab5()
    
if __name__=="__main__":
    main()

wn.exitonclick()