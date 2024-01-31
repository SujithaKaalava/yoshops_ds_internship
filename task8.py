#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import tkinter as tk
from tkinter import messagebox

def generate_bill():
    name = name_entry.get()
    phone_no = phone_entry.get()
    food_item_no = [item_var.get() for item_var in food_item_vars if item_var.get() != ""]

    if not name or not phone_no or not food_item_no:
        messagebox.showerror("Error", "Please enter all the required information.")
        return

    # Dictionary to store food item prices
    menu = {
        1: {"item": "Ambur Biryani", "price": 150},
        2: {"item": "Chicken 65", "price": 120},
        3: {"item": "Mutton Curry", "price": 180},
        4: {"item": "Veg Pulao", "price": 100},
        5: {"item": "Gulab Jamun", "price": 60}
    }

    # Calculate total price based on food item numbers
    total_price = sum(menu[int(item)]["price"] for item in food_item_no)

    # Generate bill content
    bill_content = f"Name: {name}\nPhone No: {phone_no}\n\n"
    bill_content += "Food Items:\n"
    for item in food_item_no:
        bill_content += f"- {menu[int(item)]['item']}: {menu[int(item)]['price']} INR\n"
    bill_content += f"\nTotal Price: {total_price} INR"

    # Generate bill file name
    bill_file_name = f"{name.replace(' ', '_')}_bill.txt"

    # Save bill to a folder named "bills"
    folder_path = "bills"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    bill_file_path = os.path.join(folder_path, bill_file_name)

    # Save the bill to a text file
    with open(bill_file_path, "w") as file:
        file.write(bill_content)

    messagebox.showinfo("Success", "Bill generated successfully!")
    messagebox.showinfo("Bill Path", f"Bill saved as: {bill_file_path}")


# Create GUI window
window = tk.Tk()
window.title("Ambur Biryani Billing System")

# Create labels and entry fields
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

phone_label = tk.Label(window, text="Phone No:")
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

food_item_label = tk.Label(window, text="Food Items:")
food_item_label.pack()

food_item_vars = []
menu = {
    1: "Ambur Biryani - 150 INR",
    2: "Chicken 65 - 120 INR",
    3: "Mutton Curry - 180 INR",
    4: "Veg Pulao - 100 INR",
    5: "Gulab Jamun - 60 INR"
}

for item, item_text in menu.items():
    item_var = tk.StringVar()
    item_checkbox = tk.Checkbutton(window, text=item_text, variable=item_var)
    item_checkbox.pack()
    food_item_vars.append(item_var)

# Create generate bill button
generate_button = tk.Button(window, text="Generate Bill", command=generate_bill)
generate_button.pack()

# Run the GUI window
window.mainloop()


# In[ ]:





# In[ ]:


import os
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

def generate_bill():
    name = name_entry.get()
    phone_no = phone_entry.get()
    food_item_no = [item_var.get() for item_var in food_item_vars if item_var.get() != ""]

    if not name or not phone_no or not food_item_no:
        messagebox.showerror("Error", "Please enter all the required information.")
        return

    # Dictionary to store food item prices
    menu = {
        1: {"item": "Ambur Biryani", "price": 150},
        2: {"item": "Chicken 65", "price": 120},
        3: {"item": "Mutton Curry", "price": 180},
        4: {"item": "Veg Pulao", "price": 100},
        5: {"item": "Gulab Jamun", "price": 60}
    }

    # Calculate total price based on food item numbers
    total_price = sum(menu[int(item)]["price"] for item in food_item_no)

    # Generate bill content
    bill_content = f"Name: {name}\nPhone No: {phone_no}\n\n"
    bill_content += "Food Items:\n"
    for item in food_item_no:
        bill_content += f"- {menu[int(item)]['item']}: {menu[int(item)]['price']} INR\n"
    bill_content += f"\nTotal Price: {total_price} INR"

    # Generate bill file name
    bill_file_name = f"{name.replace(' ', '_')}_bill.txt"

    # Save bill to a folder named "bills"
    folder_path = "bills"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    bill_file_path = os.path.join(folder_path, bill_file_name)

    # Save the bill to a text file
    with open(bill_file_path, "w") as file:
        file.write(bill_content)

    bill_text.delete("1.0", tk.END)  # Clear existing bill
    bill_text.insert(tk.END, bill_content)  # Display generated bill in the text widget

    messagebox.showinfo("Success", "Bill generated successfully!")
    messagebox.showinfo("Bill Path", f"Bill saved as: {bill_file_path}")


# Create GUI window
window = tk.Tk()
window.title("Ambur Biryani Billing System")

# Create labels and entry fields
name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(window, text="Phone No:")
phone_label.grid(row=1, column=0, sticky="w")
phone_entry = tk.Entry(window)
phone_entry.grid(row=1, column=1)

food_item_label = tk.Label(window, text="Food Items:")
food_item_label.grid(row=2, column=0, sticky="w")

food_item_vars = []
menu = {
    1: "Ambur Biryani - 150 INR",
    2: "Chicken 65 - 120 INR",
    3: "Mutton Curry - 180 INR",
    4: "Veg Pulao - 100 INR",
    5: "Gulab Jamun - 60 INR",
    6: "Chicken Biryani - 170 INR",
    7: "Paneer Tikka - 140 INR",
    8: "Fish Fry - 160 INR",
    9: "Butter Naan - 50 INR",
    10: "Raita - 30 INR"
}

for item, item_text in menu.items():
    item_var = tk.StringVar()
    item_checkbox = tk.Checkbutton(window, text=item_text, variable=item_var)
    item_checkbox.grid(row=item+2, column=0, sticky="w")
    food_item_vars.append(item_var)

# Create generate bill button
generate_button = tk.Button(window, text="Generate Bill", command=generate_bill)
generate_button.grid(row=0, column=2, rowspan=len(menu)+2)

# Create bill area
bill_text = tk.scrolledtext.ScrolledText(window, height=15, width=40)
bill_text.grid(row=0, column=3, rowspan=len(menu)+2, padx=10, pady=10)

# Run the GUI window
window.mainloop()


# In[ ]:




