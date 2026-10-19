age = int(input("Enter yur age: "))

#Step 1
if age >= 21:
    print("You can buy alcohol.")
#Step 2
else:
    print("You cannot buy alcohol")

#Step 3
grade = float(input("what is your grade: "))

if grade <= 90: # debugged > to <=
    print("you got an A")
elif grade >= 80:
    print("you got a B")
elif grade >= 70:
    print("you got a C")
else:
    print("you failed")

#Step 4
#removed age = 25 as we have age = input
has_license = input("have a license? y/n: ")
if age >= 16:
    if has_license == "y":
        print("You can drive.")
    else:
        print("You cannot drive without a license.")
else:
    print("You are too young to drive.")

#Challenge 1: Even of Odd
number = int(input("enter an even number or odd number: "))
if number % 2 == 0:
    if number == 0:
        print(f"{number} is a zero")
    else:
        print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

#Challenge 2: Traffic Light Simulator
Color_light = str(input("what color is the light: "))

if Color_light == "green":
    print("go")
elif Color_light == "yellow":
    print("Caution")
elif Color_light == "red":
    print("stop")
else:
    print("please enter a color thats red yellow or green")
