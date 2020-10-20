#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
# Remove the hardcoded part from the code with the help of configparser. use file exc.in

# In[1]:


from configparser import ConfigParser as cp


# In[2]:


config=cp()
config.read('exc.ini')
print(config.sections())
print(config.options('FC'))


# In[3]:


import os


# In[4]:


os.chdir(config.get('FC','file_path'))
for file in os.listdir('.'):
    if file.endswith(config.get('FC','from')):
        first_name=file.rsplit('.',1)[0]
        new_name=first_name+config.get('FC','to')
        os.rename(file,new_name)
        print(file)


# # Assignment 2
# print the all possible paths for a file 

# In[14]:


rep=os.walk('C:\\Users\\Kalva Tarun Kumar\\Desktop')
d1={}
for r,d,f in rep:
    for file in f:
        d1.setdefault(file,[]).append(r)
file_name=input('Enter the file name:')
for k,v in d1.items():
    if file_name.lower() in k.lower():
        for i in v:
            print(i)
            print('-'*50)


# In[ ]:




