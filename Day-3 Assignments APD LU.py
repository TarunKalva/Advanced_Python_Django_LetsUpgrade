#!/usr/bin/env python
# coding: utf-8

# # Day 3 Oct-1st Assignment
# ## Assignment 1

# In[3]:


list3=['192.168.10.9','192.168.10.4','192.168.10.11','192.168.10.35']
def fun1(l):
    x=l.split('.')
    return int(x[3])

list3.sort(key=fun1)
print(list3)


# ## Assignment 3

# In[4]:


list2=[(10,4),(90,3),(9,1),(10,4),(9,5)]
def fun2(l):
    return l[0]+l[1]

list2.sort(key=fun2)
print(list2)


# ## Assignment 2

# In[18]:


list1=[1,2,3,0,2,3,0,1,24,0,1,3,1,0,1,21,0,1,2,0,45]
l2=[]
for i in list1:
    if i==0:
        l2.append(i)
        list1.remove(i)
list1.sort()
list1=list1+l2
print(list1)


# In[ ]:





# In[ ]:




