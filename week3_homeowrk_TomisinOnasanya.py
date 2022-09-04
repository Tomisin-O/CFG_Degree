# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'
#

raining  = input('Is it raining? ')
if raining == 'y':
    print('Take an umbrella')
if raining == 'n':
    print("You don't need an umbrella")


# Question 2 corrected function:
my_money = input('How much money do you have? ')
boat_cost = 20 + 5

if int(my_money) >= boat_cost:
	print('You can afford the boat hire')

else :
	print('You cannot afford the board hire')

# The variable boat_cost is missing the underscore where it is first being declared
# This will lead to a syntax error as variables can not have spaces

# The print in the else statement has not been closed with a second closing bracket, it has been left open with only one bracket

# my money is a string and boat_cost is an integer, we can not use the comaprison operator (<)
# to compare a string with an intger. Need to convert the string to an integer: int(my_money) < boat_cost:

# The less than comaprison operator is used: (my_money) < boat_cost
# however to be able to afford the boat hire my money must be equal to or greater than the boat_cost
# The comparison operator greater than or equal to (>=) should be used

# Question 3
# Your friend works for an antique book shop that sells books between
# 1800 and 1950 and
# wants to quickly categorise books by the century and decade that they were written. Write a program that
# takes a year (e.g. 1872) and outputs the century and decade (e.g. "Eighteenth Century, Seventies")
# year = input('What is the year')
new_year = []
def yearfunction (year):
    if (year[:2]) == "18":
        new_year.append("Eighteenth Century")
    elif (year[:2]) == "19":
        new_year.append("Twentieth Century")

    if ((year[2:3])) == "1":
        new_year.append("Tens")
    elif ((year[2:3])) == "2":
         new_year.append("Twenties")
    elif ((year[2:3])) == "3":
        new_year.append("Thirties")
    elif ((year[2:3])) == "4":
        new_year.append("Fourties")
    elif ((year[2:3])) == "5":
        new_year.append("Fifties")
    elif ((year[2:3])) == "6":
        new_year.append("Sixties")
    elif ((year[2:3])) == "7":
        new_year.append("Seventies")
    elif ((year[2:3])) == "8":
        new_year.append("Eighties")
    elif ((year[2:3])) == "9":
        new_year.append("Ninety")
    return(new_year)

print(yearfunction("1800"))

# Task 2 question 1
shopping_list = [
	"oranges",
	"cat food",
	"sponge cake",
	"long-grain rice",
	"cheese board",
]
print(shopping_list[0])
# in a dictionary the values start from 0, so the first item would be position 0
# print(shopping_list[1]) is priniting the second item in the list,
# to get the first item it needs to be print(shopping_list[0])

#question2
chocolates = {

	'white': 1.50,

	'milk': 1.20,

	'dark': 1.80,

	'vegan': 2.00,

}

customer_choice = input('Choose your chocolate:')

for i in chocolates:
	if i == customer_choice:
		# print('true')
		print(chocolates[i])


# question3
Question 3
Write a program that simulates a lottery. The program should have a list of seven numbers that represent a lottery ticket.
It should then generate seven random numbers. After comparing the two sets of numbers,
the program should output a prize based on the number of matches:
·         £20 for three matching numbers
·         £40 for four matching numbers
·         £100 for five matching numbers
·         £10000 for six matching numbers
·         £1000000 for seven matching numbers

my_lottery_numbers = [2,5,6,7,8,9,22]
random_numbers = [2,5,67,22,55,66,99]
counter = 0
for i in i in my_lottery_numbers:
	if my_lottery_numbers(i) == random_numbers(i):
		counter+= 1


# # ·        What is the name of this API?
# Open trivia database
# ·        What does it do?
# questions that are contributed from different users qwith answers provided
API provides the questions and answers, we can decide how many questions, difficulity
can be used to create an open trivia game etc
#     Example URL to make a call to this API?
# https://opentdb.com/api.php?amount=2&category=9&difficulty=easy&type=multiple
#
# # my API OUTPUT
# {
# "response_code": 0,
# "results": [
# {
# "category": "General Knowledge",
# "type": "multiple",
# "difficulty": "easy",
# "question": "What does the &#039;S&#039; stand for in the abbreviation SIM, as in SIM card? ",
# "correct_answer": "Subscriber",
# "incorrect_answers": [
# "Single",
# "Secure",
# "Solid"
# ]
# },
# {
# "category": "General Knowledge",
# "type": "multiple",
# "difficulty": "easy",
# "question": "Foie gras is a French delicacy typically made from what part of a duck or goose?",
# "correct_answer": "Liver",
# "incorrect_answers": [
# "Heart",
# "Stomach",
# "Intestines"
# ]
# }
# ]
# }