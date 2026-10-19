#1 Print a Welcome Message
print("Welcome to the Rectangle Area Calculator!")
print(type("Welcome"))
#Question: What data type does the output indicate "Welcome" is?
#it indicates that wlecome is a string data type

print(42)
print(type(42))
#Question: What data type does print(type(42)) indicate 42 is?
#it indicates that 42 is an integer data type

print("42")
print(type("42"))
#Question: What would be the data type if 42 was wrapped in quotes?
#it indicatets that 42 is a string data type

#2 Get User Input
length = input("Enter the length of the rectangle: ")
print(type(length))

length = float(length)
print(type(length))

width = float(input("Enter the width of the rectangle: "))
print(type(width))

height = float(input("Enter the height of the rectangle: "))
print(type(height))

area = length * width
volume = length * width * height
print("The area of the rectangle is:", area)
print("The volume of the rectangle is:", volume)

#3 Variables and print()

fav_food = "hot dogs & lobster"
print("My favorite food is:", fav_food)

#4 Using the input() Function

age = input("How old are you? ")
print("I am", age, "years old.")

#5 Data Type Conversion and Expressions
sum1 = input("Enter the first number: ")
sum1 = int(sum1)
print(type(sum1))

sum2 = input("Enter the secound number: ")
sum2 = float(sum2)
print(type(sum2))

total = sum1 + sum2
print("The total is:", sum1, "+", sum2, "=", total)

#6 Mini-Challenge: Basic Math & Conversion

perimeter = (length + width) * 2
diagonal = (length ** 2 + width ** 2) ** 0.5
print("The length is:", length, "and the width is:", width, "so the perimeter is:", perimeter, "and the diagonal is:", diagonal)

#7 Causing an Error
print("The area of the rectangle is: ", + area)
print("First" + "Name")

value1 = 5
value2 = 5
print(value1, "+", value2, "=", value1 + value2)

#Question: What would "5" + "5" result in?
#it would result in "55" (string concatenation)