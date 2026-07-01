import BasicNN_v1 as nn
import Gradient_Descent as gd
import pandas as pd

startsit=""
tts_test=""

TestD=pd.read_csv(tts_test)
TestD_dt=pd.DataFrame(TestD)
TsD_shape=TestD_dt.shape

layers_import=pd.read_csv(startsit)
layers_dt=pd.DataFrame(layers_import)
layers=layers_dt["layer_widths"].tolist()

for 0 in range(0,TsD_shape[0]):
    