def distances():
    
    Locations=list()


    Locations=[(37.513271, 127.101117),(37.517189, 127.041269),(37.565705, 126.976866),(37.559776, 126.942297),(37.556846, 126.923774)]

    distances=list()

    for loc in Locations:
        print "x={} y={}".format(loc[0],loc[1])

    for x in range(0,4):
        import math
        print math.sqrt((Locations[x][0]-Locations[x+1][0])**2+(Locations[x][1]-Locations[x+1][1])**2)
        distances.append(math.sqrt((Locations[x][0]-Locations[x+1][0])**2+(Locations[x][1]-Locations[x+1][1])**2))
    print "------------------------------------------"
    print "This is minimum result"

    print min(distances)
    
distances()

raw_input()