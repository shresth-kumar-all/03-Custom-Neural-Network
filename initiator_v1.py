import pandas as pd
import random as r

def ini(_startsit):
    specs=pd.read_csv(_startsit)
    specs_df=pd.DataFrame(specs)
    specs_df=specs_df.transpose()
    num_layers=specs_df.shape[1]
    widths=specs_df.loc["layer_widths"].tolist()

    #weigth_Pools + weight_History:
    for c0 in range(0,len(widths)-1):
        w=pd.DataFrame(1,index=range(0,widths[c0]),columns=range(0,widths[c0+1]),dtype=float)
        w1=pd.DataFrame(1,index=range(0,widths[c0]),columns=range(0,widths[c0+1]),dtype=object)
        shape=w.shape
        print(shape)
        for c1 in range(0,shape[0]):
            send_r=[float(r.randint(-100,100)/100) for i in range(0,shape[1])]
            send_r1=[]
            for j in range(0,shape[1]):
                tosend=[send_r[j]]
                send_r1.append(tosend)
            w.iloc[c1]=send_r
            w1.iloc[c1]=send_r1
        w.to_csv(f"processing\\Weight_Pools\\W_{c0}-to-{c0+1}.csv",index=False)
        w1.to_csv(f"processing\\Weight_History\\Whist_{c0}-to-{c0+1}.csv",index=False)

    #biases:
    for C1 in range(0,len(widths)):
        b=pd.DataFrame(0,index=range(0,widths[C1]),columns=range(0,1))
        b.to_csv(f"processing\\Bias_Pools\\B_{C1}.csv",index=False)

    #layers:
    for C2 in range(0,len(widths)):
        l=pd.DataFrame(0,index=range(0,widths[C2]),columns=range(0,1))
        l.to_csv(f"processing\\Layers\\Layer_{C2}.csv",index=False)

    #Coordination Factor:
    cf=0
    cf_df=pd.DataFrame({"cf":[cf]})
    cf_df.to_csv("processing\\coordination_factor.csv",index=False)

    #rms_errors:
    e_df=pd.DataFrame({"e_rms":[]})
    e_df.to_csv("processing\\rms_errors.csv",index=False)

print("\nfile initialisation...V\n")