
# coding: utf-8

# In[146]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
get_ipython().run_line_magic('matplotlib', 'inline')


# In[147]:


eoul_com = pd.read_csv("seoul_com.csv") #2013년 서울시 창업자 조사 개요S


# In[148]:


Seoul_com.head()


# In[149]:


Seoul_com.columns


# In[150]:


Seoul_com.rename(columns={Seoul_com.columns[0]: "조사년도"},inplace=True)
Seoul_com.head()


# In[114]:


Seoul_com.sort_values(by="CHANG_Y(설립연도)", ascending=False).head()


# In[115]:


Seoul_com.drop("ZONE_C(행정구역분류코드)", axis=1, inplace=True)
Seoul_com.head()


# In[78]:


Seoul_com.head()


# In[79]:


Seoul_com.head()


# In[80]:


Seoul_com.head()


# In[116]:


Seoul_com.rename(columns={Seoul_com.columns[2]: "대표자성별" }, inplace=True)


# In[117]:


Seoul_com.head()


# In[118]:


Seoul_com.drop("CHANG_M(설립월)", axis=1, inplace=True)


# In[119]:


Seoul_com.head()


# In[120]:


Seoul_com.drop("EMP_JA_M(자영업자_남자)", axis=1, inplace=True)
Seoul_com.drop("EMP_JA_F(자영업자_여자)", axis=1, inplace=True)
Seoul_com.drop("EMP_JA(자영업자_계)", axis=1, inplace=True)


# In[121]:


Seoul_com.head()


# In[122]:


Seoul_com.drop("EMP_MU_M(무급가족종사자_남자)", axis=1, inplace=True)
Seoul_com.drop("EMP_MU_F(무급가족종사자_여자)", axis=1, inplace=True)
Seoul_com.drop("EMP_MU(무급가족종사자_계)", axis=1, inplace=True)


# In[123]:


Seoul_com.head()


# In[124]:


Seoul_com.rename(columns={Seoul_com.columns[3]: "대표자출생년"},inplace=True)
Seoul_com.head()


# In[126]:


Seoul_com.rename(columns={Seoul_com.columns[6]:"설립연도"}, inplace=True)
Seoul_com.rename(columns={Seoul_com.columns[19]:"종사자합계"}, inplace=True)
New_com = Seoul_com[["조사년도", "대표자성별", "대표자출생년", "설립연도", "종사자합계"]]
New_com.head()


# In[131]:


New_com.sort_values(by="종사자합계", ascending=True).head(50)


# In[135]:


종사자합계 = np.array(New_com["종사자합계"])
print("Mean 종사자합계:", 종사자합계.mean())
print("Maximum 종사자합계:", 종사자합계.max())
print("Median:", np.median(종사자합계))


# In[144]:


print("one person company:", np.sum(종사자합계==1))
print("incubating company:", np.sum(종사자합계< 5))
print("cooperation compay", np.sum(종사자합계>20))
print("support company:", np.sum(종사자합계>100))


# In[107]:




