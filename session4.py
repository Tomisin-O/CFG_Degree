### DEMO 1 ###
"""
List values can be accessed using their index in square brackets
"""
​
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
print(student_names[2])
​
"""
List indexes start counting from 0
"""
​
# student_names = [
#     'Diedre',    # index 0
#     'Hank',      # index 1
#     'Helena',    # index 2
#     'Salome'     # index 3
# ]
#
# print(student_names[0])
​
"""
You can also set the values in lists using their indexes, similar to how you would set a variable- lists are mutatable
"""
# student_names = [
#     'Diedre',    # index 0
#     'Hank',      # index 1
#     'Helena',    # index 2
#     'Salome'     # index 3
# ]
#
# student_names[1] = 'Joshua' -- update hank to joshua
​
​
### EXERCISE 1 ###
"""
When I'm travelling in the winter I often forget to pack warm clothes. 
Let's write a program to help me to remember the right clothes.
​
The program should check if the first item in the clothes list is "shorts". 
If it is it should change the value to "warm coat".
"""
​
clothes = [
    "shorts",
    "shoes",
    "t-shirt",
]
​
'''
Example Solution
'''
# clothes = [
#     "shorts",
#     "shoes",
#     "t-shirt",
# ]
#
# if clothes[0] == 'shorts':
#     clothes[0] = 'warm coat'
#
# print(clothes)
​
​
### DEMO 2 ###
"""
Examples of list functions (NB: functions and methods are different!)
method is called on an object costs.sort() - cost is now modified and sorted

function produces a new list original list unchanged print(sorted(costs)) -return a new list- sorted is
unchanges
"""
​
costs = [1.2, 4.3, 2.0, 0.5]
​
print(len(costs))
print(max(costs))
print(min(costs))
#
print(sorted(costs))
print(list(reversed(costs)))
-- when using reverse have it changes the type-need to convert it back to a list
​
​
### EXERCISE 2 ###
"""
Make a list of game scores. Using list functions write code to output information of the scores in the following format:
​
    Number of scores: 10
    Highest score: 200
    Lowest score: 3
​
Extension: Output all of the scores in descending order
"""
game_scores = [10, 90, 30, 100, 150, 200, 3, 20, 60, 87]
print(len(game_scores))
print(max(game_scores))
print(min(game_scores))
​
print(list(reversed(sorted(game_scores))))
print(200 in game_scores) - print true as its a value in game scores
### DEMO 3 ###
"""
append() and in
​
You can check if an value is in a list using the IN operator. 
If the value is in the list it will result in True and False if it is not.
"""
student_name = input('Which student are you looking for? ')
​
students = [
    'Diedre', 'Hank', 'Helena', 'Salome',
]
​
if student_name in students:
    print('{} is in the class'.format(student_name))
else:
    print('{} is not in the class'.format(student_name))
​
"""
The .append() method is used to add items to a list / end(right side)
"""
​
students = [
    'Diedre', 'Hank', 'Helena', 'Salome',
]
student_name = input('What is the name of the new student? ')
​
students.append(student_name)
​
print(students)
​
​
### EXERCISE 3 ###
"""
Whenever I'm shopping and I buy some bread I always forget to buy butter. 
Create a list and if 'bread' is in the list, add 'butter' to the shopping list.
​
Try running the program with and without bread in the list to check that your program works.
​
Remember the in operator checks if an item is in a list and the .append() method adds an item to a list.
"""
shopping_list = [
    'bread',
    'cheese',
    'pop tarts',
    'carrots',
]
shopping_list_without_bread = [
    'cheese',
    'pop tarts',
    'carrots',
]
​
def add_butter(shopping_items):
    if 'bread' in shopping_items:
        shopping_items.append('butter')
    return shopping_items

print(add_butter(shopping_list_without_bread))
print(add_butter(shopping_list))
​
​
'''
Example solution
'''
# if 'bread' in shopping_list:
#     shopping_list.append('butter')
​
'''
To check if an item is not in a list
'''
fridge = [
    'cheese',
    'pizza',
    'coke',
]
​
if 'milk' not in fridge:
    print('You have no milk in the fridge')
​
​
### DEMO 4 ###
"""
Using lists and for loops together
"""
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
​
for student_name in student_names:
    print(student_name)
​
"""
Counting the total number of items in a list using a for loop
"""
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
count = 0
​
for student_name in student_names:
    # count = count + 1
    count += 1
​
print(count)
​
for index, student_name in enumerate(student_names):
    print(f"{student_name} is student number {index}")
enumerate joins index and value
​
### EXERCISE 4 ###
"""
I want to work out how much money I've spent on lunch this week. I've created a list of what I spent each day.
Write a program that uses a for loop to calculate the total cost
"""
​
costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0
​
'''
Example Solution
'''
# costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
# total_cost = 0
#
# for cost in costs:
#     total_cost = total_cost + cost
#   or total_cost += cost
# print(total_cost)
​
'''
There is an easier way to do the last program without a for loop. 
The sum() function can be used to add up all of the values in a list:
'''
# costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
# total = sum(costs)
#
# print(total)
​
​
### DEMO 5 ###
"""
Using FOR LOOP to create a new list
"""
​
new_list = []
​
for number in range(5):
    new_list.append(number)
​
print(new_list)
​
"""
Using LIST COMPREHENSION to create a new list
"""
new_list = [num for num in range(5)]
​
print(new_list)
​
'''
Another example:
Using FOR LOOP to create a new list filtering out some values
'''
new_list = []
​
for word in ['cat', 'dog', 'rat', 'cow']:
    if word != 'rat':
        new_list.append(word)
​
print(new_list)
​
'''
Using LIST COMPREHENSION to create a new list filtering out some values
'''
# new_list = [word for word in ['cat', 'dog', 'rat', 'cow'] if word != 'rat']
#
# print(new_list)
​
​
### EXERCISE 5 ###
"""
write a list comprehension expression to build a new list of EVEN numbers ONLY from range(5)
​
your sample output should be [0, 2, 4]
"""
​
# new_list = # your solution to be added here
​
'''
Example solution
'''
# new_list = [i for i in range(5) if i % 2 == 0]
#
# print(new_list)
​
​
### DEMO 6 ###
"""
Values in a dictionary are accessed using their keys
"""
person = {
    'name': 'Jessica',
    'age': 23,
    'height': 172
}
​
print(person['name'])
print(person.get('name'))  # to avoid KeyError if the key is not present in the dictionary, returns None by default
print(person.get('name', 'Jane Doe'))  # give a default value as the 2nd argument to .get() method
​
pets = {'puppies': 6, 'kittens': 10, 'turtles': 4}
pets['dolphins'] = 1
for key, value in pets.items():
    print(f"We have {value} {key}.")
​
​
### EXERCISE 6 ###
"""
 Print the values of name, post_code and street_number from the dictionary
"""
place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}
​
'''
Example solution
'''
​
# place = {
#     'name': 'The Anchor',
#     'post_code': 'E14 6HY',
#     'street_number': '54',
#     'location': {
#         'longitude': 127,
#         'latitude': 63,
#     }
# }
#
# print(place['name'])
# print(place['post_code'])
# print(place['street_number'])
​
​
'''
Extension: Print the values of longitude and latitude from the inner dictionary
'''
​
# Extension solution
​
print(place['location']['longitude'])
print(place['location']['latitude'])
# or
print(place.get('location', {}).get('longitude'))
#
#
# location = place['location']
#
# print(location['longitude'])
# print(location['latitude'])
​
​
### DEMO 7 ###
"""
Dictionaries in Lists --> Putting dictionaries inside a list is very common
"""
people = [
    {'name': 'Jessica', 'age': 23},
    {'name': 'Trisha', 'age': 24},
]
​
for person in people:
    print(person['name'])
    print(person['age'])
​
​
### EXERCISE 7 ###
"""
Using a for loop, output the values name, colour and price of each dictionary in the list
"""
fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]
​
'''
Example solution
'''
# fruits = [
#     {'name': 'apple', 'colour': 'red', 'price': 0.12},
#     {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
#     {'name': 'pear', 'colour': 'green', 'price': 0.19},
# ]
#
# for fruit in fruits:
#     print(fruit['name'])
#     print(fruit['colour'])
#     print(fruit['price'])
​
​
### DEMO 8 ###
"""
Random choice -- The choice() function in the random module returns a random item from a list
"""
import random
​
colours = ['red', 'green', 'blue']
chosen_colour = random.choice(colours)
​
print(chosen_colour)
​
​
### EXERCISE 8 ###
"""
Write a program to create a random name. 
You should have a list of random first-names and a list of last-names. 
Choose a random item from each and display the result.
​
Extension: Using list of verbs and a list of nouns, create randomised sentences
"""
​
### DEMO 9 ###
"""
Tuple examples
"""
​
# # Tuple cannot be changed
#
order = ('croissant', 'coffee', 'juice')
#
#
# # This throws an error
#
order.append('porridge')
#
#
# # Tuple behaves very similar to list
#
# order = ('croissant', 'coffee', 'juice')
#
print(order[1])
​
​
def give_tuple(a, b, c):  # example of when a function returns a tuple
    return a, b, c

a, b, c = give_tuple(0, 1, 2)
​
​
for item in order:
    print('Order item: ' + item)
​
​
### DEMO 10 ###
"""
Set examples
"""
​
my_set = {1, 2, 3, 4, 5, 'hi', 7}
​
​
# We can add new elements to a set
my_set = {1,2,3}
my_set.add(4)
print(my_set)
#
#
# # No duplicate values in Set -- Try adding a new value to a set if it is already there
# numbers = {1,2,3,4,5}
# numbers.add(3)
# print(numbers)
#
#
# # Convert a list to a set to remove duplicates
words = ['hi', 'potatoe', 'car', 'hi', 'hi', 'car']
result = set(words)
print(result)