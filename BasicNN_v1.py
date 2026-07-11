import pandas as pd

def input_layer(in_): #in_ is a file path string
    in_df=pd.read_csv(in_)
    input_=in_df["0"].to_list()
    for c0 in range(0,len(input_)):
        input_[c0]=float(input_[c0])
    inlayer=pd.DataFrame()
    inlayer[0]=input_
    inlayer.to_csv("processing\\Layers\\Layer_0.csv",index=False)

def layer(layer_num): #layer_num is an integer         #start processing on first hidden layer
    now_layer=pd.read_csv(f"processing\\Layers\\Layer_{layer_num}.csv")
    now_layer_df=pd.DataFrame(now_layer,dtype=float)
    prev_layer=pd.read_csv(f"processing\\Layers\\Layer_{layer_num-1}.csv")
    prev_layer_df=pd.DataFrame(prev_layer)
    weights=pd.read_csv(f"processing\\Weight_Pools\\W_{layer_num-1}-to-{layer_num}.csv")
    weights_df=pd.DataFrame(weights)
    biases=pd.read_csv(f"processing\\Bias_Pools\\B_{layer_num}.csv")
    biases_df=pd.DataFrame(biases)
    def node(pos):
        bias=float(biases_df.iloc[pos].sum())
        active_func="" #future updates coming with bias processing
        sigma=weights_df[f"{pos}"]*prev_layer_df["0"]
        w_sum_inlist=sigma.sum()
        w_sum=float(w_sum_inlist)
        wb_sum=w_sum+bias
        
        #activation function:
        if wb_sum > 0:
            echo=wb_sum
        else:
            echo=0
        #####################
        now_layer_df.iloc[pos]=float(echo)
        

    for c0 in range(0,now_layer_df.shape[0]):
        node(c0)

    now_layer_df.to_csv(f"processing\\Layers\\Layer_{layer_num}.csv",index=False)
    

def output_layer():
    specs=pd.read_csv("01-initialization_criteria\\startsit.csv")
    specs_df=pd.DataFrame(specs)
    num_layers=specs_df.shape[0]
    last=num_layers - 1
    
    out=pd.read_csv(f"processing\\Layers\\Layer_{last}.csv")
    out_df=pd.DataFrame(out)
    print(out_df)