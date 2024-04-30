#for loop

for number in range(4): #0, 1, 2, 3
    print(number)

print("----")

for char in "hello": #h, e, l, l, o
    print(char)

print("----")

for pet in ["Lola", "Babybel", "Cheddar"]: #list
    print(pet)

"""
A for loop is used to iterate over sequences (a collection of items).
And not only just the sequences but any iterable object can also be traversed.
The execution will start and look for the first item in the sequence.
After executing the statements in the block, it will look for the next item and the process will continue until the the last item is reached.
"""

print("this is out side the loop")
print("loop starting")
for number in range(4):
    print("this is inside the loop")
    print(number)
    print("moving on")
print("loop finished")

print("this is out side the loop")
total =0
print("loop starting")
for number in range(4):
    print("this is inside the loop")
    print(number)
    total = total +1
    print("moving on")
print("loop finished")
print(f"after loop, total is {total}")

#while loop
"""
WHILE loop
In case of a while loop a user does not know beforehand how many iterations are going to take place.
Beware of infinite while loops - they execute infinite times i we don't specify correct condition
If the loop is running infinitely and never stops, we would 'blow' our memory usage and the program would encounter an error.

example: 
due to social distancing, only 10 ppl are allowed to be inside a shop at the same time
this program invites ppl in the queue to come in while we have some capacity
"""

store_capacity = 5
while store_capacity >0:
    print(f"please come in, we have {store_capacity} space available")
    store_capacity = store_capacity - 1
    print(store_capacity)
print("sotre full, please wait for someone to leave")


print("-----")


#function
""" 
Function: is a reusable block of code that contains one or more Python statements and used for performing a specific task.
Why use function in Python?
1. Code re-usability: it is better to wrap 10 lines of code in a function and just call the function wherever needed, as opposed to writing those
10 identical lines every time you perform that task.
1. Improves Readability: By using functions for frequent tasks you make your code structured and readable.
1. Avoid redundancy: When you no longer repeat the same lines of code throughout the code and use functions in places of those, you
actually avoiding the redundancy that you may have created by not using functions.
"""

#def name(argument):
#    statement #do thins here
#    return value

def hello(name, language):
    print(f"hello {name}, we're learning {language}")

name = "k"
language = "python"
hello(name, language)

hello(language, name)

hello(language=language, name=name) #keyword arguement

#def hello(name1, language = "french"): #default arguement


def sum(x,y):
    return(x+y)
result = sum(10,5)

print(f"our result is {result}")

#Exercise 2.6: Complete the function to return the area of a circle
#use the comments to help you

def circle_area(radius): #add the radius argument inside the brackets
    area =3.14 * (radius ** 2)
    return(area)         #add return statement

circle_1 = circle_area(10)
print(circle_1)


print("----")

def times_two(number):
    result = number *2
    return(result)

for number in range(3): #0, 1, 2
    calculate_res = times_two(number)
    print(calculate_res)

#modules

#import <name of module>
#from <name of module> import <specific package name>

"""
math
datetime: date and time value manipulation 
timeit : time the execution of small blocks of python code 
re- :regular expression(pattern search )
copy    : duplicating objects 
"""

import datetime

x = datetime.datetime.now()
print(x)




