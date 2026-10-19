# **NO AI USED**
# File: duncanDoyon_hmwk2.py
# Author: Duncan Doyon
# Date: 9/29/2026
# Section: Homework 2
# E-mail: duncan.doyon@maine.edu
# Description:
# A simulation of dinning venues, and how students can interact with the
# varying price ranges and with a budget
# Collaboration:
# Oliva Omensky

#import as place holder
import random
#CONSTANTS
ZERO = 0
ONE = 1
FIVE = 5

#INPUTS
enter_name = str(input("Enter Student Or Falculty Name: "))
remaning_balance = float(input("Enter Starting Dining Balance ($): "))

#LIST            0        1        2        3
list_venue = ["Venue", "Venue", "Venue", "Venue"]
list_location = ["Student Union", "North Dining",
"Library Cafe", "South Bear Express"]

#1 Venue Directory
print("\nAvaliable Dining Venues:")
for i in range(len(list_venue)):
    print(f"{list_venue[i]} {i + ONE}: {list_location[i]}")

dining_spot = str(input("Enter Dinning Venue: "))

#2 Simulation Loop
print("\n===Starting Simulation===")
daily_expenses = []
day = ZERO

while remaning_balance >= FIVE:
    checkout_expense = random.randrange (800, 1601) / 100
    daily_expenses.append(checkout_expense)
    remaning_balance -= checkout_expense

    day += ONE

    print(f"Daily expense {day}: ${checkout_expense:.2f}")
    print(f"Remaining balance: ${remaning_balance:.2f}")
    print("====================")

if remaning_balance < FIVE:
    print("ALERT: Dining balance has fallen below $5.00!")
    print("===Ending Simulation===")

#3 Summary Calculations
total_spending = sum(daily_expenses)
average_daily_expense = total_spending / len(daily_expenses)

print(f"\n=== Summary Report for {enter_name} ===")
print(f"Total Days Simulated: {len(daily_expenses)}")
print(f"Dining Spot: {dining_spot}")
print(f"Total Spent: ${total_spending:.2f}")
print(f"Average Daily Expense: ${average_daily_expense:.2f}")

main_list = [
    "aspen", [1, 2, 3],  # First nested list
    "maple", [4, 5, 6],  # Second nested list
    "oak", [7, 8, 9]     # Third nested list
]
