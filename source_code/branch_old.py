import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# In[22]:


Old_pop = pd.read_excel("population_in_Seoul.xls")


# In[23]:


Old_pop.head()


# In[24]:


Old_pop = pd.read_excel("population_in_Seoul.xls",header = 2, parse_cols ="B, D, N")


# In[25]:


Old_pop


# In[26]:


Old_pop.drop([26]).tail()


# In[27]:


Old_pop.rename(columns={Old_pop.columns[2]:"고령자"}, inplace=True)


# In[28]:


Old_Pop = Old_pop.sort_values(by="고령자", ascending=False)


# In[30]:


Old_pop1 =Old_Pop.drop([26])


# In[37]:


Old_popu = Old_pop1


# In[40]:


Old_popu["고령자"].sort_values().plot(kind="barh", grid=True, figsize=(10,10))

