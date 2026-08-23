import pandas as pd
import numpy as np

def fom(m_):
    a_=20 #learning rate: higher the value, slower it learns but better accuracy probably idk
    if m_ == 0:
        return 0
    else:
        func=(np.absolute(m_)/m_)*((np.log10(np.absolute(m_) + 1))/np.log10(a_)) #func is susceptible to 0/0 nan errors but numpy doesnt generate those errors
        return func

'''
weight_hist=pd.read_csv("processing\\Weight_History\\Whist_0-to-1.csv")
weight_hist_specs=weight_hist.shape

for c0_1 in range(0,weight_hist_specs[0]):
    curr_set=weight_hist.iloc[c0_1].tolist()

    for c0_1_1 in range(0,len(curr_set)):
        x=curr_set[c0_1_1]
        #download
        y=list(x)
        y.pop(0)
        y.pop(-1)
        y.append("#")
        a=[]
        mem=[]
        for c in range(0,len(y)):
            if y[c] in {',','#'}:
                s1="".join(mem)
                a.append(float(s1))
                mem=[]

            else:
                mem.append(y[c])

                
print(weight_hist)
'''
a="0.123"
b="0.1234567890808480843058345"
print(float(a),float(b))