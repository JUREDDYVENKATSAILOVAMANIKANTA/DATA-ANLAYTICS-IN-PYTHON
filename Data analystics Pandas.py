#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as  plt 
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes = True)


# In[7]:


car = pd.read_csv(r'C:\Users\srini\Downloads\archive\CarPrice_Assignment.csv')
car.head(2)


# In[8]:


# Reading the Excel file
data_dict = pd.read_excel(r'C:\Users\srini\Downloads\archive\Data Dictionary - carprices.xlsx')

# Display the first few rows of the DataFrame
print(data_dict.head(3))


# In[9]:


car.dtypes


# In[12]:


car.columns


# In[13]:


car.describe(include='all')


# In[15]:


car.hist(figsize = (20,30))


# In[20]:


sns.pairplot(car)


# In[21]:


car.shape


# In[24]:


duplicate_rows_car = car[car.duplicated()]
print("Number of duplicate rows : ", duplicate_rows_car.shape)


# In[25]:


car.count()


# In[26]:


car = car.drop_duplicates()
car.head()


# In[27]:


print(car.isnull().sum())


# In[28]:


car = car.dropna()
car.count()


# In[29]:


print(car.isnull().sum())


# In[30]:


sns.boxplot(x= car["price"])


# In[39]:


plt.figure(figsize=(20,10))
c=  car.corr()
sns.heatmap(c,cmap="BrBG",annot=True)


# In[ ]:




