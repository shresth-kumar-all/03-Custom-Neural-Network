import pandas as pd
import numpy as np

def learner(_startsit,_traindata):
    #_startsit="01-initialization_criteria\\startsit.csv"
    #_traindata="02-Training_Data\\tts_train_0.8.csv"

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
            return float(func)

    ##########################################################################################################

    if len(errors_list) <= 2:
        for c0 in range(1,num_layers):
            weights=pd.read_csv(f"processing\\Weight_Pools\\W_{c0-1}-to-{c0}.csv")
            weight_hist=pd.read_csv(f"processing\\Weight_History\\Whist_{c0-1}-to-{c0}.csv")

            weight_hist_specs=weight_hist.shape

            weights+=1
            weights=round(weights,2)

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
    else:
        for c1 in range(1,num_layers):
            weights=pd.read_csv(f"processing\\Weight_Pools\\W_{c1-1}-to-{c1}.csv")
            weight_hist=pd.read_csv(f"processing\\Weight_History\\Whist_{c1-1}-to-{c1}.csv")
            e_l=pd.read_csv("processing\\rms_errors.csv")
            e_list=e_l["e_rms"].tolist()
            weight_hist_specs=weight_hist.shape
            print("weights:\n",weights)
            print("\nweights_hist:\n",weight_hist)

            for c1_1 in range(0,weight_hist_specs[0]):
                curr_set=weight_hist.iloc[c1_1].tolist()
                curr_update=weights.iloc[c1_1].tolist()

                for c1_1_1 in range(0,len(curr_set)):
                    w0=curr_update[c1_1_1]

                    x=curr_set[c1_1_1]
                    #download
                    y=list(x)
                    y.pop(0)
                    y.pop(-1)
                    y.append("#")
                    a=[]
                    a_backup=[] #downloaded list
                    mem=[]
                    for c in range(0,len(y)):
                        if y[c] in {',','#'}:
                            s1="".join(mem)
                            a.append(float(s1))
                            a_backup.append(float(s1))
                            mem=[]

                        else:
                            mem.append(y[c])

                    xy_link=dict(zip(a,e_list))
                    decimal_checking=a[-1]
                    pos=None
                    for c in range(len(f"{decimal_checking}"),0,-1):
                        try:
                            pos=a.index(decimal_checking)
                            break
                        except:
                            decimal_checking=float(f"{decimal_checking:.{c}f}")
                    a.sort()

                    #finding slope:
                    if pos==0:
                        x_0=a[0]
                        x_plus=a[1]
                        y_0=xy_link[x_0]
                        y_plus=xy_link[x_plus]

                        slope=(y_plus-y_0)/(x_plus-x_0)

                    elif pos==len(a)-1:
                        x_0=a[len(a)-1]
                        x_minus=a[len(a)-2]
                        y_0=xy_link[x_0]
                        y_minus=xy_link[x_minus]

                        slope=(y_minus-y_0)/(x_minus-x_0)                    

                    else:
                        x_0=a[pos]
                        x_plus=a[pos+1]
                        x_minus=a[pos-1]
                        y_0=xy_link[x_0]
                        y_plus=xy_link[x_plus]
                        y_minus=xy_link[x_minus]

                        try:
                            slope_plus=(y_plus-y_0)/(x_plus-x_0)
                            slope_minus=(y_minus-y_0)/(x_minus-x_0)
                        except ZeroDivisionError:
                            slope_plus=0
                            slope_minus=0

                        if abs(slope_plus)>abs(slope_minus):
                            slope=slope_plus
                        else:
                            slope=slope_minus

                    wi=w0-fom(slope)
                    a_backup.append(wi)
                    curr_set[c1_1_1]=f"{a_backup}"
                    curr_update[c1_1_1]=wi

                weights.iloc[c1_1]=curr_update
                weight_hist.iloc[c1_1]=curr_set

            weights.to_csv(f"processing\\Weight_Pools\\W_{c1-1}-to-{c1}.csv",index=False)
            weight_hist.to_csv(f"processing\\Weight_History\\Whist_{c1-1}-to-{c1}.csv",index=False)

    cf+=1
    cf_df=pd.DataFrame({"cf":[cf]})
    cf_df.to_csv("processing\\coordination_factor.csv",index=False)