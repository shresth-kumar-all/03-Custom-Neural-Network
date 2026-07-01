import pandas as pd
x=pd.DataFrame([1,2,3])
y=pd.DataFrame([1,2,3])
print(type(x*y))
x.iloc[0]=1000000000
print(x)
print(float(x.sum().iloc[0]))