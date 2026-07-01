#inputs:
Weightxin=[] #from prev layer

#internal:
bias=0 #alterable
activation_func="codeup"

#processing:
sum=0
for c0 in range(0,len(Weightxin)):
    sum+=Weightxin[c0]

#output:
out=sum
print(out)