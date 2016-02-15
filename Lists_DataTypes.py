# Examples with Data Type : Lists

# The list is a most versatile datatype available in Python which can be written as a list of comma-separated
# values (items) between square brackets.
# Important thing about a list is that items in a list need not be of the same type.
# Creating a list is as simple as putting different comma-separated values between square brackets.
#
# For example

# list1 = ['physics', 'chemistry', 1997, 2000];
# list2 = [1, 2, 3, 4, 5 ];
# list3 = ["a", "b", "c", "d"];

shoppinglist = "eggs,milk,carrot,bread,sugar"
shoppinglist

# A different, and more appropriate way, to define a list is using an array format.Let's see what do we mean exactly.
# The advantage of using an "array" way to define a list is that on this way you will be able to index a specific
# member of the list, e.g. the first, or the fifth.

# Let's see an example of list indexing

shoppinglist2 = ["eggs", "milk", "carrot", "bread", "sugar"]

print("The first element of my list is :  {0:s}".format(shoppinglist2[0]))
print(" ")
print("The second element of my list is : {0:s}".format(shoppinglist2[1]))
print(" ")
print("The fifth element of my list is : {0:s}".format(shoppinglist2[4]))
print(" ")

print("The first element of my list is {0:s} the second is {1:s} and the fifth element is {2:s}".format(shoppinglist2[0], shoppinglist2[1], shoppinglist2[4]))
print (" ")

# How to change the value of a list item

print("The first item of list before the change is :  {0:s}".format(shoppinglist2[0]))
shoppinglist2[0] = "onions"
print(" ")
print("The first item of list after the change is :  {0:s}".format(shoppinglist2[0]))