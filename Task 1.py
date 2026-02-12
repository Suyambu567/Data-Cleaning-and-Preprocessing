#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv(r"C:\Users\suyambu\Downloads\archive (1)\Auto Sales data.csv")


# In[3]:


df.head()


# In[4]:


df.shape
df.info()


# In[5]:


pip install openpyxl


# In[6]:


df.isnull().sum()


# In[7]:


df[df.isnull().any(axis=1)]


# In[8]:


df = df.dropna()


# In[9]:


df.duplicated().sum()


# In[10]:


df = df.drop_duplicates()


# In[11]:


df.dtypes


# In[13]:


df["orderdate"] = pd.to_datetime(
    df["ORDERDATE"], dayfirst=True
)


# In[14]:


df.dtypes


# In[15]:


df.info()
df.head()


# In[16]:


df["PHONE"].head()


# In[17]:


df["phone"] = df["PHONE"].str.replace(r"[^\d]", "", regex=True)


# In[18]:


df[["PHONE", "phone"]].head()


# In[ ]:




