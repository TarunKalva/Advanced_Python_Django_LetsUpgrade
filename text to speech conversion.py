#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gtts import gTTS


# In[2]:


import os


# In[3]:


os.chdir('C:\\Users\\Kalva Tarun Kumar\\Desktop\\text to speech files')
print(os.getcwd())
fh=open(r'firstfile.txt','r')
mytext=fh.read()
fh.close()
print(mytext)


# In[26]:


language='en-us'


# In[27]:


myobj=gTTS(text=mytext,lang=language)


# In[28]:


myobj.save('C:\\Users\\Kalva Tarun Kumar\\Desktop\\text to speech files\\welcome.mp3')


# In[29]:


os.system('welcome.mp3')


# In[20]:


from gtts import lang


# In[21]:


lang.tts_langs() # various languages 


# In[31]:


# Instead of downloading we can get URLs of the voice
myobj.get_urls()


# In[ ]:




