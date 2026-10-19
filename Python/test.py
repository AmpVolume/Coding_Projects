birthdays = {
    "Alice": "2000-05-14",
    "Bob": "1998-11-22",
    "Charlie": "2002-03-08",
    "Diana": "2001-07-19"
}

# Look up a birthday
name = input("Whose birthday do you want to find? ")

if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}.")
else:
    print("That person is not in the birthday dictionary.")