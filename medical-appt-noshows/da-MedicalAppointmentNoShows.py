#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Project Name: Medical Appointment No Shows
Which factors can help us to predict if patients would show?
'''

# import packages
import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("noshowappointments-kagglev2-may-2016.csv")


# In[3]:


# check the count of columns and rows
df.shape


# In[4]:


df.head()
# notice ScheduleDay and AppointmentDay values has incorrect 'Z' and 'T'
# No-show and SMS_received column name format is incorrect


# In[5]:


df.info()
# notice there is no nan values
# some datatypes may be changed: 
# PatientID,ScheduledDay,AppointmentDay


# In[6]:


# check any duplicated rows
df.duplicated().sum()
# no duplications


# In[7]:


# rename No-show and SMS_received columns name
df.rename(columns={'No-show':'NoShow','SMS_received':'SmsReceived'},inplace=True)

#check if rename correctly
df.info()


# In[8]:


# check detailed datatypes of some columns
type(df.AppointmentDay)


# In[ ]:


# delete 'Z' and 'T' in ScheduledDay and AppointmentDay values
def dele(columns): 
        df[columns] = df[columns].apply(lambda x:x.replace('Z',' '))
        df[columns] = df[columns].apply(lambda x:x.replace('T',' '))
        return columns
dele('ScheduledDay')
dele('AppointmentDay')

# check if changed correctly


# In[ ]:


# change datatypes
df.head()


# In[11]:


df.describe()

# age has abnormal values which index is 99832
df['Age'].replace(-1,0,inplace=True)


# In[12]:


df.describe()


# In[13]:


df.duplicated().sum()
#no duplicated rows


# In[14]:


df.head(20)


# In[15]:


df.isnull().sum()

# no NaN values


# In[16]:


# change datatype: PatientId,ScheduledDay,AppointmentDay

df[['ScheduledDay','AppointmentDay']] = df[['ScheduledDay','AppointmentDay']].apply(pd.to_datetime)
df['PatientId'] = df['PatientId'].astype(int)


# In[17]:


df.info()


# In[18]:


df.describe()


# In[36]:


# change 'yes' to 1, change 'no' to o

df['NoShow'].replace(1,'Yes',inplace=True)
df['NoShow'].replace(0,'No',inplace=True)


# In[37]:


df.head(10)


# In[24]:


df.hist(figsize = (12,12))


# In[35]:


# noshow_per = df.query("NoShow = 1").sum()/df['NoShow'].count()

df.query('NoShow==1').count()


# In[38]:


# question 1: if gender affects 
not_showing = df.query('NoShow == "Yes"')
showup = df.query('NoShow == "No"')
not_showing


# In[40]:


total_count = df.Gender.value_counts()
total_count


# In[42]:


not_showing_count = not_showing.Gender.value_counts()
not_showing_count


# In[44]:


female_not = not_showing_count[0]/total_count[0]
male_not = not_showing_count[1]/total_count[1]
female_not,male_not


# In[57]:


locations = range(2)
heights = [female_not,male_not]
labels = ['Female','Male']
plt.bar(locations,heights,alpha=0.8,color=['tomato','skyblue'],tick_label=labels)
plt.title('Gender Difference in Not Showing Patients')
plt.ylim(0,0.25)
plt.xlabel('Gender')
plt.ylabel('Proportion for gender')


# In[49]:


# question 2: if age affects 

not_showing.Age.mean()


# In[50]:


showup.Age.mean()


# In[55]:


not_showing.Age.hist(alpha=0.8)
plt.title('Age Distribution for Notshowing Patients')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.ylim(0,4500)


# In[63]:


showup.Age.hist(alpha=0.8)
plt.title('Age Distribution for Showup Patients')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.ylim(0,17000)


# In[68]:


# question 3: if sms receive affects
not_sms = not_showing.SmsReceived.value_counts()
not_sms


# In[69]:


showup_sms = showup.SmsReceived.value_counts()
showup_sms


# In[75]:


plt.title('SMS receive in Notshowing Patients')
plt.xlabel('sms receive')
plt.ylabel('Number of Patients')
locations = range(2)
labels= ['Not received','Received']
heights= [not_sms[0],not_sms[1]]
plt.bar(locations,heights,alpha=0.8,color=('tomato','lightgreen'),tick_label=labels)


# In[77]:


plt.title('SMS receive in Showup Patients')
plt.xlabel('sms receive')
plt.ylabel('Number of Patients')
locations = range(2)
labels= ['Not received','Received']
heights= [showup_sms[0],showup_sms[1]]
plt.bar(locations,heights,alpha=0.8,color=('tomato','lightgreen'),tick_label=labels)


# In[79]:


# output 
from subprocess import call
call(['python3','-m','nbcovert','da-MedicalAppointmentNoShows.ipynb'])
#incorrect


# In[ ]:




