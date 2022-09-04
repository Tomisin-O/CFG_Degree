today = input('What day is it? ')
is_monday = today.lower == 'Monday'
print('Today is Monday: {}'.format(is_monday))

day = 'Monday'
not day.title() === 'Monday'
# returns false due to the not

not (true or false)
# returns false

counter = 0
while not counter > 5:
        print(counter)
        counter +=1

# prints 0 1 2 3 4 5

# if expression is true run indented block of code if not true nothing runs

# only one if and else vut can have multiple eleifs
# each if creates a new if statement

random
# randit is inclusive of the two numbers given
# random.random generates a float between 0 and 1

# random.choice choose a value at random from an iterable/list
# random.shuffle shuffles the values from iterables

user_word = input('Enter a word: ')

reversed_word = word[::-1]
if reversed_word = word:
        print('True')
else:
        print('False')
# method two

def is_palindrome(word):
        if reversed_word == word:
                return('True')
        else:
                return('False')

#
def is_palindrome(word):
        return reversed_word == word

word = input('What is your word? ')
if is_palindrome(word.lower):
        print('congrats you have a palindrome')
else:
        print('better luck next time')