""" 
@author John 
@since 160411 
""" 



y=list()

def sumList(y):
    for i in range(1,1000):
        if i%4==0 and not i%5==0:
            y.append(i)
    sum=0
    for i in range(0,len(y)):
        sum+=y[i]
    return sum

print sumList(y)

raw_input()

def main():
	sumList(y)

if __name__=="__main__": 
     main() 
