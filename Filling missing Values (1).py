#!/usr/bin/env python
# coding: utf-8

# 1.Fill null values of a data frame using median and mode

# In[1]:


import numpy as np
import pandas as pd


# In[6]:


df = pd.DataFrame({'A':[1,3,5,np.nan,7],
                  'B':[2,4,np.nan,6,8],
                  'C':[3,np.nan,21,18,30],
                  'D':[5,10,15,20,np.nan]})


# In[7]:


df


# In[8]:


df.fillna(value=df.median())


# In[9]:


df.fillna(value=df.mode())

