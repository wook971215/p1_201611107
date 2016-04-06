import turtle
wn=turtle.Screen()

print "Sum of Multiples of 3 or 5!"

begin=raw_input("input begin number:")

end=raw_input("input end number:")

begin=int(begin)
end=int(end)

def sumOfMultiplesOf3_5(begin,end):
    sum=0
    for i in range(begin,end):
        if i%3==0 or i%5==0:
            sum=sum+i
    print sum
    return sum

sumOfMultiplesOf3_5(1,1000)

wn.exitonclick()