#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


src = cv2.imread("plane.jpg")
dst = cv2.imread("scenery.jpg")


# In[8]:


mask = np.zeros(src.shape, src.dtype)


# In[11]:


width, height, channels = src.shape
center = (int(height/2),int(width/2))


# In[12]:


normal_clone = cv2.seamlessClone(src, dst, mask, center, cv2.NORMAL_CLONE)
mixed_clone = cv2.seamlessClone(src, dst, mask, center, cv2.MIXED_CLONE)


# In[13]:


cv2.imshow("normal",normal_clone)
cv2.imshow("mixed",mixed_clone)


# In[ ]:




