#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import *
A=array([1,2,3] , int)
A


# In[2]:


B = array([2.0, 3.0, 4.0] , float)
B


# In[3]:


#linspace
F= linspace(0,9,10)
F


# In[4]:


G= linspace(0,9,30)
G


# In[5]:


I= arange(0,10,2)
I


# In[6]:


K=array([2.3635897, 3.986547, 6.23458,5.879654], float)
print('%.2f' %K[0])


# In[7]:


print('%.3f' %K[3])


# In[8]:


Y= array([0,0,0,0,0,0] ,float)
Y


# In[9]:


zeros(6)


# In[10]:


ones(5)


# In[11]:


ones(10, int)


# In[12]:


R= ones(5)
i=0
while(i<len(R)):
    print(i,',' ,R[i])
    i=i+1


# In[13]:


len(R)


# In[14]:


M=array([1,2,3,4,5] ,int)
N=M+10
N


# In[15]:


M=array([1,2,3,4,5] ,int)
U=array([20,30,40,50,60], int)
P=M+U
P


# In[16]:


sin(P)


# In[17]:


sqrt(P)


# In[18]:


sum(P)


# In[19]:


min(P)


# In[20]:


max(P)


# In[21]:


M=array([1,2,3,4,5])
O=array([10,10,10,10])
Y=concatenate([M,O])
Y


# In[22]:


M=array([1,2,3,4,5])
W=M
print(id(M), id(W))


# In[25]:


M=array([1,2,3,4,5])
W=M.view()
print(id(M), id(W))


# In[26]:


M=array([1,2,3,4,5])
M[1]=100
M


# In[28]:


M=array([1,2,3,4,5])
U=M.copy()
print(id(M), id(U))


# In[ ]:




