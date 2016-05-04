def charCount():
    d=dict()
    word=raw_input('input word :')
    
    for c in word:
        if c not in d:
            d[c]=1
	else:
            d[c]=d[c]+1
    
	print d

    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(D)),H.values(),align='center')
    plt.xticks(range(len(D)),list(D.keys()))
    plt.show()

def adressCount():
    import matplotlib
    import matplotlib.pyplot as plt

    word = 'Hongji 2gil 20,Jongrogu,Seoul'

    D=dict()
    D['str']=0
    D['int']=0
    for i in word:


        if i.isalpha():
                D['str']=D['str']+1
        elif i.isdigit:
                D['int']=D['int']+1
    print D


    plt.bar(range(len(D)),D.values(),align='center')
    plt.xticks(range(len(D)),list(H.keys()))
    plt.show()


def electronics(a,b):
    print "우리집"
    print a
    print "친구집"
    print b
    print "우리 집에 없지만 친구 집에 있는 가전제품" 
    print b.difference(a)
    print "친구 집에 없지만 우리 집에 있는 가전제품" 
    print a.difference(b)
    print "모든 집에 같이 있는 가전제품 "
    print a.intersection(b)
    print "어느 한 집에라도 있는 가전제품"
    print a.union(b)
    
def countElectronics(x,y):
    dict=dict()
    for i in x:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]=dict[i]+1

    for i in y:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]=dict[i]+1

    return dict

def lab9_1():
    charCount()

def lab9_2():
    adress()

def lab9_3():
    mh={'TV','phone','camera','fridger','mixer','audio','cd player','light','computer','notebook','recorder'}
    fh={'coffee machine','radio','camera','running machine','ramp','computer','notebook','recorder'}
    electronics(mh,fh)
    result3=countElectronics(mh,fh)
    print result3

def main():
    lab9_1()
    lab9_2()
    lab9_3()

if __name__=="__main__":  
     main()  