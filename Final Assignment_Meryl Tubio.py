#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from collections import Counter


# In[2]:


#Load dataset
raw_data = pd.read_csv('survey.csv')
raw_data.head()


# In[3]:


#Identify the most number of results in the dataset per country, then sorting it from highest to lowest
clean_data = raw_data.groupby("Country")["treatment"].count().reset_index()
clean_data.sort_values("treatment", ascending = False, inplace = True)

print(clean_data)


# In[4]:


#Afterwards, I visualized this data to identify which Country has the largest population for the dataset 
count_country = Counter(raw_data['Country'].dropna().tolist()).most_common(10)
country_idx = [country[0] for country in count_country]
country_val = [country[1] for country in count_country]
fig,ax = plt.subplots(figsize=(8,6))
sns.barplot(x = country_idx, y= country_val, ax = ax)
plt.title('Top ten country')
plt.xlabel('Country')
plt.ylabel('Count')
ticks = plt.setp(ax.get_xticklabels(),rotation=90)


# In[5]:


#create a new sub-dataset for the United States, since we will be focusing on this Country
US_data = raw_data[raw_data["Country"] == "United States"]


# In[6]:


#After identifying the most populated country, the United States, for our data source, We can break that down further to
#different states in the united states
US_data.head()


# In[7]:


#Then visualize the dataset above
count_USstates = Counter(US_data['state'].dropna().tolist()).most_common(10)
state_idx = [state[0] for state in count_USstates]
state_val = [state[1] for state in count_USstates]
fig,ax = plt.subplots(figsize=(8,6))
sns.barplot(x = state_idx, y= state_val, ax = ax)
plt.title('Top ten states')
plt.xlabel('States')
plt.ylabel('Count')
ticks = plt.setp(ax.get_xticklabels(),rotation=90)


# In[8]:


#In this assignment, What do we define as attitude towards mental health?
#I define attitude to mental health by 2 attributes: Wellness program and Leave.
#The availability of mental wellness_program.
#The likelihood that an employee would approach a supervisor about mental health issues


# In[9]:


#We have identified that California, Washington, and New York are the top 3 states in the US.
#Then create sub-datasets below.
CA_data = US_data[US_data ["state"] == "CA"]
WA_data = US_data[US_data ["state"] == "WA"]
NY_data = US_data[US_data ["state"] == "NY"]


# In[10]:


#We first identify people in California who marked yes in seeking treatment
sns.countplot(CA_data['treatment'] == "Yes")
plt.title("Number of people in California seeking Treatment")


# In[11]:


sns.countplot(WA_data['treatment'] == "Yes")
plt.title("Number of people in Washington seeking Treatment")


# In[12]:


sns.countplot(NY_data['treatment'] == "Yes")
plt.title("Number of people in New York seeking Treatment")
#From here we can identify that most people in the top 3 states were seeking treatment


# In[13]:


sns.countplot(CA_data['benefits'] == "Yes")
plt.title("Are benefits offered by your employer in California?")


# In[14]:


sns.countplot(WA_data['benefits'] == "Yes")
plt.title("Are benefits offered by your employers in Washington?")


# In[15]:


sns.countplot(NY_data['benefits'] == "Yes")
plt.title("Are benefits offered by your employers in New York?")


# In[16]:


#Lastly, identify the ease of approaching employers regarding Mental Health leaves
fig,ax = plt.subplots(figsize=(8,6))
total = CA_data['leave'].dropna().shape[0] * 1.0
leave_count  = Counter(CA_data['leave'].dropna().tolist())
for key,val in leave_count.items():
    leave_count[key] = leave_count[key] / total
leave_group = np.asarray(list(leave_count.keys()))
leave_val = np.asarray(list(leave_count.values()))
sns.barplot(x = leave_group , y = leave_val)
plt.title('leave ratio in California')
plt.ylabel('Count of prospective leaves')
plt.xlabel('Leave')


# In[17]:


fig,ax = plt.subplots(figsize=(8,6))
total = WA_data['leave'].dropna().shape[0] * 1.0
leave_count  = Counter(WA_data['leave'].dropna().tolist())
for key,val in leave_count.items():
    leave_count[key] = leave_count[key] / total
leave_group = np.asarray(list(leave_count.keys()))
leave_val = np.asarray(list(leave_count.values()))
sns.barplot(x = leave_group , y = leave_val)
plt.title('leave ratio in Washington')
plt.ylabel('Count of prospective leaves')
plt.xlabel('Leave')


# In[18]:


fig,ax = plt.subplots(figsize=(8,6))
total = NY_data['leave'].dropna().shape[0] * 1.0
leave_count  = Counter(NY_data['leave'].dropna().tolist())
for key,val in leave_count.items():
    leave_count[key] = leave_count[key] / total
leave_group = np.asarray(list(leave_count.keys()))
leave_val = np.asarray(list(leave_count.values()))
sns.barplot(x = leave_group , y = leave_val)
plt.title('leave ratio in New York')
plt.ylabel('Count of prospective leaves')
plt.xlabel('Leave')

