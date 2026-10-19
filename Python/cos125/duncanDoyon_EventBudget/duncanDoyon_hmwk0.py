#**NO AI USED**
# File: duncanDoyon_hmwk0.py
# Author: Duncan Doyon
# Date: 9/7/2026
# Section: Homework 0
# E-mail: duncan.doyon@maine.edu
# Description:
# A bugeting system that allows the user to input
# their budget and expenses and then calculates the remaining budget.
# Collaboration:
# Oliva Omensky

#input
attendees = int(input("how many attendees: "))
hours = int(input("how many hours: "))
venue = float(input("Venue Cost $: "))
food_beverages = float(input("Cost for both Food & Beverages $: "))
supplies_promotion = float(input("Cost of Supplies and Promotion $: "))

total_expenses = venue + food_beverages + supplies_promotion

#Proccess
Avg_per_attendee = total_expenses / attendees
food_beverages_percent = (food_beverages / total_expenses) * 100
cost_per_event_hour = (total_expenses / hours)
cost_per_attendee_per_hour = (total_expenses / hours / attendees)

print("\n") #\n and \t create indentations to create visual appeal

#output
print("=========Event Budget Calculator==========")
print("\nInputs")
print("\tNumber of Attendees:", attendees)
print("\tEvent Hours:", hours)
print("\tVenue Cost: $", venue)
print("\tFood & Beverage Cost: $", food_beverages)
print("\tSupplies & Promotion Cost: $", supplies_promotion)

print("\nResults")
print("\tTotal Event Cost: $", total_expenses)
print("\tAverage Cost Per Attendee: $", Avg_per_attendee)
print("\tFood & Beverage Percentage:", food_beverages_percent, "%")
print("\tCost Per Event Hour: $", cost_per_event_hour)
print("\tCost Per Attendee Per Hour: $", cost_per_attendee_per_hour)