#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics 
import pickle
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df=pd.read_csv('data.csv')
df.head()


# In[3]:


df['district'].unique()


# In[4]:


#df['district'].replace(['ryk', 'bahawalnagar', 'bwp', 'rajanpur', 'digikhan', 'layyah',
#       'm.garh', 'vihari', 'khanewal', 'lodhran', 'multan', 'pakpatan',
#       'sahiwal', 'okara', 'kasur', 'lahore', 'nankana sahib',
#       'shekupora', 'hafizabad', 'gujranwala', 'narowall', 'sialkot',
#       'gujrat', 'chainiot', 'jhang', 'faisalabad', 'bakar', 'mianwali',
#       'tobataiksingh', 'attock', 'rawalpindi ', 'isl', 'jehlum',
#       'chakwall', 'sarjodha', 'khushab', 'm.b.din', 'muzafargarh',
#       'd.g.khan'],
 #                       [0, 1, 2, 3, 4, 5, 6,7 ,8 ,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38], inplace=True)


# In[5]:


df.iloc[0:,-1].head(50)


# In[6]:


df.size


# In[7]:


df.shape


# In[8]:


df.columns


# In[9]:


df['label'].value_counts()


# In[10]:


sns.heatmap(df.corr(),annot=True)


# In[11]:


features = df[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
target = df['label']
labels = df['label']


# In[12]:


# Xtrain=df.iloc[0:,0:7]
# Xtrain


# In[13]:


# Ytrain=df.iloc[0:,7:9]
# Ytrain


# In[14]:


from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,  target,test_size = 0.2,random_state =2)


# In[15]:


acc = []
model = []


# In[16]:


from sklearn.linear_model import LogisticRegression

LogReg = LogisticRegression(random_state=2)

LogReg.fit(Xtrain,Ytrain)
pickle.dump(LogReg, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))


# In[17]:


data = np.array([[104,18, 30, 23.603016, 60.3, 6.7, 140.91]])
prediction = LogReg.predict(data)
print(prediction)


# In[18]:





# In[ ]:





# In[ ]:




