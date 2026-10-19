# **NO AI USED**
# File: duncanDoyon_MemoryCopy.py
# Author: Duncan Doyon
# Date: 10/13/2026
# Section: Homework 3
# E-mail: duncan.doyon@maine.edu
# Description:
# A simulation many diffrent looping methods

inventory = ["Apples", "Bananas", "Cherries"]
ref_inventory = inventory

copy_inventory = inventory[:]

print("Before modifying the inventory:")
print(f"inventory: {inventory}")
print(f"ref_inventory: {ref_inventory}")
print(f"copy_inventory: {copy_inventory}")

inventory.append("Oranges")

inventory.pop(1)

print("\nAfter modifying the inventory:")
print(f"inventory: {inventory}")
print(f"ref_inventory: {ref_inventory}")
print(f"copy_inventory: {copy_inventory}")

# Explanation:
print("\nExplanation:")
print("inventory and ref_inventory refer to the same list.")
print("Changes made to inventory also appear in ref_inventory.")
print("copy_inventory was created with slicing, so it is a separate list.")
print("Changes to inventory do not change the items in copy_inventory.")
