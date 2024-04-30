#Question 1
#I am building some very high quality chairs and need exactly four nails for each chair. I've written a
#program to calculate how many nails I need to buy to build these chairs.
#chairs = '15'
#nails = 4
#total_nails = chairs * nails
#message = 'I need to buy {} nails'.format(total_nails)
#print('You need to buy {} nails'.format(message))
#When I run the program it tells me that I need to buy 15151515 nails. This seems like a lot of nails. Is
#my program calculating the total number of nails correctly? What is the problem? How do I fix it?

chairs = 15
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(message))

#Question 2
#I'm trying to run this program, but I get an error. What is the error telling me is wrong? How do I fix
#the program?
#my_name = Penelope
#my_age = 29
#message = 'My name is {} and I am {} years old'.format(my_name, my_age)
#print(message)

my_name = "Penelope"
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

#Question 3
#I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can
#make. Write a program to calculate this.
#Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be
#able to easily change these values if I want. The output should say something like "You can make 9
#omelettes with 6 boxes of eggs".

a_box_of_eggs = 6
number_of_omelettes = 9
egg_need_for_a_omelettes = 4
box_for_ommelettes = number_of_omelettes*egg_need_for_a_omelettes/a_box_of_eggs
box_for_ommelettes = int(box_for_ommelettes)
print("You can make 9 omelettes with 6 boxes of eggs")
print(f"You can make {number_of_omelettes} omelettes with {box_for_ommelettes} boxes of eggs")