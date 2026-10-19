# **NO AI USED**
# File: duncanDoyon_DataCleaner.py
# Author: Duncan Doyon
# Date: 10/13/2026
# Section: Homework 3
# E-mail: duncan.doyon@maine.edu
# Description:
# A simulation many diffrent looping methods

outer_list = []

for i in range(3):
    user_input = input(f"Enter comma-separated values for list {i + 1}: ")
    items = user_input.split(",")
    outer_list.append(items)

cleaned_list = []

for element in outer_list:
    cleaned_element = []
    for item in element:
        if len(item) > 0:
            if item.isdigit():
                cleaned_element.append(int(item))
            elif item[0] == "-" and len(item) > 1 and item[1:].isdigit():
                cleaned_element.append(int(item))
            else:
                cleaned_element.append(item)
        else:
            cleaned_element.append(item)
    cleaned_list.append(cleaned_element)

print("\n===== CLEANED DATA =====")

for element in cleaned_list:
    print(f"\t{element}")
