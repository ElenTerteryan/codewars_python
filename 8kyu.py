import numpy as np

#1###############################################################################################
# Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    new_numbers = []
    for num in numbers:
        new_numbers.append(num**2)
    return sum(new_numbers)
    
result = square_sum([1, 2, 3])
print(result)

#2###############################################################################################
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(i):
    a=""
    if i%2==0:
        a="Even"
    else:
        a="Odd"
    return a

result = even_or_odd(4)
print(result)

#3###############################################################################################
# Given 2 elevators (named "left" and "right") in a building with 3 floors (numbered 0 to 2), write a function elevator accepting 3 arguments (in order):
# left - The current floor of the left elevator
# right - The current floor of the right elevator
# call - The floor that called an elevator
# It should return the name of the elevator closest to the called floor ("left"/"right").
# In the case where both elevators are equally distant from the called floor, choose the elevator to the right.
# You can assume that the inputs will always be valid integers between 0-2.

def elevator(left,right,call):
    if abs(left-call)<abs(right-call):
        return "left"
    else:
        return "right"
        
result = elevator(4,4,1)
print(result)

#4###############################################################################################
# We need a function that can transform a number (integer) into a string.

def intstring(anynum):
    return str(anynum)

result = intstring(4)
print(result)

#5###############################################################################################
# You are given a string containing a sequence of character sequences separated by commas.
# Write a function which returns a new string containing the same character sequences except the first and the last ones but this time separated by spaces.
# If the input string is empty or the removal of the first and last items would cause the resulting string to be empty, return an empty value.

def array(mystring):
    if not mystring:
        return None
    items = mystring.split(',')
    return ' '.join(items[1:-1]) if len(items) > 2 else None

result = array("1,2,3,4,5")
print(result)

#6###############################################################################################
#Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

def sheep(somearray):
    keepcount = 0
    for i in somearray:
        if i is True:
            keepcount+=1
    return keepcount

result = sheep([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True])
print(result)

#7###############################################################################################
#Clock shows h hours, m minutes and s seconds after midnight.
#Your task is to write a function which returns the time since midnight in milliseconds.

def past(h, m, s):
    return s*1000+m*60*1000+h*60*60*1000

result = past(5,32,2)
print(result)

#8###############################################################################################
#Given a non-empty array of integers, return the result of multiplying the values together in order. 

def grow(arr):
    a = 1
    for i in sorted(arr):  
        a *= i
    return a

result = grow([1, 7, 8, 4]) 
print(result) 

#9###############################################################################################
# Build a function that returns an array of integers from n to 1 where n>0.
# Example : n=5 --> [5,4,3,2,1]

def reverse_seq(n):
    return list(range(n, 0, -1)) 

result = reverse_seq(6)
print(result)

#10###############################################################################################
#Write a function findNeedle() that takes an array full of junk but containing one "needle"
#After your function finds the needle it should return a message (as a string) that says:
#"found the needle at position " plus the index it found the needle, so:

def findNeedle(junksarr):
    for index,value in enumerate(junksarr):
        if value=="needle":
            return f'found the needle at position {index}'

result = findNeedle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"])
print(result)

#11###############################################################################################
# Find the mean (average) of a list of numbers in an array.

def find_average(nums):
    return average(nums) # with Numpy

def find_average(nums):
    return sum(nums) / len(nums)

result = find_average([1,2,3])
print(result)

#12###############################################################################################
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

def areYouPlayingBanjo(name):
    if name[0]=="R" or name[0]=="r":
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'
result = areYouPlayingBanjo("Rebecca")
print(result) 

#13###############################################################################################
# The Western Suburbs Croquet Club has two categories of membership, Senior and Open. 
# They would like your help with an application form that will tell prospective members which category they will be placed.
# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
# In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

def open_or_senior(data): # with dict 
    output=[]
    for key, value in data.items():
        if key>=55 and value>7:
            output.append("Senior")
        else:
            output.append("Open")
    return output

result = open_or_senior({58:8,25:9, 63:8, 55:8})

def open_or_senior(data): # with nested list 
    output=[]
    for pair in data:
        if pair[0]>=55 and pair[1]>7:
            output.append("Senior")
        else:
            output.append("Open")
    return output

result = open_or_senior([[58,8],[25,9], [63,8], [55,8]])

def openOrSenior(data): # with list comprehension
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

result = open_or_senior([[58,8],[25,9], [63,8], [55,8]])
print(result)


#14###############################################################################################
# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
# Otherwise, you can be sure he's not.

def friend(x):
    return [item for item in x if len(item)==4]
    
result = friend(["Ryan", "Kieran", "Jason", "Yous"])
print(result)


#15###############################################################################################
# Write a program that finds the summation of every number from 1 to num. 
# The number will always be a positive integer greater than 0. Your function only needs to return the result.

def summation(num):
    return sum([i for i in range(0,num+1)])

result=summation(7)

#16###############################################################################################
# Given a list of integers, determine whether the sum of its elements is odd or even.
# Give your answer as a string matching "odd" or "even".
# If the input array is empty consider it as: [0] (array with a zero).

def odd_or_even(arr):
    if sum(arr)%2==0:
        return "even" 
    else:
        return "odd"    
    
result = odd_or_even([0, 1, 4])
print(result)

#17###############################################################################################
# In this kata you will create a function that takes a list of non-negative integers and strings
# and returns a new list with the strings filtered out.
def filter_list(l):
    return [item for item in l if isinstance(item, int)]
    
result =filter_list([1,2,'aasf','1','123',123])
print(result)

#18###############################################################################################
# Code as fast as you can! You need to double the integer and return it.

def double_integer(i):
    return i*2

result= double_integer(2)
print(result)


#19###############################################################################################
# Create a function finalGrade, which calculates the final grade of a student depending on two parameters: 
# a grade for the exam and a number of completed projects.
# This function should take two arguments: exam - grade for exam (from 0 to 100); 
# projects - number of completed projects (from 0 and above);
# This function should return a number (final grade). There are four types of final grades:

# 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# 0, in other cases

def final_grade(exam, projects):
    if exam>90 or projects>10:
        return 100
    elif exam>75 and projects>=5:
        return 90
    elif exam >50 and projects>=2:
        return 75
    else:
        return 0
    
result = final_grade(76,10)
print(result)


#20###############################################################################################
# You get an array of numbers, return the sum of all of the positives ones.
def positive_sum(arr):
    return sum([i for i in arr if i>0])

result = positive_sum([1,2,5,-8,-2,0])
print(result)