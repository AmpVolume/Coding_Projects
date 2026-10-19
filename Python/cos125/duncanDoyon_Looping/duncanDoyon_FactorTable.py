# **NO AI USED**
# File: duncanDoyon_FactorTable.py
# Author: Duncan Doyon
# Date: 10/13/2026
# Section: Homework 3
# E-mail: duncan.doyon@maine.edu
# Description:
# A simulation many diffrent looping methods

max_number = int(input("Enter Max Number: "))

print("\n===== FACTOR TABLE =====")
print("Number\tSmallest Factor")
print("-----------------------")

for number in range(2, max_number + 1):
    factor = 2
    while number % factor != 0:
        factor += 1
    print(f"{number}\t{factor}\n")
