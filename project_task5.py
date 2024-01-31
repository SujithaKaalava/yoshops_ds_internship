#!/usr/bin/env python
# coding: utf-8
'''task 5:
1.Write a python programm for merge two excel file data to one file
Write a python programm to shorting file in different folder means main folder containing 40 word file. Now after shorting create 4 child folder and store 10 file each folder.
2.Write a python programm separate duplicate file.
Check with mobile number in main excel file and test data  doc and if it is same or equal create sperate file and store duplicate file data
3.Write a python programm for Shorting file by keywords.
input: folder path = text value
Create new folder=text value
Search Keyword= text value
Output: Create folder with input value and inside folder all shorting files displaying.
# ### 1.Write a python programm for merge two excel file data to one file'''

# In[10]:


import pandas as pd

#loading the first excel file
df1=pd.read_csv(r'C:\Users\Srinu\Downloads\orders_2016-2020_Dataset1.csv',encoding="ISO-8859-1")
df2=pd.read_csv(r'C:\Users\Srinu\Downloads\orders_2016-2020_Dataset1.csv',encoding="ISO-8859-1")

df_combine=pd.concat([df1,df2])


# In[11]:


df_combine


# In[12]:


df_combine=df_combine.iloc[:,0:6]


# In[13]:


df_combine


# In[14]:


df_combine.to_excel('YoshopsOrderList_NovDec_2022.xlsx', index = False)


# In[15]:


new_df=pd.read_excel('YoshopsOrderList_NovDec_2022.xlsx')
new_df


# ### Write a python programm to shorting file in different folder means main folder containing 40 word file. Now after shorting create 4 child folder and store 10 file each folder.

# In[ ]:





# In[21]:


import os
import shutil

# Specify the main folder path
main_folder_path = r"C:\Users\Srinu\Desktop\Naveen"
# Create four child folders
child_folder_names = ["Folder1", "Folder2", "Folder3", "Folder4"]
child_folder_paths = [os.path.join(main_folder_path, name) for name in child_folder_names]
for folder_path in child_folder_paths:
    os.makedirs(folder_path, exist_ok=True)

# Get a list of all files in the main folder
file_names = os.listdir(main_folder_path)
file_names.sort()

# Distribute files evenly among child folders
files_per_folder = len(file_names) // len(child_folder_paths)
for i, folder_path in enumerate(child_folder_paths):
    start_index = i * files_per_folder
    end_index = start_index + files_per_folder
    files_to_move = file_names[start_index:end_index]
    for file_name in files_to_move:
        src = os.path.join(main_folder_path, file_name)
        dst = os.path.join(folder_path, file_name)
        if os.path.isfile(src):  # Check if the source is a file, not a directory
            shutil.move(src, dst)

# Move remaining files to the last folder
for i, file_name in enumerate(file_names[-(len(file_names) % len(child_folder_paths)):]):
    src = os.path.join(main_folder_path, file_name)
    dst = os.path.join(child_folder_paths[-1], file_name)
    if os.path.isfile(src):  # Check if the source is a file, not a directory
        shutil.move(src, dst)
#print message for completion
print("files stored into child folders successfully")


# ### 2.Write a python programm separate duplicate file

# In[22]:


import os
import hashlib
import shutil

# Specify the directory path
directory_path = r"C:\Users\Srinu\Desktop\Naveen"

# Specify the duplicate folder path
duplicate_folder_path = r"C:\Users\Srinu\Desktop\duplicate"

# Create the duplicate folder if it doesn't exist
os.makedirs(duplicate_folder_path, exist_ok=True)

# Dictionary to store file hashes and corresponding paths
file_hashes = {}

# Iterate over all files in the directory
for root, dirs, files in os.walk(directory_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)

        # Calculate the hash of the file
        with open(file_path, 'rb') as file:
            file_hash = hashlib.md5(file.read()).hexdigest()

        # Check if the hash already exists in the dictionary
        if file_hash in file_hashes:
            # Move the duplicate file to the duplicate folder
            duplicate_file_path = os.path.join(duplicate_folder_path, file_name)
            shutil.move(file_path, duplicate_file_path)
            print(f"Moved duplicate file: {file_path}")
        else:
            # Add the file hash and path to the dictionary
            file_hashes[file_hash] = file_path

print("Duplicate files have been separated.")


# ### Check with mobile number in main excel file and test data  doc and if it is same or equal create sperate file and store duplicate file data

# In[38]:


import pandas as pd
from docx import Document

# File paths
excel_file_path = "random_data.xlsx"
test_data_doc_path = "test_data.docx"
output_file_path = "task5_output_file_mobile.xlsx"

# Read the main Excel file
excel_data = pd.read_excel(excel_file_path)

# Read the test data document as a Word document
doc = Document(test_data_doc_path)

# Extract mobile numbers from both data sources
excel_mobile_numbers = set(excel_data['Mobile Number'].astype(str))
test_data_mobile_numbers = set()

# Read mobile numbers from the test data document
for table in doc.tables:
    for row in table.rows[1:]:
        test_data_mobile_numbers.add(row.cells[1].text.strip())

# Find common mobile numbers
duplicate_mobile_numbers = excel_mobile_numbers.intersection(test_data_mobile_numbers)

# Filter duplicate data from the main Excel file
duplicate_data = excel_data[excel_data['Mobile Number'].astype(str).isin(duplicate_mobile_numbers)]

# Save the duplicate data to a separate file
duplicate_data.to_excel(output_file_path, index=False)
print("Duplicate data has been stored in a separate file.")


# In[30]:





# ### 3.Write a python programm for Shorting file by keywords.
# 

# In[ ]:





# In[ ]:





# In[45]:


import os
import shutil

def sort_files_by_keyword(folder_path, new_folder_name, keyword):
    # Create a new folder
    new_folder_path = os.path.join(folder_path, new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)

    # List of encodings to try
    encodings = ['utf-8', 'latin-1']

    # Iterate over files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            # Check if the file contains the keyword
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as file:
                        content = file.read()
                        if keyword in content:
                            # Move the file to the new folder
                            new_file_path = os.path.join(new_folder_path, filename)
                            try:
                                shutil.move(file_path, new_file_path)
                                print(f"Moved file '{filename}' to '{new_folder_name}' folder.")
                            except PermissionError as e:
                                print(f"Failed to move file '{filename}': {str(e)}")
                            break
                except UnicodeDecodeError:
                    continue

# Example usage
folder_path = input("Enter the folder path: ")
new_folder_name = input("Enter the new folder name: ")
keyword = input("Enter the keyword to search: ")

sort_files_by_keyword(folder_path, new_folder_name, keyword)


# In[ ]:




