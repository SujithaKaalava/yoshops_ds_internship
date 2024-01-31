#!/usr/bin/env python
# coding: utf-8
PROJECT TASK 3
Automation : Products Page Automation Validation
Write a python programm to find product page where Products Image missing.
Enter 1 for Input value  = Yoshops.com
Enter 2 for Input value= Any main categories and sub categories Link
Output = create excel file with  web url, Products name, Products Details, contact no and address columns.
task - Work flow logic:
First  get the url of each product so that you can check whether their images are missing or not in the next step.
To do that  using beautiful soup or Auto Scraper lib file which requires a raw html code or webpage as a parameter and not a url(ie. yoshops.com).
You decided to use the request package to get the yoshops.com webpage so that you can pass it to beautiful soup but having permission issues.
Use urllib open instead of request get
# ###### IMPORTING THE REQUIRED LIBRARIES

# In[34]:


from bs4 import BeautifulSoup
import requests
from urllib import request

category='toys'

url='https://yoshops.com/t/'+category.lower()
headers={'User-Agent':'Mozilla/5.0'}
webpage=requests.get(url,headers=headers)
soup=BeautifulSoup(webpage.content,'html.parser')
table=soup.find('ul',class_='nav category-bar')
sub=table.findAll('li')
table


# In[18]:


sub


# In[19]:


link=[]

for i in range(1,62):
    y=sub[i].find('a',href=True)
    link.append(y.get('href'))


# In[20]:


#sub category products
link


# In[21]:


final_link=[]
for i in link:
    final_link.append('https://yoshops.com'+i)


# In[22]:


#all product category links
final_link


# In[24]:


#web page link 
def web_page():
    print('https://yoshops.com')
#all the sub links in a web page
def sub_links():
    for i in final_link:
        print(i)


# # enter 1 to input value of web page link ,enter 2 for sub links in webpage

# In[27]:


print('1.web page link')
print('2.sub links in a web page')
choice=int(input('enter the choice'))
if choice==1:
    web_page()
if choice==2:
    sub_links()


# In[2]:


#taking input web page url
url=input('Input url :')


# In[24]:


#category url
category_name=input("input category/sub-category: ")


# In[25]:


search_link= url+'/t/'+category_name
search_link


# In[36]:


from urllib import request
def connectsite(search_link,page=1):
    soup=''
    headers={}
    if page==1:
        url=search_link.lower()
    else:
        url=search_link.lower()+page
    headers=headers={'User-Agent':'Mozilla/5.0'}
    req=request.Request(url,headers=headers)
    resp=request.urlopen(req)
    respData=resp.read()
    
    #convert string to HTML
    soup=BeautifulSoup(respData,'html.parser')
    return soup


# In[37]:


connectsite(search_link,page=1)


# In[35]:


def getpagenoifnextpageexist(soup):
    paginations_class=soup.find(attrs={'class':'pagination pull-right'})
    
    if paginations_class==None:
        return
    paginations_arrow_class=paginations_class.findAll('li')
    if paginations_arrow_class[-1].attrs['class'][-1]!='disabled':
        return paginations_arrow_class[-1].a['href']


# In[29]:


def productwithnoimage(search_link,soup):
    no_product_image=[]
    
    while True:
        product_links=soup.findAll('a',class_='product-link')
        
        #loop through each product link and check if image is missing
        for link in product_links:
            
            # GET the url for product page
            product_img_link=link.find('img')['src']
            if 'noimage' in product_img_link:
                product_url=url+'/t'+link['href']
                product_name=link.find('span').text
                
                no_product_image.append([category_name,product_name,product_url])
        page_exists=getpagenoifnextpageexist(soup)
        if page_exists:
            soup=connectsite('https://yoshops.com/t/food',page_exists)
        else:
            return no_product_image


# In[30]:


import pandas as pd
soup=connectsite(search_link)

# storing the products with no image in data

data=productwithnoimage('https://yoshops.com/t/food',soup)

df_product_no_image=pd.DataFrame(data,columns=(['category','product_name','product_url']))


# In[31]:


df_product_no_image


# In[33]:


# storing into an excel sheet
df_product_no_image.to_excel('project_task3_sol.xlsx',index=False)


# In[ ]:





# In[ ]:




