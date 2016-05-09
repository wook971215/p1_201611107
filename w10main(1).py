Rate=[["Coffee","Water","Milk","Icecream"],
  ["Espresso","No","No","No"],
  ["Long Black","Yes","No","No"],
 ["Flat White","No","Yes","No"],
 ["Cappuccino","No","Yes - Frothy","No"],
 ["Affogato","No","No","Yes"]]

data= Rate[1:]
datav=list()

for i in data:
    if i[2]=="Yes" or i[2]=="Yes - Frothy":
        datav.append(i[0])
        
float(len(data))/float(len(datav))