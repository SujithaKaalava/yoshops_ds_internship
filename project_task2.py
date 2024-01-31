#!/usr/bin/env python
# coding: utf-8

# In[121]:


# importing the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv(r'C:\Users\Srinu\Downloads\orders_2016-2020_Dataset1.csv',encoding="ISO-8859-1")
data['Payment Method']


# In[3]:


data.sample(4)


# In[62]:


data.info


# In[5]:


reviewdata=pd.read_csv(r'C:\Users\Srinu\Downloads\review_dataset.csv')
reviewdata.tail(10)


# ## data cleaning

# In[6]:


reviewdata.dropna()


# In[7]:


index=reviewdata['stars'].value_counts().keys()[0:10]
index


# In[8]:


count=reviewdata['stars'].value_counts()[0:10]
count.astype(int)


# In[9]:


data['Order Date and Time Stamp']=pd.to_datetime(data['Order Date and Time Stamp'])
data['Order Date and Time Stamp']


# In[79]:


reviewdata
data['Payment Method']


# In[11]:


dfnew=pd.DataFrame()
dfnew['Order Date and Time Stamp']=data['Order Date and Time Stamp']


# In[63]:


dfnew['total']=data['Subtotal']
dfnew['product name']=reviewdata['product_name']
dfnew['payment method']=data['Payment Method']
dfnew['stars']=reviewdata['stars']
dfnew['LineItem Name']=data['LineItem Name']
dfnew['Shipping Method']=data['Shipping Method']
dfnew['category']=reviewdata['category']
dfnew['price']=data['LineItem Sale Price']
dfnew['quantity']=data['LineItem Qty']
dfnew['Payment Status']=data['Payment Status']
dfnew.columns


# In[13]:


def price1(price):
    if price<100:
        return 'cheap'
    elif price<200:
        return 'moderate'
    else:
        return 'expensive'


# In[ ]:





# In[ ]:





# # year wise quantity of products

# In[64]:


dfnew['Date']=dfnew['Order Date and Time Stamp'].dt.date

dfnew['month']=dfnew['Order Date and Time Stamp'].dt.month
dfnew['year']=dfnew['Order Date and Time Stamp'].dt.year
plt.figure(figsize=(15,6))
plt.plot(dfnew['year'],dfnew['quantity'])
plt.xticks(rotation='vertical')
plt.show()


# # MOST PREFERD SHIP MODE

# In[16]:


plt.xticks(rotation='vertical')
sns.countplot(dfnew['Shipping Method'])


# In[139]:



def payment_method():
    index=data['Payment Method'].value_counts().keys()[0:10]
    freq=data['Payment Method'].value_counts()[0:10]
    plt.xticks(rotation='vertical')
    sns.barplot(x=index,y=freq)
    plt.title('Payment Method Distribution')
    plt.savefig('payment_method.png')
    # Save the plot into an existing Excel file
    writer = pd.ExcelWriter('task2_sol.xlsx', engine='xlsxwriter')
    workbook = writer.book
    payment_sheet = workbook.add_worksheet('Payment Method')
    payment_sheet.insert_image('B2', 'payment_method.png')
    writer.save()
payment_method()


# # 1.analysis of review dataset

# In[147]:


def reviews_of_customer():
    
    plt.xticks(rotation='vertical')
    sns.countplot(reviewdata['stars'])
    plt.title('analysis of reviews given by customer')
#reviews_of_customer()
def  review1():
    index=reviewdata['stars'].value_counts().keys()[0:10]
    freq=reviewdata['stars'].value_counts()[0:10]
    sns.barplot(y=index,x=freq)
    plt.title('review rating')
    plt.xlabel('frequency')
    plt.savefig('review_rating.png')

    # create a Pandas Excel writer using XlsxWriter as the engine
    writer = pd.ExcelWriter('task2_sol.xlsx', engine='xlsxwriter')

    # convert the Pandas dataframe to an Excel worksheet
    review_df = pd.DataFrame({'index': index, 'freq': freq})
    review_df.to_excel(writer, sheet_name='Review Data', index=False)

    # insert the image into the Excel worksheet
    workbook = writer.book
    worksheet = writer.sheets['Review Data']
    worksheet.insert_image('E2', 'review_rating.png')

    # save the Excel file
    writer.save()

review1()


# In[19]:


dfnew.head(20)
data
reviewdata


# In[25]:


#payment method analysis
plt.xticks(rotation='vertical')
sns.countplot(data['Payment Method'])
plt.title("payment method analysis")


# In[26]:


data.columns


# # customer states analysis
# 

# In[155]:


def consumer_state_analysis():
    index=data['Shipping State'].value_counts().keys()[0:10]
    freq=data['Shipping State'].value_counts()[0:10]
    plt.xticks(rotation='vertical')
    sns.barplot(x=index,y=freq)
    plt.title('customer state analysis')
    plt.savefig('consumer_state_analysis.png')
consumer_state_analysis()


# # 5.analysis of product analysis

# In[149]:


def product_analysis():
    index=data['LineItem Name'].value_counts().keys()[0:10]
    freq=data['LineItem Name'].value_counts()[0:10]
    plt.xticks(rotation='vertical')
    sns.barplot(x=index,y=freq)
    plt.xlabel("product name")
    plt.ylabel("no of products")
    plt.title("product analysis")
    plt.savefig('product_analysis.png')
product_analysis()


# # 6. analysis of all product category reviews

# In[150]:


def category_reviews():
    review_cat=dfnew.groupby('category')['stars'].count()
    review_cat.plot.bar(figsize=(15,6))
    plt.xlabel("categories")
    plt.ylabel("no of reviews")
    plt.title('top selling product category reviews')
    plt.savefig('category_reviews.png')
category_reviews()


# In[30]:


dfnew['Date']=pd.to_datetime(dfnew['Date'])


# In[31]:


dfnew['month-year']=dfnew['Date'].dt.strftime('%m %Y')


# In[32]:


dfnew['month-year']


# # 8.reviews by month and year

# In[157]:


#creting and saving the reviews_by_month_year() method in a excel sheet
def reviews_by_month_year():
    plt.figure(figsize=(15,8))
    plt.xticks(rotation='vertical')
    ax=sns.countplot(x='month-year',hue='stars',data=dfnew)
    plt.ylabel('no of reviews')
    plt.title('reviews by month and year')
    plt.savefig('reviews_by_month_year.png')
reviews_by_month_year()


# # consumer cities analysis

# In[152]:


def consumer_city_analysis():
    index=data['Shipping City'].value_counts().keys()[0:10]
    freq=data['Shipping City'].value_counts()[0:10]
    plt.xticks(rotation='vertical')
    sns.barplot(x=index,y=freq)
    plt.title('customer city analysis')
    plt.savefig('consumer_city_analysis.png')
consumer_city_analysis()


# # 7.no of orders per month

# In[35]:


dfnew['orders']=data['Order #']
order=dfnew.groupby('month')['orders'].count()
order


# In[36]:


def orders_per_year():
    orders_per_year=dfnew['year'].value_counts()
    orders_per_year.plot.bar(figsize=(15,6))
    plt.xlabel('year')
    plt.ylabel('no of orders')
    plt.title('orders per year')
def orders_per_month():
    orders_per_month=dfnew['month'].value_counts()
    orders_per_month.plot.bar(figsize=(15,6))
    plt.xlabel('month number')
    plt.ylabel('no of orders')
    plt.title('orders per month')
print(orders_per_year())
print(orders_per_month())


# ### 7.orders per month-year

# In[156]:


#defining orders_per_month_year () and saving it into the excel file
def orders_per_month_year():
    index=dfnew['month-year'].value_counts().keys()[0:10]
    freq=dfnew['month-year'].value_counts()[0:10]
    sns.barplot(x=index,y=freq)
    plt.xlabel('month-year')
    plt.xticks(rotation='vertical')
    plt.ylabel('no of orders')
    plt.title('orders per month-year')
    #plt.savefig(r'C:\Users\Srinu\Desktop\sujitha\project_task2_sol.xlsx')
    plt.savefig('orders_per_month_year.png')
    
#data['Payment Method']


# # 9.no of orders across parts of the day

# In[38]:


dfnew['hours']=data['Order Date and Time Stamp'].dt.hour


# In[39]:



def time_analysis(x):
    if x<11:
        return 'morning'
    elif x<16:
        return 'afternoon'
    elif x<20:
        return 'evening'
    else:
        return 'night'
dfnew['parts od day']=dfnew['hours'].apply(time_analysis)


# In[158]:


def orders_across_parts_of_day():
    index=dfnew['parts od day'].value_counts().keys()[0:10]
    freq=dfnew['parts od day'].value_counts()[0:10]
    plt.xticks(rotation='vertical')
    sns.barplot(x=index,y=freq)
    plt.title('analysis of no of orders across parts of the day')
    plt.savefig('orders_across_parts_of_day.png')
    

orders_across_parts_of_day()


# In[41]:


def all_reports():
    print('full report')
    
    reviews_of_customer()
   
    payent_method()
    
    consumer_state_analysis()
    
    consumer_city_analysis()
    
    product_analysis()
    
    category_reviews()
   
    orders_per_year()
   
    orders_per_month()
    
    orders_per_month_year()
    
    reviews_by_month_year()
    
    orders_across_parts_of_day()


# In[42]:


choice=int(input("Enter Your Choice:"))
if choice==1:
    print('analysis of reviews given by customer')
    reviews_of_customer()
elif choice==2:
    print('analysis of different payment methods used by customer')
    payent_method()
elif choice==3:
    print('analysis of top consumer states..')
    consumer_state_analysis()
    
elif choice==4:
    print('analysis of top consumer cities...')
    consumer_city_analysis()
    
elif choice==5:
    print('analysis of top selling product categories...')
    product_analysis()
    
elif choice==6:
    print('analysis of all product category reviews')
    category_reviews()
    
elif choice==7:
    print('no of orders per year')
    orders_per_year()
    print('no of orders per month')
    orders_per_month()
    print('orders per month-year')
    orders_per_month_year()
    
elif choice==8:
    print('reviews of no of orders per month year')
    reviews_by_month_year()
    
elif choice==9:
    print('no of orders across the parts of the day')
    orders_across_parts_of_day()
elif choice==10:
    all_reports()
else:
    print('invalid choice......!')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:



    # Save the plot into the existing Excel file
    writer = pd.ExcelWriter('task2_sol.xlsx', engine='xlsxwriter')
    workbook = writer.book
    worksheet1 = writer.sheets['']
    worksheet1.insert_image('B10', 'category_reviews.png')
    worksheet2 = workbook.add_worksheet('Orders by Month-Year')
    worksheet2.insert_image('B10', 'orders_per_month_year.png')
    worksheet3 = workbook.add_worksheet('Orders across Parts of Day')
    worksheet3.insert_image('B10', 'orders_across_parts_of_day.png')
    worksheet4 = workbook.add_worksheet('Payment Method')
    worksheet4.insert_image('B2', 'payment_method.png')
    writer.save()


# In[ ]:





# ## saving all the plots into an excel file

# In[164]:


# creating an object to anexcel sheet
writer = pd.ExcelWriter('task2_sol.xlsx', engine='xlsxwriter')
workbook = writer.book

#saving the review_rating plot in excel

worksheet1 = workbook.add_worksheet('reviews of customer')
worksheet1.insert_image('B10', 'review_rating.png')
  
    #saving the payment_method plot in excel
    
worksheet2 = workbook.add_worksheet('payment methods')
worksheet2.insert_image('B10', 'payment_method.png')
    
#saving the consumer_state_analysis plot in excel
    
worksheet3 = workbook.add_worksheet('consumer state analysis')
worksheet3.insert_image('B10', 'consumer_state_analysis.png')
    
#saving the consumer_city_analysis plot in excel
 
worksheet4 = workbook.add_worksheet('consumer city analysis')
worksheet4.insert_image('B2', 'consumer_city_analysis.png')
    
#saving the product_analysis plot in excel
 
worksheet5 = workbook.add_worksheet('product analysis')
worksheet5.insert_image('B10', 'product_analysis.png')
    
#saving the category_reviews plot in excel
 
worksheet6 = workbook.add_worksheet('review_all_categories')
worksheet6.insert_image('B2', 'category_reviews.png')
    
#saving the orders_per_month_year plot in excel

worksheet7 = workbook.add_worksheet('orders_per_month_year')
worksheet7.insert_image('B10', 'orders_per_month_year.png')
    
   #saving the reviews_by_month_year plot in excel
    
worksheet8 = workbook.add_worksheet('reviews_by_month_year')
worksheet8.insert_image('B2', 'reviews_by_month_year.png')
    
#saving theorders_across_parts_of_day plot in excel

worksheet9 = workbook.add_worksheet('orders_across_parts_of_day')
worksheet9.insert_image('B10', 'orders_across_parts_of_day.png')
    
    
writer.save()


# In[ ]:





# ## saving all the plots in a pdf file

# In[ ]:


from matplotlib.backends.backend_pdf import PdfPages

# Create a PDF file to save the plots
pdf_file = 'task2_sol.pdf'
pdf_pages = PdfPages(pdf_file)

# Plot 1: reviews of customer
reviews_of_customer()
pdf_pages.savefig()

#plot2:payment_method

payent_method()
pdf_pages.savefig()

#plot3:consumer state analysis
    
consumer_state_analysis()
pdf_pages.savefig()

#plot4:consumer city analysis
    
consumer_city_analysis()
pdf_pages.savefig()

#plot5:product category analysis

product_analysis()
pdf_pages.savefig()

#plot6:all product category reviews

category_reviews()
pdf_pages.savefig()

#plot7:orders per month

orders_per_year()
pdf_pages.savefig()

#orders per year

orders_per_month()
pdf_pages.savefig()

#orders per onth-year

orders_per_month_year()
pdf_pages.savefig()

#plot8:reviews by month year

reviews_by_month_year()
pdf_pages.savefig()

#plot9:orders_across_parts_of_day

orders_across_parts_of_day()
pdf_pages.savefig()

# Close the PDF file
pdf_pages.close()


# In[ ]:




