for iterator in range(22):
    print(iterator)
    #dont need to update the iterator

for letter in "hello world":
    print(letter, end= "")
print()

print(list(range(1, 10, 2)))
print(list(range(2,10,2)))
print(list(range(10, 0 ,-1)))

name = "nidoSNOW"
print(name.upper())
print(name.lower())
print(name.capitalize())

mylist = input("enter a range of numbers").split(",")
print(mylist)

#1 Taxes per age
TAX_ZERO = 0
TAX_FIFTEEN = 0.15
TAX_TWENTYFIVE = 0.25

age = int(input("enter your age: "))
annual_income = int(input("what is your income: "))

if  age <= 0:
    print(annual_income)
elif age <= 25:
    print(annual_income * TAX_FIFTEEN)
elif age <= 180:
    print(annual_income * TAX_TWENTYFIVE)
else:
    print("didnt work")

# Combining Logic Structures and Loops
sentinal = False
num = ""
while sentinal == False:
    if num = int(input("please guess a number from 1 to 10: "))
        if num == 5:
            sentinal = True
            if sentinal = True
                 print("it worked")