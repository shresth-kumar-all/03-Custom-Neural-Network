import pandas as pd

specs=pd.read_csv("startsit.csv")
specs_df=pd.DataFrame(specs)
specs_df=specs_df.transpose()
num_layers=specs_df.shape[1]
widths=specs_df.loc["layer_widths"].tolist()
print(widths)

#weigth_pools:
for c0 in range(0,len(widths)-1):
    w=pd.DataFrame(1,index=range(0,widths[c0]),columns=range(0,widths[c0+1]))
    w.to_csv(f"processing\\Weight_Pools\\W_{c0}-to-{c0+1}.csv",index=False)
    print(w)

#biases:
for c1 in range(0,len(widths)):
    b=pd.DataFrame(0,index=range(0,widths[c1]),columns=range(0,1))
    b.to_csv(f"processing\\Bias_Pools\\B_{c1}.csv",index=False)

#layers:
for c1 in range(0,len(widths)):
    l=pd.DataFrame(0,index=range(0,widths[c1]),columns=range(0,1))
    l.to_csv(f"processing\\Layers\\Layer_{c1}.csv",index=False)