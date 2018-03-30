
# coding: utf-8

# # JSON examples and exercise
# ****
# + get familiar with packages for dealing with JSON
# + study examples with JSON strings and files 
# + work on exercise to be completed and submitted 
# ****
# + reference: http://pandas-docs.github.io/pandas-docs-travis/io.html#json
# + data source: http://jsonstudio.com/resources/
# ****

# In[9]:


import pandas as pd


# ## imports for Python, Pandas

# In[10]:


import json
from pandas.io.json import json_normalize


# ## JSON example, with string
# 
# + demonstrates creation of normalized dataframes (tables) from nested json string
# + source: http://pandas-docs.github.io/pandas-docs-travis/io.html#normalization

# In[11]:


# define json string
data = [{'state': 'Florida', 
         'shortname': 'FL',
         'info': {'governor': 'Rick Scott'},
         'counties': [{'name': 'Dade', 'population': 12345},
                      {'name': 'Broward', 'population': 40000},
                      {'name': 'Palm Beach', 'population': 60000}]},
        {'state': 'Ohio',
         'shortname': 'OH',
         'info': {'governor': 'John Kasich'},
         'counties': [{'name': 'Summit', 'population': 1234},
                      {'name': 'Cuyahoga', 'population': 1337}]}]


# In[12]:


# use normalization to create tables from nested element
json_normalize(data, 'counties')


# In[13]:


# further populate tables created from nested element
json_normalize(data, 'counties', ['state', 'shortname', ['info', 'governor']])


# ****
# ## JSON example, with file
# 
# + demonstrates reading in a json file as a string and as a table
# + uses small sample file containing data about projects funded by the World Bank 
# + data source: http://jsonstudio.com/resources/

# In[23]:


# load json as string
json.load((open(r"C:\Users\yi6\Desktop\data_wrangling_json\data\world_bank_projects_less.json")))


# In[34]:


# load as Pandas dataframe
sample_json_df = pd.read_json(r"C:\Users\yi6\Desktop\data_wrangling_json\data\world_bank_projects_less.json")
print(sample_json_df.columns)


# ****
# ## JSON exercise
# 
# Using data in file 'data/world_bank_projects.json' and the techniques demonstrated above,
# 1. Find the 10 countries with most projects
# 2. Find the top 10 major project themes (using column 'mjtheme_namecode')
# 3. In 2. above you will notice that some entries have only the code and the name is missing. Create a dataframe with the missing names filled in.

# In[42]:


json.load((open(r"C:\Users\yi6\Desktop\data_wrangling_json\data\world_bank_projects.json")))
json_df = pd.read_json(r"C:\Users\yi6\Desktop\data_wrangling_json\data\world_bank_projects.json")


# In[49]:


json_sum = json_df.groupby("countryshortname").count()
print(json_sum.nlargest(10,"_id"))


# In[87]:


project_list = json_df['mjtheme_namecode'].tolist()
frames=[]
for each in project_list:
    frames.append(pd.DataFrame(each))
results = pd.concat(frames)
print(results.head())
results_sum = results.groupby("name").count()
print(results_sum.nlargest(10,"code"))


# In[89]:


results_fill = results.fillna(value = None, method = 'ffill')

