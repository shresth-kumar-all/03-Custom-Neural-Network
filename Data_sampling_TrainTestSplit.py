import pandas as pd
import random as r

#data splitting:

#train test spilt(tts):
data=pd.read_csv("01-initialization_criteria\\LogicGate_input.csv")
dt=pd.DataFrame(data)
dt_shape=dt.shape

test_split = 0.2  #0 to 1
test_sample_size=int(dt.shape[0]*test_split)        #int() can work as box function
print(f"testing data points: {test_sample_size}")

test_index_set=set()
while len(test_index_set)<test_sample_size:
    rnum=r.randint(0,dt_shape[0]-1)
    test_index_set.add(rnum)
test_index=list(test_index_set)
print(test_index)
test_index.sort()       #sorted in ascending order

testdata_export=[]
for c0 in range(0,len(test_index)):
    data_series=dt.iloc[test_index[c0]].tolist()
    cols=["n","x","y","out"]
    tosend=dict(zip(cols,data_series))
    testdata_export.append(tosend)
toexport_testing=pd.DataFrame(testdata_export)
toexport_testing.to_csv(f"03-Testing_Data\\tts_test_{test_split}.csv",index=False)
toexport_testing.index = test_index
print(toexport_testing)

#toexport_training:
Trans_set=dt.T
for c1 in range(0,len(test_index)):
    Trans_set.pop(test_index[c1])
toexport_training=Trans_set.T
toexport_training.to_csv(f"02-Training_Data\\tts_train_{1-test_split}.csv",index=False)
print(toexport_training)