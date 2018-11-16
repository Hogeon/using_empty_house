
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing


# In[23]:


Seoul_E_House =pd.read_excel("Seoul_emp_house.xls", header = 1)


# In[24]:


Seoul_Ehome = Seoul_E_House


# In[25]:


Seoul_Ehome.head()


# In[26]:


Seoul_Ehome.drop("기간", axis=1, inplace=True)


# In[29]:


Seoul_Ehome.head()


# In[30]:


Seoul_Ehome.rename(columns={Seoul_Ehome.columns[0]: "자치구"}, inplace=True)


# In[50]:


Seoul_Ehome.head()


# In[51]:


Old_pop = pd.read_excel("population_in_Seoul.xls")


# In[52]:


Old_pop = pd.read_excel("population_in_Seoul.xls",header = 2, parse_cols ="B, D, N")


# In[53]:


Old_pop.head()


# In[55]:


New_data = pd.merge(Seoul_Ehome, Old_pop, on = "자치구")


# In[56]:


New_data.head()


# In[61]:


Join_New_data= New_data[["자치구", "계_x", "65세이상고령자"]]


# In[62]:


Join_New_data.head()


# In[66]:


Join_New_data.rename(columns={Join_New_data.columns[1]: "빈집합계",
                            Join_New_data.columns[2]: "고령자"}, inplace=True)


# In[70]:


Join_New_data.head()


# In[72]:


Join_New_data["빈집합계"].plot(kind="barh", grid=True, figsize=(10,10))

