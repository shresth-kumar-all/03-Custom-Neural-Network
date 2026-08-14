import pandas as pd

x=pd.read_csv("list_test.csv")
print(x)
y=list(x["0"].to_list()[0]) #replace with the string of the list which is to be converted
y.pop(0)
y.pop(-1)
y.append("#")

#download:
a=[]
mem=[]
for c in range(0,len(y)):
    if y[c] in {',','#'}:
        s1="".join(mem)
        a.append(float(s1))
        mem=[]

    else:
        mem.append(y[c])

print(a) # the list "a" has the list in usable form from the csv file