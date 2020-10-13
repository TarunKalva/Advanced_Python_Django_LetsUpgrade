#!/usr/bin/env python
# coding: utf-8

# ## Assignment
# Convert 15-08-2020 15:20:20 into epoch time

# In[2]:


import time
t1='15-08-2020 15:20:20'
t9=time.strptime(t1,'%d-%m-%Y %H:%M:%S')
epoch=time.mktime(t9)
print('The epoch time for 15-08-2020 15:20:20 is: ',epoch)


# In[ ]:




