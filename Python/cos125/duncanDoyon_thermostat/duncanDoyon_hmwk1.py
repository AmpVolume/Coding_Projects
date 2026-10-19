##**AI COMPANION SADLY USED**
# File: duncanDoyon_hmwk1.py
# Author: Duncan Doyon
# Date: 9/16/2026
# Section: Homework 1
# E-mail: duncan.doyon@maine.edu
# Description:
# A software program that calculates smart home thermostat
# energy costs based on season, temperature, and peak hours.
# Collaboration: Olivia Omensky


# Constants
TEST_CASE = "I AM NOT WORKING HELP!"
SUMMER = "summer"
WINTER = "winter"

YES = "y"
NO = "n"

SUMMER_BASE_RATE = 4.00
WINTER_BASE_RATE = 3.50

SUMMER_TEMP = 70
WINTER_TEMP = 72

SUMMER_SURCHARGE = 1.50
WINTER_SURCHARGE = 1.25

PEAK_HOURS_PRICE = 1.00
PEAK_TEMP_ADJUSTMENT = 2

ZERO_COST = 0.00 #used zero in given cases gotta avoid magic numbers


# Inputs
user_name = str(input("What is your name?: "))
base_temp = float(input("What is your desired base temperature?: "))
seasons = str(input("What season is it?: ")).lower() #Change string to all lowercase
is_it_peak_hours = str(input("Is it peak hours y/n?: ")).lower() #Change string to all lowercase
budget = float(input("What is your energy budget ($)?: "))


# Processing
# Structure 1
if seasons == SUMMER:
    base_daily_cost = SUMMER_BASE_RATE
elif seasons == WINTER:
    base_daily_cost = WINTER_BASE_RATE
else:
    base_daily_cost = ZERO_COST

# Structure 2
if seasons == SUMMER or seasons == WINTER:
    base_rate = base_daily_cost
    seasonal_surcharge = ZERO_COST
    peak_hours_fee = ZERO_COST
    recommended_temp = base_temp
    if seasons == SUMMER:
        if base_temp < SUMMER_TEMP:
            seasonal_surcharge = SUMMER_SURCHARGE
            total_cost = (base_rate + seasonal_surcharge)
    elif seasons == WINTER:
        if base_temp > WINTER_TEMP:
            seasonal_surcharge = WINTER_SURCHARGE
            total_cost = (base_rate + seasonal_surcharge)
    else:
        print(TEST_CASE)

# Structure 3
    if is_it_peak_hours == YES:
        peak_hours_fee = PEAK_HOURS_PRICE
        total_cost = (total_cost + peak_hours_fee)
        if seasons == SUMMER:
            recommended_temp = (base_temp + PEAK_TEMP_ADJUSTMENT)
        elif seasons == WINTER:
            recommended_temp = (base_temp - PEAK_TEMP_ADJUSTMENT)
    elif is_it_peak_hours == NO:
        recommended_temp = base_temp
    else:
        print(TEST_CASE)

# Structure 4
    budget_difference = total_cost - budget
    if total_cost <= budget:
        budget_status = "within"
    else:
        budget_status = "over"

# Output

    print("========== SMART THERMOSTAT SUMMARY ==========")
    print(f"Hello, {user_name}.")
    print(f"Season: {seasons.capitalize()}")
    print(f"Base temperature: {base_temp}°F")
    if is_it_peak_hours == YES:
        print("Peak hours are active.")
        print(f"Recommended eco-temperature:{recommended_temp}°F")
    elif is_it_peak_hours == NO:
        print("Peak hours are not active.")
        print(f"Recommended temperature remains:{recommended_temp}°F")
    else:
        print("Invalid peak hours entry.")
    print(f"Base daily cost: ${base_daily_cost:.2f}")#.2f Rounds to 2 decimal places
    print(f"Seasonal surcharge: ${seasonal_surcharge:.2f}")#.2f Rounds to 2 decimal places
    print(f"Peak hours fee: ${peak_hours_fee:.2f}")#.2f Rounds to 2 decimal places
    print(f"Total projected daily cost: ${total_cost:.2f}")#.2f Rounds to 2 decimal places
    print(f"Daily energy budget: ${budget:.2f}")#.2f Rounds to 2 decimal places
    if budget_status == "within":
        print(f"Your projected cost is within budget by ${budget_difference:.2f}.")#.2f Rounds to 2 decimal places
    else:
        print(f"Your projected cost is over budget by ${budget_difference:.2f}.")#.2f Rounds to 2 decimal places
    print("===============================================")
else:
    print("Invalid season entered.")
    print("Please enter summer or winter and restart the program.")