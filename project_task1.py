
from bs4 import BeautifulSoup
import requests
from urllib import request
fp=request.urlopen("https://yoshops.com/")
bytes=fp.read()
htmlstr=bytes.decode("utf8")
soup=BeautifulSoup(htmlstr,"html.parser")
print(soup.prettify())


# In[29]:


category=[]
caturls=[]
url=soup.findAll('ul',{'class':'category bar'})
#print(url)
links=[]

link=soup.findAll('ul',class_="nav category-bar")
for i in link:
    for j in soup.findAll('li',class_="dropdown"):
        a=j.find('a')
        if 'href' in a.attrs:
            url=a.get('href')
            category.append(a.contents)
            caturls.append(url)
print(caturls)
print(category)


# In[8]:


catdict={}
for i in category:
    catdict[i[0].strip()]={}
print(catdict)


# In[ ]:





# In[64]:



subcategory={}
soup=BeautifulSoup(htmlstr,"html.parser")
link=soup.findAll('ul',class_="category-bar")
for i in link:
    for j in soup.findAll('li',class_="dropdown"):
        a=j.find('a')
        url=a.get('href')
        key=a.contents[0].strip()
        for ul in j.findAll("ul",class_="dropdown-menu"):
            for a in ul.findAll("a"):
                if 'href' in a.attrs:
                    url=a.get('href')
                    subcategory[a.contents[0]]=url
                    catdict[key][a.contents[0]]={}
                    catdict[key][a.contents[0]]['url']=url
                    catdict[key][a.contents[0]]['count']=0
print(catdict)


# In[74]:


page=request.urlopen("https://yoshops.com/t/drones")
bytes=page.read()
htmlstr=bytes.decode('utf8')
tempsoup=BeautifulSoup(htmlstr,"html.parser")
div=tempsoup.find('div',class_='content')
products=div.findAll('div',class_='products')
allproducts=products[0].findAll('div',class_='product')
print(len(allproducts))


# In[82]:


for key in catdict:
    sub=catdict[key]
    for k in sub:
        url=sub[k]['url']
        page=request.urlopen("https://yoshops.com"+url+" ")
        bytes=page.read()
        htmlstr=bytes.decode('utf8')
        tempsoup=BeautifulSoup(htmlstr,"html.parser")
        div=tempsoup.find('div',class_='content')
        products=div.findAll('div',class_='products')
        allproducts=products[0].findAll('div',class_='product')
        catdict[key][k]['count']=len(allproducts)


# # writing into an excel file

# In[91]:


import xlsxwriter
wb=xlsxwriter.Workbook("project_task1_sol.xlsx")
bold=wb.add_format({'bold':True})
ws=wb.add_worksheet()
ws.write('A1','s.no',bold)
ws.write('B1','category',bold)
ws.write('C1','sub category',bold)
ws.write('D1','product_count',bold)
row=1

col=0
sno=1
for i in catdict:
    for j in catdict[i]:
        ws.write(row,col,sno)
        ws.write(row,col+1,i)
        ws.write(row,col+2,j)
        if i in subcategory and j in subcategory[i]:
            ws.write(row,col+3,subcategory[i][j]['count'])
        else:
            ws.write(row,col+3,'0')
        sno=sno+1
        row+=1
wb.close()
        


# In[88]:





# In[ ]:




