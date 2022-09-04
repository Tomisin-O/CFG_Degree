import math
pow -- get error message 'pow is not defined'
from math import pow (pow is a built in function)
from math import ceil
ceil(0.6)

# import time class
from datetime import time
   t1= time(17, 40)
   # t1.hour = 17
#    t1.minuite = 40
# t1 second = 0

# striftime- tale string ad format into time
# dt =datetime.now()
dt.strftime('%Y %m %d')
dt.strftime('%Y -%m -%d')
from datetime import datetime, timedelta

FORMAT = '%Y-%m-%d'

print('Welcome to the Future. Please enter date you would like to go to the future of.')
user_dt = input(f'Please enter a date as {FORMAT}: ')
dt = datetime.strptime(user_dt, FORMAT)

def add_days(date_to_increment, num_days):
    return date_to_increment + timedelta(days=num_days)
FOR LOOP
number- is just a name/alias to each value thats in the loop
name to the number in each iteration of the loop
each time we go through value assigned to the name number which we can use in our block

range(10, 0, -1)
returns an iterable- something we iterate through/go through step by step

WHILE LOOP
# keeps going while something is true


def while_counter(maximum):
    counter = 0

    while counter <= maximum:
        print('My new favourite number is...')
        print(counter)
        counter += 1

    print('My loop is over 😍')

# loops while thst bolleon expression is true indented block of code is run
# key word e.g example and conditions colon
#     indented block
# non indented block when condition is no longer met and loop is done/ when indent is overf

def for_counter(n):
    for num in range(n):
        print(f'my number is {num + 1}')

    print('My loop is over 😍')

while_counter(5)
for_counter(4)

def square(x):
    return x * x

def sum_two_squares(x, y):
    return (x * x) + (y * y)

def pythagoros(x, y):
    from math import sqrt
    sum_squares = sum_two_squares(x, y)
    return sqrt(sum_squares)

print(pythagoros(3, 4))

print('The following five days are: ')
for increment in range(1, 6):
    print(add_days(dt, increment))

The cheeky default dict in the first get() is so that is doesn't give you None as you'd then be trying to call .get() on None (which is an attributeerror)

A tuple is also generally thought of as a data structure where the order means something (e.g. (key, value) tuple from Dictionary.items()) or coordinates (x,y) etc. They
A list is more generally used when you need to contain a number of similar items or items of the same type.


print(len(game_scores))
print(max(game_scores))
print(min(game_scores))
for cost in costs:
total_cost += cost

