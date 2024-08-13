#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
arr1 = np.array([1,2,3])
print(arr1)


# In[4]:


print(type(arr1))


# In[5]:


print(arr1.shape)


# In[7]:


print(arr1[2])


# In[8]:


arr1[2]=5
arr1


# In[10]:


arr2 = np.array([[1,2,3],[4,5,6]])
arr2


# In[12]:


arr2[1][2]


# In[13]:


print(arr2.shape)


# In[14]:


arr2[1,2,]


# In[17]:


arr2[1][-3]


# In[19]:


arrS = np.array(['China','India','USA','UK'])
arrS


# In[24]:


arrR = np.arange(0,20,3)
arrR


# In[26]:


arrL = np.linspace(0,10,20)
arrL


# In[29]:


arr = np.random.rand(10)
arr


# In[30]:


arr = np.random.rand(2,4)
arr


# In[31]:


print(np.zeros(10))
print('/n')
print(np.zeros((2,3)))


# In[34]:


print(np.ones((10,10)))


# In[35]:


arr = [0,1,2]
print(np.repeat(arr ,2))


# In[37]:


print(np.tile(arr,3))


# In[40]:


identity_matrix = np.eye(3)
identity_matrix


# In[41]:


np.diag([1,2,3,4,5,])


# In[44]:


arr = np.random.rand(4,4)
arr


# In[45]:


np.diag(arr)


# In[46]:


arr.ndim


# In[47]:


arr.size


# In[48]:


arr.shape


# In[49]:


np.random.randint(-10,10,4)


# In[59]:


arr


# In[60]:


np.log2(arr)


# In[62]:


np.tan(arr)


# In[64]:


np.sum(arr,axis = 0)


# In[66]:


np.min(arr,axis=0)


# In[68]:


np.max(arr)


# In[69]:


np.mean(arr)


# In[71]:


np.median(arr)


# In[72]:


np.std(arr)


# In[73]:


np.var(arr)


# In[74]:


arr


# In[77]:


arr[1:,2:3]


# In[80]:


np.sort(arr)


# In[81]:


arr.T


# In[84]:


arr[:3,:].T


# In[86]:


arr[:3,:].flatten()


# In[88]:


arr = np.array([4,5,6,7,8])
arr


# In[90]:


arr1 = np.append(arr,10)
arr1


# In[92]:


arr2 = np.insert(arr,0,[1,2,3])
arr2


# In[95]:


arr3 = np.delete(arr2,1)
arr3


# In[97]:


arrC = arr3.copy()
arrC


# In[3]:


arr1 = np.array([[1,2,3,4,],[1,2,3,4]])
arr2 = np.array([[5,6,7,8],[5,6,7,8]])
arr_cat = np.concatenate((arr1,arr2),axis =0)
print(arr_cat)


# In[5]:


cat = np.hstack((arr1,arr2))
cat


# In[9]:


cat = np.vstack((arr1,arr2))
cat


# In[10]:


arr = np.array([1,2,3,4,5,6,3,1,2,3])
np.unique(arr)


# In[11]:


uniques, counts = np.unique(arr,return_counts=True)
print(uniques)
print(counts)


# In[15]:


#intersection, differentiation, neither
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([3,4,5,6,7])
print(np.intersect1d(arr1,arr2))
print(np.union1d(arr1,arr2))
print(np.setdiff1d(arr1,arr2))
print(np.setxor1d(arr1,arr2))


# In[ ]:




