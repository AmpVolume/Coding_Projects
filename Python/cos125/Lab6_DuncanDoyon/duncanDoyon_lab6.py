myList = [[11,22,33,44], [21,313,41,51]]
print(myList[0])
print(myList[0][1])

myList2 = ['this', 'that', 'other', 'those', 'these']
print(myList2[1:4])

otherList = []
otherList.append('hi')
print(otherList)

sentence = "This is a sentence"
sentList = sentence.split(" ")
print(sentence)
print(sentList)

#1 Dataset Creation
positive_number = int(input("Enter the number of data points: "))
number_list = [ ]
for item in range(positive_number):
    number = int(input(f"enter integers values #{item + 1}: "))
    number_list.append(number)
print(number_list)

#2 Dataset Creation with Split
split_list = input("Enter number sepreated by a commas: ")
data_list = split_list.split( )
