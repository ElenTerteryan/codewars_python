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