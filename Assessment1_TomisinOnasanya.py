
# 2.	If you would need to count all of the capital letters in a file. How would you do it?
# # with open('my_file.txt') as fh:
# 	text = fh.read()
# 	YOUR CODE HERE

# 3.	Given any string, reverse it, so that it reads backwards, for example:  if the string is “Apple”, you get “'elppA”.

S = "orange"
print(S[::-1])

# 4. 	Write a function to find the longest word in the list of strings.
# Given [‘cat’, ‘horse’, ‘elephant’, ‘dog’] your function would return ‘elephant’
string = ["cat", "‘horse’", "‘elephant’", "‘dog’"]
string.sort(key=len)
print(string)
# print(string(len-1))
print(string[-1])
# for i in string:
 # print(sorted(string))
    # print(str(len(i)))
    # print(i)
#  list.append(len(i) + (i))
# print(sorted(list))
# print(list(len-1))

# 5.
#
# print("Please select operation -\n "
#
#   	"1. Add\n "
#
#   	"2. Subtract\n"
#
#   	"3. Multiply\n"
#
#   	"4. Divide\n")
#
#
# # Take input from the user
#
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))

number_2 = int(input("Enter second number: "))

if select == 1:
    print((number_1 + number_2 ))
elif select ==2:
    print(number_1 - number_2)
elif select ==3:
    print(number_1 * number_2)
elif select == 4:
    print(number_1 / number_2)
else:
    print("Please enter aa number from 1 to 4")