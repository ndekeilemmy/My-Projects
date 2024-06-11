#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')


# In[42]:


pd.set_option('display.max.columns', 67)
pd.set_option('display.max.rows', 3122)


# In[43]:


df = pd.read_csv(r"C:\Users\HomePC\Downloads\Football Players Statistics.csv")
df.head()


# In[8]:


df.shape


# In[9]:


df.dtypes


# In[10]:


df.describe()


# In[124]:


# Cleaning my data


# In[11]:


df = df.drop_duplicates()


# In[12]:


df.shape


# In[ ]:


df.isna().sum()


# In[ ]:


df[['Team', 'Contract']] = df['Team & Contract'].str.split('\n', expand = True)
df[['Height_cm', 'Height_ft']] = df['Height'].str.split('/', expand = True)
df[['Weight_kg', 'Weight_lbs']] = df['Weight'].str.split('/', expand = True) 


# In[ ]:


df['Weight_lbs'] = df['Weight_lbs'].str.rstrip('lbs')
df['Height_ft'] = df['Height_ft'].str.rstrip('ft')
df['Weight_kg'] = df['Weight_kg'].str.replace('kg', '')
df['Height_cm'] = df['Height_cm'].str.replace('cm', '')


# In[ ]:


df['Value'] = df['Value'].str.lstrip('€')
df['Wage'] = df['Wage'].str.lstrip('€')
df['Release clause'] = df['Release clause'].str.lstrip('€')


# In[ ]:


df['Value'] = df['Value'].replace({'K': '*1e3', 'M': '*1e6'}, regex=True).map(pd.eval).astype(int)
df['Wage'] = df['Wage'].replace({'K': '*1e3', 'M': '*1e6'}, regex=True).map(pd.eval).astype(int)
df['Release clause'] = df['Release clause'].replace({'K': '*1e3', 'M': '*1e6'}, regex=True).map(pd.eval).astype(int)


# In[ ]:


df.rename(columns = {'name':'Player', 'foot':'Preferred foot', 'Value':'Value_€', 'Wage':'Wage_€',
                     'Release clause':'Release clause_€', 'Total attacking':'Attacking',
                     'Total skill':'Skill', 'Total movement':'Movement', 'Total power':'Power',
                     'Total mentality':'Mentality', 'Total defending':'Defending',
                     'Total goalkeeping':'Goalkeeping'}, inplace = True)


# In[18]:


df.columns


# In[19]:


df = df[['Player', 'Age', 'Overall rating', 'Potential', 'ID', 'Preferred foot',
       'Best overall', 'Best position', 'Growth', 'Value_€', 'Wage_€',
       'Release clause_€', 'Attacking', 'Crossing', 'Finishing',
       'Heading accuracy', 'Short passing', 'Volleys', 'Skill', 'Dribbling',
       'Curve', 'FK Accuracy', 'Long passing', 'Ball control', 'Movement',
       'Acceleration', 'Sprint speed', 'Agility', 'Reactions', 'Balance',
       'Power', 'Shot power', 'Jumping', 'Stamina', 'Strength', 'Long shots',
       'Mentality', 'Aggression', 'Interceptions', 'Att. Position', 'Vision',
       'Penalties', 'Composure', 'Defending', 'Defensive awareness',
       'Standing tackle', 'Sliding tackle', 'Goalkeeping', 'GK Diving',
       'GK Handling', 'GK Kicking', 'GK Positioning', 'GK Reflexes',
       'Total stats', 'Base stats', 'International reputation',
       'Pace / Diving', 'Shooting / Handling', 'Passing / Kicking',
       'Dribbling / Reflexes', 'Defending / Pace', 'Team', 'Contract',
       'Height_cm', 'Height_ft', 'Weight_kg', 'Weight_lbs']].copy()


# In[20]:


df['Overall rating'] = df['Overall rating'].str.replace('+1', '')
df['Overall rating'] = df['Overall rating'].str.replace('+2', '')
df['Overall rating'] = df['Overall rating'].str.replace('+3', '')
df['Overall rating'] = df['Overall rating'].str.replace('-1', '')
df['Overall rating'] = df['Overall rating'].str.replace('-2', '')


# In[21]:


df['Height_cm'] = df['Height_cm'].astype(int)
df['Weight_kg'] = df['Weight_kg'].astype(int)
df['Weight_lbs'] = df['Weight_lbs'].astype(int)
df['Overall rating'] = df['Overall rating'].astype(int)


# In[22]:


df.head(11)


# In[23]:


df.loc[df.duplicated()]


# In[24]:


df.loc[df.duplicated(subset = 'Player')]


# In[25]:


df.query('Player == "N. Collins CB"')


# In[26]:


df = df[['Player', 'Age', 'Overall rating', 'Potential', 'ID', 'Preferred foot',
       'Best overall', 'Best position', 'Growth', 'Value_€', 'Wage_€',
       'Release clause_€', 'Attacking', 'Crossing', 'Finishing',
       'Heading accuracy', 'Short passing', 'Volleys', 'Skill',
       'Dribbling', 'Curve', 'FK Accuracy', 'Long passing', 'Ball control',
       'Movement', 'Acceleration', 'Sprint speed', 'Agility',
       'Reactions', 'Balance', 'Power', 'Shot power', 'Jumping',
       'Stamina', 'Strength', 'Long shots', 'Mentality', 'Aggression',
       'Interceptions', 'Att. Position', 'Vision', 'Penalties', 'Composure',
       'Defending', 'Defensive awareness', 'Standing tackle',
       'Sliding tackle', 'Goalkeeping', 'GK Diving', 'GK Handling',
       'GK Kicking', 'GK Positioning', 'GK Reflexes', 'Total stats',
       'Base stats', 'International reputation', 'Pace / Diving',
       'Shooting / Handling', 'Passing / Kicking', 'Dribbling / Reflexes',
       'Defending / Pace', 'Team', 'Contract', 'Height_cm', 'Height_ft',
       'Weight_kg', 'Weight_lbs']].copy()


# In[ ]:


# Univariate analysis


# In[27]:


df['Age'].value_counts()


# In[28]:


df['Age'].value_counts().plot(kind = 'bar', title = 'Age_Distribution', ylabel = 'No_of_Players')
plt.show()


# In[29]:


df['Height_cm'].plot(kind='hist', bins=(40), title='Player_Heights (cm)', xlabel='Height (cm)') 
plt.show()


# In[30]:


ax = df['Weight_kg'].plot(kind='kde', title='Player_Weights (kg)')
ax.set_xlabel('Weight (kg)')
plt.show()


# In[127]:


# Feature Relationships


# In[31]:


ax = df.plot(kind='scatter', x='Value_€', y='Release clause_€', title=('Player Value vs Release Clause'))
ax.set_xlabel('Value (€)')
ax.set_ylabel('Release_Clause (€)')
plt.show()


# In[32]:


ax = sns.scatterplot(x='Age', y='Value_€', hue='Preferred foot', palette=sns.color_palette('flare', 2), data=df)


# In[129]:


# Comparing multiple features aganist each other (correlation and pairplotting)


# In[33]:


df.head()


# In[34]:


df_corr = df[['Skill','Movement',
              'Power','Mentality',
              'Attacking','Defending',
              'Goalkeeping']].dropna().corr()
df_corr


# In[39]:


sns.heatmap(df_corr, annot=True)
plt.show()


# In[35]:


sns.pairplot(df,
             vars=['Skill','Movement',
                   'Power','Mentality'],
                    hue='Best position')
plt.show()


# In[93]:


# Which teams have the most valuable squads


# In[36]:


df['Team'].value_counts()


# In[37]:


ax = df.groupby('Team')['Value_€']\
    .agg(['sum','count'])\
    .query('count >= 22')\
    .sort_values(by= 'sum')['sum']\
    .plot(kind= 'barh', title='Squad Values')
ax.set_xlabel('Squad_value (€)')
plt.show()


# In[125]:


# How does the size of a player affect their skill level and ability to move


# In[38]:


ax = sns.scatterplot(x='Weight_kg', y='Height_cm', hue='Skill', data=df)


# In[40]:


ax = sns.scatterplot(x='Weight_kg', y='Height_cm', hue='Movement', data=df)


# In[ ]:




