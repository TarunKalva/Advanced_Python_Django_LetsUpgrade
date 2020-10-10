#!/usr/bin/env python
# coding: utf-8

# # Assignment
# The SHIELD is a secretive organization entrusted with the task of guarding the world against
# any disaster. Their arch nemesis is the organization called HYDRA. Unfortunately some
# members from HYDRA had infiltrated into the SHIELD camp. SHIELD needed to find out all
# these infiltrators to ensure that it was not compromised.
# 
# Nick Fury, the executive director and the prime SHIELD member figured out that every one
# in SHIELD could send a SOS signal to every other SHIELD member he knew well. The HYDRA
# members could send bogus SOS messages to others to confuse others, but they could never
# receive a SOS message from a SHIELD member. Every SHIELD member would receive a
# SOS message ateast one other SHIELD member, who in turn would have received from
# another SHIELD member and so on till NickFury. SHIELD had a sophisticated mechanism to
# capture who sent a SOS signal to whom. Given this information, Nick needed someone to
# write a program that could look into this data and figure out all HYDRA members.

# ### sample input
# Nick Fury : Tony Stark, Maria Hill, Norman Osborn\n
# Hulk : Tony Stark, HawkEye, Rogers\n
# Rogers : Thor,\n
# Tony Stark: Pepper Potts, Nick Fury\n
# Agent 13 : Agent-X, Nick Fury, Hitler\n
# Thor: HawkEye, BlackWidow\n
# BlackWidow:Hawkeye\n
# Maria Hill : Hulk, Rogers, Nick Fury\n
# Agent-X : Agent 13, Rogers\n
# Norman Osborn: Tony Stark, Thor
# ### sample output
# Agent 13, Agent-X, Hitler

# In[33]:



d1={'Nick Fury': 'Tony Stark,Maria Hill,Norman Osborn','Hulk':'Tony Stark,HawkEye,Rogers', 'Rogers':'Thor','Tony Stark':'Pepper Potts,Nick Fury','Agent-13':'Agent-X,Nick Fury,Hitler','Thor':'HawkEye,Black Widow','Black Widow':'HawkEye','Maria Hill':"Hulk,Rogers,Nick Fury",'Agent-X':"Agent-13,Rogers", 'Norman Osborn': "Tony Stark,Thor"}
print(d1,'\n')
print('This is the pattern of sending SOS now find culprit...\n')
value=[]


# In[35]:


l1=list(d1.keys())
l2=list(d1.values())
l3=set(l1)
def splitvalues(l):
    return l.split(',')

for each in l2:
    value.extend(splitvalues(each))


# In[46]:


l1.extend(value)

s1=set(l1)
v111=[]
keys=['Nick Fury']

def findhydra(k):
    v111.extend(splitvalues(d1[k]))
    
        
for k,v in d1.items():
    if k in keys:
        keys.extend(splitvalues(d1[k]))
kl=set(keys)
y=l3.intersection(kl)

for i in y:
    findhydra(i)

v222=set(v111)
print(s1-v222)


# In[ ]:




