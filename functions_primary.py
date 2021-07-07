# author:Layla
# date:7/72021


# --------------- Section 1 --------------- #

# 1 | Exploring Built-in Functions
#
# Visit this documentation:
#   - https://www.w3schools.com/python/python_ref_functions.asp
#   - https://docs.python.org/3/library/functions.html
#
# Using the documentation above of built in functions, complete the following operations:
#   1 - Print the absolute value of a negative number.
#   2 - Save the hexadecimal value of 21 to a variable. Print this variable while describing it.
#   3 - Print the id of the variable holding the hexadecimal value of 21.
#   4 - Print 2 ^ 5 using the function instead of **.
#   5 - Print the number 3.75123 after being rounded to the nearest integer.
#   6 - Get the length of your full name by adding the length of first and last name together. Print it.
#
# Hint: REMEMBER, functions are typically named after verbs or nouns. Notice that the main action for a lot of tasks is
# to print, a verb, that is also the name of the function print. Think about what is being asked of you and that should
# help you find the right function.
#
# 1 is done for you.

print('The absolute value of -15 is:', abs(-15)) #1
print('when you Converts 21 into its hexadecimal variable:', hex(21)) #2
print('the id of the variable holding the hexadecimal value of 21:', id(0x15)) #3
print('2*5:',pow(2,5)) #4
print('rounded to the nearest integer:', round(3.75123))  #5
pass
print('length of my name:', len('layla')+len('jones')) #6





# --------------- Section 2 --------------- #

# 1 | Function Definitions no Parameters
#
# Relevant Documentation:
#   - https://www.w3schools.com/python/python_functions.asp
#
# Define the following functions:
#   1 - Define a function that will print out your name.
#   2 - Define a function that will print out three animals that you like.
#   3 - Define a function that will print the three odd numbers.
#
# Calling the functions:
#   1 - Call each function once.
#
# WRITE CODE BELOW
def my_name():
    print('layla')


my_name()

def  animals_i_like():
    print('raccoon')
    print('red fox')
    print('anura')
animals_i_like()


def odd_numbers():
    print('9')
    print('11')
    print('7')

odd_numbers()

#2 | Function Definitions with Parameters
#
# Relevant Documentation:
#   - https://www.w3schools.com/python/python_functions.asp
#
# Define the following functions:
#   1 - Define a function that will print out the cube of a number.
#       a. Parameters:
#           Name | Type(s)         | Description
#           num  | Integer / Float | The number to be cubed.
#   2 - Define a function that will print the sum of three numbers.
#       a. Parameters:
#           Name | Type(s)         | Description
#           a    | Integer / Float | A number. Will be added with b and c to find the sum.
#           b    | Integer / Float | A number. Will be added with a and c to find the sum.
#           c    | Integer / Float | A number. Will be added with a and b to find the sum.
#   3 - Define a function that will return a string duplicated five times.
#       a. Parameters
#           Name | Type(s)| Description
#           text | String | The text to be duplicated.
#
# Calling the functions:
#   1 - Call each function once.
#   2 - For the 3rd function, save the return value to a variable and print it.
#
# WRITE CODE BELOW
def cube_number(t):
    cube= t**3
    print(cube)
cube_number(23)


def sum_of_three_num(t,r,k):
    sum= t+r+k
    print(sum)


def string_dup(e):
    dup=e*5
    return dup


fogboy=('%')
print(string_dup('%'))
