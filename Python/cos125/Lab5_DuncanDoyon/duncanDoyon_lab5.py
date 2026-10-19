#1) Expression Evaluation & Precedence
#
val1 = 30 / 3 // 3.0
# 30 / 3 = 10 // 3.0 = 3.33 floor it (round down)
# val1 = 3.0
val2 = (2 ** 4) + (8 % 3)
# 2 ** 4 is = to 4 * 4 = 16, 8 % 3 = 6, 8 - 6 = 2, 16 + 2 = 18
# val2 = 18
val3 = (7 // 2) + (44 % 3)
# 7//2 = 3.0, 44 % 3 = 42, 42 - 44 = 2
#val3 = 5

#Question: What data type did val1 result in, and why did the division operator / influence the final
#type even though // was used? Write your answer in a comment.
#the reason why val1 was a float is because the operation had a float value in it
#the reason val3 was a intger becasuse all the operation values where inegers so no conversion was needed

print(val1)
print(val2)
print(val3)

#2) Nested Temperature Categorization

temp = float(input("what is temperature: "))
if temp <= 32:
    print("Water Freeze")
elif temp <= 212:
    print("water is liquid")
else:
    print("water boils at 212")