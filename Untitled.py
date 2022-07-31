#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# How to create an empty and a full NumPy array?

# In[2]:


np.empty((3,4),dtype=int)


# In[3]:


np.full((3,3),11)


# Create a Numpy array filled with all zeros

# In[4]:


np.zeros((4,4),dtype=int)


# Create a Numpy array filled with all ones

# In[5]:


np.ones((3,3),dtype=int)


# Check whether a Numpy array contains a specified row

# In[6]:


arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

#for i in arr:
    #if i==[1,2,3]:
        #print("yes it cotains this row")
        
print([3, 2, 5, -4, 5] in arr.tolist())
print([1,4,5] in arr.tolist())
print([4,5,6] in arr.tolist())


# In[7]:


arr=np.array([[1,2,3],[4,5,np.nan],["x",6,8]])
#print(arr,np.any(np.nan))
print(arr[~np.isnan(arr).any(axis=1)])
#print(n_arr[~np.isnan(n_arr).any(axis=0)])


# Reverse a numpy array

# In[ ]:


arr.T


# Change data type of given numpy array

# In[57]:


x=arr.astype("str")
x


# Combining a one and a two-dimensional NumPy Array

# In[23]:


x=np.array([6,7,8])
y=np.array([[1,2,3]
          ,[3,4,5]])
z=x+y
z


# Find the number of occurrences of a sequence in a NumPy array

# In[27]:


x=np.array([[3,3,4]
            ,[5,3,6]])
np.where(x==3)
v=repr(x).count("3")
v


# In[36]:


y=np.array([[[1,2,3]
          ,[3,4,5]]])
y.shape


# In[41]:


np.squeeze(y)
y


# In[ ]:




