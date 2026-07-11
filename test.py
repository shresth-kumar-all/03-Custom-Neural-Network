import pandas as pd
import numpy as np
'''
x=pd.read_csv("list_test.csv")
y=list(x["0"].to_list()[0])
#print(y)

################################################

#download:
a=[]
a_backup=[]
mem=[]
for c in range(0,len(y)):
    if y[c] in {',','#'}:
        s1="".join(mem)
        a.append(float(s1))
        a_backup.append(float(s1))
        mem=[]

    else:
        mem.append(y[c])

#print(a)

################################################

#say after processing we add -0.98 to the list:
a.append(-0.98)
a_backup.append(-0.98)
#print(a)

#upload:
up_0=list(f"{a}")
remove=['[',']']
for c in range(0,len(remove)):
    up_0.remove(remove[c])
up_0.append("#")

for c in range(0,up_0.count(" ")):
    up_0.remove(" ")

b="".join(up_0)
print(b)
'''
#########################################################################################################

a=[1,2,3,4]
in_layer=pd.DataFrame()
in_layer["0"]=a
print(in_layer["0"].tolist())