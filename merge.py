
# coding: utf-8

# In[3]:

import pandas as pd
import glob


# In[6]:

path =r'./newData' # use your path
allFiles = glob.glob(path + "/*/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0,sep="|")
    list_.append(df)
frame = pd.concat(list_)


# In[20]:

frame.to_csv("./combinedData.txt",sep='\t',index=False)


# In[ ]:



