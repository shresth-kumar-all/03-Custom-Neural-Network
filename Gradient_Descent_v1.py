import pandas as pd
import numpy as np

def learner(_startsit,_traindata):
    #importing assets for comparison:
    specs=pd.read_csv(_startsit)
    specs_df=pd.DataFrame(specs)
    specs_df=specs_df.transpose()
    specs_df1=pd.DataFrame(specs)
    layers=specs_df1["layer_widths"].tolist() #list of layers
    num_layers=len(layers) #no. of layers
    last=num_layers - 1
    last_L=pd.read_csv(f"processing\\Layers\\Layer_{last}.csv")
    out_model=pd.DataFrame(last_L) #model output

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

    cf+=1
    cf_df=pd.DataFrame({"cf":[cf]})
    cf_df.to_csv("processing\\coordination_factor.csv",index=False)

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
        for cl in range(0,num_layers-1):
            weights=pd.read_csv(f"processing\\Weight_Pools\\W_{cl}-to-{cl+1}.csv")
            weights_df=pd.DataFrame(weights)
            shape=weights.shape
            weights_h=pd.read_csv(f"processing\\Weight_Pools\\Whist_{cl}-to-{cl+1}.csv")
            weights_h_df=pd.DataFrame(weights_h)
            weights_hn=pd.read_csv(f"processing\\Weight_Pools\\Whist_{cl}-to-{cl+1}.csv")
            weights_hn_df=pd.DataFrame(weights_hn)

            weights_df_up=weights_df+1
            weights_df_up.to_csv(f"processing\\Weight_Pools\\W_{cl}-to-{cl+1}.csv",index=False)

            for a in range(0,shape[0]):
                wr=weights_df_up.iloc[a].tolist()
                whr=weights_h_df.iloc[a].tolist()

                for b in range(0,shape[1]):
                    wr_ab=wr[b]
                    whr_ab=whr[b]

                    whr_y=whr_ab
                    whr_y.pop(0)
                    whr_y.pop(-1)
                    whr_y.append("#")
                    whr_a=[]
                    mem=[]
                    for c1 in range(0,len(whr_y)):
                        if whr_y[c1] in {',','#'}:
                            s1="".join(mem)
                            a.append(float(s1))
                            mem=[]

                        else:
                            mem.append(whr_y[c])
                    whr_next=whr_a.append(wr_ab)
                    whr[b]=f"{whr_next}"
                
                weights_hn_df.iloc[a]=whr
            
            weights_hn_df.to_csv(f"processing\\Weight_Pools\\Whist_{cl}-to-{cl+1}.csv",index=False)

    else:
        for cl in range(0,num_layers-1):
            weightsf=pd.read_csv(f"processing\\Weight_Pools\\W_{cl}-to-{cl+1}.csv")
            weightsf_df=pd.DataFrame(weightsf)
            shape=weightsf.shape
            weightsf_h=pd.read_csv(f"processing\\Weight_History\\Whist_{cl}-to-{cl+1}.csv")
            weightsf_h_df=pd.DataFrame(weightsf_h)
            ef_csv=pd.read_csv("processing\\rms_errors.csv")
            ef_df=pd.DataFrame(ef_csv)
            ef=ef_df["e_rms"].tolist()


            for af in range(0,shape[0]):
                #wfr=weightsf_df.iloc[af].tolist()
                wfhr=weightsf_h_df.iloc[af].tolist()

                wfr_updated=[]
                wfhr_updated=[]

                for bf in range(0,shape[1]):
                    #wfr_ab=wfr[bf]
                    wfhr_ab=wfhr[bf]

                    wfhr_y=wfhr_ab
                    wfhr_y.pop(0)
                    wfhr_y.pop(-1)
                    wfhr_y.append("#")
                    
                    wfhr_a=[]
                    wfhr_a_backup=[] #download mechanism for weight history lists
                    memf=[]
                    for c1f in range(0,len(wfhr_y)):
                        if wfhr_y[c1f] in {',','#'}:
                            s1f="".join(memf)
                            af.append(float(s1f))
                            memf=[]

                        else:
                            memf.append(wfhr_a[c])
                            memf.append(wfhr_a_backup[c])
                    
                    e_link_w=dict(zip(wfhr_a,ef))
                    wx=wfhr_a[-1]
                    wfhr_a.sort() #making the x axis of the graph
                    wx_pos=wfhr_a.index(wx)
                    m=0 #initializing slope

                    if wx_pos == (len(wfhr_a)-1):
                        wx_prev=wfhr_a[wx_pos-1]
                        erms_prev=e_link_w[wx_prev]
                        erms=e_link_w[wx]
                        
                        m=(erms-erms_prev)/(wx-wx_prev) #slope calculation
                        delta_w=fom(m)
                        wx_new=float(wx-delta_w) #updated weight

                    elif wx_pos == 0:
                        wx_next=wfhr_a[1]
                        erms_next=e_link_w[wx_next]
                        erms=e_link_w[wx]

                        m=(erms-erms_prev)/(wx-wx_prev) #slope calculation
                        delta_w=fom(m)
                        wx_new=float(wx-delta_w) #updated weight

                    else:
                        wx_prev=wfhr_a[wx_pos-1]
                        wx_next=wfhr_a[wx_pos+1]
                        
                        if np.absolute(wx-wx_prev) < np.absolute(wx-wx_next):
                            erms_prev=e_link_w[wx_prev]
                            erms=e_link_w[wx]

                            m=(erms-erms_prev)/(wx-wx_prev) #slope calculation
                            delta_w=fom(m)
                            wx_new=float(wx-delta_w) #updated weight
                        
                        else:
                            erms_next=e_link_w[wx_next]
                            erms=e_link_w[wx]

                            m=(erms-erms_next)/(wx-wx_next) #slope calculation
                            delta_w=fom(m)
                            wx_new=float(wx-delta_w) #updated weight

                    wfr_updated.append(wx_new) #sending updated weights back to loaded data collections
                    wfhr_a_backup.append(wx_new)
                    str_hist=f"{wfhr_a_backup}"
                    wfhr_updated.append(str_hist)

                weightsf_df.iloc[af]=wfr_updated #sending updated weights back to DataFrames
                weightsf_h_df.iloc[af]=wfhr_updated
            
            weightsf_df.to_csv(f"processing\\Weight_Pools\\W_{cl}-to-{cl+1}.csv",index=False) #sending weights and history back to processing(globally accessible folder)
            weightsf_h_df.to_csv(f"processing\\Weight_Pools\\Whist_{cl}-to-{cl+1}.csv",index=False)

##########################################################################################################