# **NO AI USED**
# File: duncanDoyon_ATM.py
# Author: Duncan Doyon
# Date: 10/13/2026
# Section: Homework 3
# E-mail: duncan.doyon@maine.edu
# Description:
# A simulation many diffrent looping methods

# Starting balance and transaction history
balance = 1000
history = []

# Menu
choice = ""
while choice != "4":
    print("\n===== ATM MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Transaction History")
    print("4. Exit")
    choice = input("Choose an option: ")

# Deposit
    if choice == "1":
        amount = input("Enter deposit amount in whole dollars: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                balance += amount
                history.append(("Deposit", amount))
                print(f"Deposit successful: ${amount}")
                print(f"Current balance: ${balance:.2f}")
            else:
                print("Amount must be greater than zero.")
        else:
            print("Invalid amount. Enter whole dollars only.")

# Withdraw
    elif choice == "2":
        amount = input("Enter withdrawal amount in whole dollars: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    history.append(("Withdrawal", amount))
                    print(f"Withdrawal successful: ${amount}")
                    print(f"Current balance: ${balance:.2f}")
                else:
                    print("Insufficient funds.")
            else:
                print("Amount must be greater than zero.")
        else:
            print("Invalid amount. Enter whole dollars only.")

# Transaction history
    elif choice == "3":
        print("\n===== TRANSACTION HISTORY =====")
        print(f"Current Balance:\t${balance:.2f}\n")
        if len(history) == 0:
            print("No transactions yet.")
        else:
            for transaction in history:
                print(f"{transaction[0]}:\t${transaction[1]}\n")

# Exit
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")

# Invalid menu selection
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")