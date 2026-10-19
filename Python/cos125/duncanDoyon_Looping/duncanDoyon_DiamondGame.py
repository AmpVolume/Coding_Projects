# **NO AI USED**
# File: duncanDoyon_DiamondGame.py
# Author: Duncan Doyon
# Date: 10/13/2026
# Section: Homework 3
# E-mail: duncan.doyon@maine.edu
# Description:
# A simulation many diffrent looping methods

import random

print("Countdown starting!")

for number in range(10, 0, -1):
    print(number)

print("Blast off!")

choice = input("Do you want to enter a peak limit? (yes/no): ")

if choice.lower() == "yes":
    limit = int(input("Enter a peak limit between 3 and 9: "))

    while limit < 3 or limit > 9:
        print("Please enter a number between 3 and 9.")
        limit = int(input("Enter a peak limit: "))
else:
    limit = random.randint(3, 9)
    print(f"Random peak limit selected: {limit}")

print("\nNumber Diamond:")

for number in range(1, limit + 1):
    print(str(number) * number)

for number in range(limit - 1, 0, -1):
    print(str(number) * number)

peak_numbers = list(range(1, limit + 1))

reversed_numbers = peak_numbers[::-1]
print("\nPart C: Slicing Demonstration")
print(f"Peak numbers: {peak_numbers}")
print(f"Reversed numbers: {reversed_numbers}")