import BasicNN_v1 as nn
import Gradient_Descent_v1 as gd
import pandas as pd

startsit="01-initialization_criteria\\startsit.csv"
tts_train="02-Training_Data\\tts_train_0.8.csv"

TrainD=pd.read_csv(tts_train)
TrainD_dt=pd.DataFrame(TrainD)
TrD_shape=TrainD_dt.shape

layers_import=pd.read_csv(startsit)
layers_dt=pd.DataFrame(layers_import)
layers=layers_dt["layer_widths"].tolist()

for c1 in range(0,TrD_shape[0]):

    in_=TrainD_dt.iloc[c1].tolist()
    in_dt=pd.DataFrame(in_)
    in_dt_tosend=in_dt.to_csv("processing\\in_layer.csv",index=False)

    nn.input_layer("processing\\in_layer.csv")
    for c2 in range(1,len(layers)):
        nn.layer(c2)
    print("###############################################################")
    nn.output_layer()
    print("actual ans: ",in_[-1])