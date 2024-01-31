#!/usr/bin/env python
# coding: utf-8
'''Task-6
Payroll ATS
1. pay slips generate monthly one time
2. cash flow report a. for chennai
   b. for franchises (Aurangabad)
3. Balance Sheet report a. for chennai
   b. for aurangabad
4. Stack holder distribute(profit) report'''
# In[6]:


import pandas as pd

#pay slip for december
#read data rom excel file
df=pd.read_excel(r'C:\Users\Srinu\Downloads\Kalyani_Balance_Sheet_December_2022.xlsx')
df['Chennai'].count()

df
#no of studens in chennai and aurangabad
chennai_students=df['Chennai'].count()

aurangabad_students=df['Aurangabad'].count()

#fees of chennai and aurangabad students
chennai_fee=df['Chennai'].sum()
aurangabad_fee=df['Aurangabad'].sum()

#pay slip for the chennai

print('pay slip for chennai')
print('total no of students of chennai',chennai_students)
print('total fee of students in chennai',chennai_fee)
print()
#pay slip for Aurangabad

print('pay slip for aurangabad')
print('total no of students of Aurangabad',aurangabad_students)
print('total fee of students in aurangabad',aurangabad_fee)
print()
#total pay slip
print('total no of students of chennai',chennai_students)
print('total no of students of Aurangabad',aurangabad_students)
print('total fee of students in chennai',chennai_fee)
print('total fee of students in aurangabad',aurangabad_fee)
print('total students in both cities',chennai_students+aurangabad_students)
print('total fee payed by students in both cities',chennai_fee+aurangabad_fee)


# In[7]:


import pandas as pd
#pay slip for november

#read data rom excel file
df1=pd.read_excel(r'C:\Users\Srinu\Downloads\Kalyani_Balance_Sheet_November_2022.xlsx')
df1['Chennai'].count()

df1
#no of studens in chennai and aurangabad
chennai_students=df1['Chennai'].count()

aurangabad_students=df1['Aurangabad'].count()

#fees of chennai and aurangabad students
chennai_fee=df1['Chennai'].sum()
aurangabad_fee=df1['Aurangabad'].sum()


#pay slip for the chennai

print('pay slip for chennai')
print('total no of students of chennai',chennai_students)
print('total fee of students in chennai',chennai_fee)
print()
#pay slip for Aurangabad

print('pay slip for aurangabad')
print('total no of students of Aurangabad',aurangabad_students)
print('total fee of students in aurangabad',aurangabad_fee)
print()
#total pay slip
print('total no of students of chennai',chennai_students)
print('total no of students of Aurangabad',aurangabad_students)
print('total fee of students in chennai',chennai_fee)
print('total fee of students in aurangabad',aurangabad_fee)
print('total students in both cities',chennai_students+aurangabad_students)
print('total fee payed by students in both cities',chennai_fee+aurangabad_fee)


# In[8]:


df.iloc[:,0:6]


# In[ ]:





# In[ ]:





# ### 2. cash flow report a. for chennai b. for franchises (Aurangabad),3. Balance Sheet report a. for chennai b. for aurangabad4. Stack holder distribute(profit) report for NOVEMBER

# In[9]:


import pandas as pd

# Assuming the table data is stored in a pandas DataFrame called 'df'

# Cash Flow Report for Chennai
chennai_cash_flow_report = df[['Name', 'Chennai']]
chennai_cash_flow_report = chennai_cash_flow_report.dropna()

print("Cash Flow Report for Chennai:")
print(chennai_cash_flow_report)

# Cash Flow Report for Aurangabad
aurangabad_cash_flow_report = df[['Name', 'Aurangabad']]
aurangabad_cash_flow_report = aurangabad_cash_flow_report.dropna()

print("Cash Flow Report for Aurangabad:")
print(aurangabad_cash_flow_report)

# Balance Sheet Report for Chennai
chennai_balance_sheet_report = df[['Name', 'Chennai.1']]
chennai_balance_sheet_report = chennai_balance_sheet_report.dropna()

print("Balance Sheet Report for Chennai:")
print(chennai_balance_sheet_report)

# Balance Sheet Report for Aurangabad
aurangabad_balance_sheet_report = df[['Name', 'Aurangabad.1']]
aurangabad_balance_sheet_report = aurangabad_balance_sheet_report.dropna()

print("Balance Sheet Report for Aurangabad:")
print(aurangabad_balance_sheet_report)

# Stakeholder Distribution (Profit) Report
profit_distribution_report = df[['Name', 'Unnamed: 6']]
profit_distribution_report = profit_distribution_report.dropna()

print("Stakeholder Distribution (Profit) Report:")
print(profit_distribution_report)


# ### Stakeholder profile ratio in different cities december

# In[10]:


import matplotlib.pyplot as plt
label="Aurangabad","Chennai"
sizes=[df1['Aurangabad'].sum(),df1['Chennai'].sum()]
colors=["#e0707c", "#F5DADF"]
explode=(0,0.3)

plt.pie(sizes,explode=explode,labels=label,autopct="%1.1f%%",shadow=True,startangle=90,colors=colors)
plt.title("Stakeholder profile ratio in different cities")
fig = plt.gcf()
fig.set_size_inches(6, 6)
plt.legend() 


# ### 2. cash flow report a. for chennai b. for franchises (Aurangabad)3. Balance Sheet report a. for chennai b. for aurangabad,4. Stack holder distribute(profit) report for (DECEMBER)

# In[11]:


import pandas as pd

# Assuming the table data is stored in a pandas DataFrame called 'df'

# Cash Flow Report for Chennai
df=pd.read_excel(r'C:\Users\Srinu\Downloads\Kalyani_Balance_Sheet_December_2022.xlsx')
chennai_cash_flow_report = df[['Name', 'Chennai']]
chennai_cash_flow_report = chennai_cash_flow_report.dropna()

print("Cash Flow Report for Chennai:")
print(chennai_cash_flow_report)

# Cash Flow Report for Aurangabad
aurangabad_cash_flow_report = df[['Name', 'Aurangabad']]
aurangabad_cash_flow_report = aurangabad_cash_flow_report.dropna()

print("Cash Flow Report for Aurangabad:")
print(aurangabad_cash_flow_report)

# Balance Sheet Report for Chennai
chennai_balance_sheet_report = df[['Name', 'Chennai.1']]
chennai_balance_sheet_report = chennai_balance_sheet_report.dropna()

print("Balance Sheet Report for Chennai:")
print(chennai_balance_sheet_report)

# Balance Sheet Report for Aurangabad
aurangabad_balance_sheet_report = df[['Name', 'Aurangabad.1']]
aurangabad_balance_sheet_report = aurangabad_balance_sheet_report.dropna()

print("Balance Sheet Report for Aurangabad:")
print(aurangabad_balance_sheet_report)


# ### Stakeholder profile ratio in different cities november

# In[12]:


import matplotlib.pyplot as plt
label="Aurangabad","Chennai"
sizes=[df['Aurangabad'].sum(),df['Chennai'].sum()]
colors=["#e0707c", "#F5DADF"]
explode=(0,0.3)

plt.pie(sizes,explode=explode,labels=label,autopct="%1.1f%%",shadow=True,startangle=90,colors=colors)
plt.title("Stakeholder profile ratio in different cities")
fig = plt.gcf()
fig.set_size_inches(6, 6)
plt.legend() 


# In[ ]:





# In[ ]:





# In[ ]:




