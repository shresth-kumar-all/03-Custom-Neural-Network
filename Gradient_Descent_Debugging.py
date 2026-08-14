import pandas as pd
import numpy as np

_startsit="01-initialization_criteria\\startsit.csv"
_traindata="02-Training_Data\\tts_train_0.8.csv"

#importing assets for comparison:
specs=pd.read_csv(_startsit)
specs_df=pd.DataFrame(specs)
layers=specs_df["layer_widths"].tolist() #list of layers
num_layers=len(layers) #no. of layers
last=num_layers - 1
last_L=pd.read_csv(f"processing\\Layers\\Layer_{last}.csv")
out_model=pd.DataFrame(last_L) #model output
print("out_model: \n",out_model)

train_data=pd.read_csv(_traindata)
train_data_df=pd.DataFrame(train_data)

#Coordinating with other files:
c=pd.read_csv("processing\\coordination_factor.csv")
cf=c["cf"].to_list()[0]
print(cf)

##########################################################################################################

#RMS Error:

    #customize to match the output structure of the data:
out_real_list=train_data_df.iloc[cf].to_list()
out_real_val=out_real_list[-1]
if out_real_val == 0:
    to_form=[1,0]
    out_real=pd.DataFrame(to_form)
    out_real.columns=["0"]
elif out_real_val == 1:
    to_form=[0,1]
    out_real=pd.DataFrame(to_form)
    out_real.columns=["0"]

e=out_model - out_real
e2=e*e
sum_e2=e2.sum().to_list()
e_rms=(sum_e2[0])**(1/2)  #rms error calculation concluded
print(e_rms)
##########################################################################################################

if cf == 0:
    rms_errors=pd.DataFrame({"e_rms":[e_rms]},dtype=float)
    rms_errors.to_csv("processing\\rms_errors.csv",index=False)
else:
    rms_errors_csv=pd.read_csv("processing\\rms_errors.csv")
    rms_errors_prev=pd.DataFrame(rms_errors_csv)
    rms_errors_new=pd.DataFrame({"e_rms":[e_rms]},dtype=float)
    rms_errors=pd.concat([rms_errors_prev,rms_errors_new],ignore_index=True)
    rms_errors.to_csv("processing\\rms_errors.csv",index=False)

##########################################################################################################

errors_csv=pd.read_csv("processing\\rms_errors.csv")
errors_df=pd.DataFrame(errors_csv)
errors_list=errors_df["e_rms"].tolist()
 
#grdient descent function:
def fom(m_):
    a_=20 #learning rate: higher the value, slower it learns but better accuracy probably idk
    if m_ == 0:
        return 0
    else:
        func=(np.absolute(m_)/m_)*((np.log10(np.absolute(m_) + 1))/np.log10(a_)) #func is susceptible to 0/0 nan errors but numpy doesnt generate those errors
        return func

if len(errors_list) < 2:
    for c0 in range(1,num_layers):
        weights=pd.read_csv(f"processing\\Weight_Pools\\W_{c0-1}-to-{c0}.csv")
        weight_hist=pd.read_csv(f"processing\\Weight_History\\Whist_{c0-1}-to-{c0}.csv")

        weight_hist_specs=weight_hist.shape

        weights+=1

        for c0_1 in range(0,weight_hist_specs[0]):
            curr_set=weight_hist.iloc[c0_1].tolist()
            curr_update=weights.iloc[c0_1].tolist()

            for c0_1_1 in range(0,len(curr_set)):
                update=curr_update[c0_1_1]
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
                a.append(update)
                curr_set[c0_1_1]=f"{a}"

            weight_hist.iloc[c0_1]=curr_set

        weights.to_csv(f"processing\\Weight_Pools\\W_{c0-1}-to-{c0}.csv",index=False)
        weight_hist.to_csv(f"processing\\Weight_History\\Whist_{c0-1}-to-{c0}.csv",index=False)

##########################################################################################################