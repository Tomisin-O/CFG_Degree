# TASK 3
# Question 1
chairs = '15'
nails = 4
total_nails = int(chairs) * nails
message = 'I need to buy {} nails'.format(total_nails)
print(message)

# It is not calculating the total correctly because it is multiplying a string by an integer to give a repeating sequence
# of that string (the string is being repeated four times). To resolve this the string ('15')needs to be
# converted to an integer using the int function

# Question 2
my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

# What is the error telling me is wrong? How do I fix the program?
# The error is --- NameError: name 'Penelope' is not defined
# my_name's value (Penelope) is a string however it is not defined
# It needs to be wrapped in quotation marks

# Question 3
# I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make. Write a program to calculate this.
# Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be able to easily change these values if I want. The output should say something like:
# "You can make 9 omelettes with 6 boxes of eggs"

quantityOfBoxes =  input('How many boxes of eggs?')
eggsForomelettes = int(quantityOfBoxes) * 6
quantityOfOmelettes = eggsForomelettes / 4
print ('You can make {} omelettes with {} boxes of eggs'.format(quantityOfOmelettes , quantityOfBoxes))

#question 4
# Task 1 - Replace the (.) character with (!) instead. Output should be “I love coding!”

my_str = "I love coding."
print(my_str.replace(".", "!"))

# Task 2 - Reassign str so that all of its characters are lowercase.
my_str_1 = "EVERY Exercise Brings Me Closer to Completing my GOALS."
print(my_str_1.lower())

# Task 3 - Output whether this string starts with an A or not

my_str_2 = "We enjoy travelling"
ans_1 = my_str_2.startswith("A")
print(ans_1)
# output = False

# Task4 - What is the length of the given string?
my_str_3="1.458.001"
ans_2= len(my_str_3)
print(ans_2)
# length = 9

# Question 5
# Task 1 - Slice the word so that you get "thon".

wrd="Python"
sliced = slice(2, 6)
ans_1= wrd[sliced]
print(ans_1)

# Task 2 - Slice the word until "o". (Pyth)

wrd="Python"
ans_1= slice(4)
print(wrd[ans_1])

# Task 3 - Now try to get "th" only.

wrd="Python"
ans_1 = slice(2, -2)
print(wrd[ans_1])

# Task 4 - Now slice the word with steps of 2, excluding first and last characters
# result is ytho
wrd="Python"
step1=(wrd[:5])
# print(step1)
step2= (step1[1:])
print(step2)

# Question 6
# for number in range(100):
# 	output = 'o' * number
# 	print(output)

# The for loop allows us to iterate through all the numbers from 0 and up to 100 (0-99)
# 'O' the string is being multipled by the values from 0 to 99 and then printed
# 'O' is being multipled a total of 100 times in this function
# for each time 'O' is being multipled (100 times) the result is being printed,
# there are 99 results each with O being multipled from 0 too 99

# Question 7
# corrected version below:
def calculate_vat(amount):
	total= amount * 1.2
	return(total)
print(calculate_vat(100))

# What is wrong? How do you fix it?
# The function is  not returning anything so is automatically returning "None"
#  Ahe amount has not been assigned the value of 100
# total has not been assigned to equal : amount * 1.2
# the function is being called in the function incorrectly
# to fix it we return a value, set amount to 100 and total= amount * 1.2


# Question 8
# Write a new function to print a ‘cashier receipt’ output for a shop (any shop – clothes, food, events etc).
# It should accept 3 items, then sum them up and print out a detailed receipt with TOTAL.
myShop = {
  "burger": 10.99,
  "fries": 2.99,
  "milkshake": 5.99
}

for key, value in myShop.items():
    print(key, ':', value)
TOTAL = sum(myShop.values())
print(f"Total {TOTAL}")



