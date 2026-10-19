phonebook = {
    "Alice": "207-555-0101",
    "Bob": "207-555-0102",
    "Charlie": "207-555-0103"
}

# Display the phonebook
print("Phonebook:")
for name, number in phonebook.items():
    print(f"{name}: {number}")

# Look up a contact
name = input("\nEnter a name to look up: ")

if name in phonebook:
    print(f"{name}'s phone number is {phonebook[name]}")
else:
    print("Contact not found.")

# Add a new contact
new_name = input("\nEnter a new contact name: ")
new_number = input("Enter their phone number: ")

phonebook[new_name] = new_number

print(f"{new_name} has been added to the phonebook.")

# Display the updated phonebook
print("\nUpdated Phonebook:")
for name, number in phonebook.items():
    print(f"{name}: {number}")