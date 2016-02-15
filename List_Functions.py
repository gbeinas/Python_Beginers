# --------- List Functions ----------------

# IN GENERAL LISTS ARE SIMILAR TO ARRAYS DATA STRUCTURES IN OTHER PROGRAMMING LANGUAGES

# In this tutorial we are going to learn about some very basic functions that can be used for list
#
# - add two lists  : + operation
# - size of a list : len
# - adda new item to the list : append
# - number of times an item appears to the list : count

shoppinglist = "eggs,milk,carrot,bread,sugar"
shoppinglist2 = ["eggs", "milk", "carrot", "bread", "sugar"]


# How to delete a list item

print("My list before the deletion :  " )
print shoppinglist2
del shoppinglist2[4]
print("My list after the deletion :  ")
print shoppinglist2

# How to add two lists - It is the same thing as to add two strings.The second array will be placed at the end
# of the first one. Let's see an example

print("The first array is : ")
array_1 = [1,3,5]
print array_1
print("The second array is : ")
array_2 = [4,6,8]
print array_2
array_3 = array_1 + array_2
print("The sum of array_1 and array_2 is : ")
print array_3
print (" ")


# To learn the size of my list, meaning how much item includes, I have to use the predefined function 'len'.
# Let's see an example of how to use this

print("The size of my list is : {0:d}".format(len(array_1)))

# How to use Max and Min functions. Returns the maximum and the minimum number within a list. Let's try it

print("The maximum number of the array_1 is : {0:d} and the minimum is : {1:d}".format((max(array_1)),min(array_1)))
print(" ")

# How to add an item to the list

print ("My list before adding an item is : " + str(shoppinglist2))
shoppinglist2.append("Brocoli")
print ("My list after adding an item is : " + str(shoppinglist2))
print(" ")

# How much times an item appears to a list. See the example below

print("My list consists of these items : " + str(shoppinglist2))
print(" ")
shoppinglist2.append("cacao")
shoppinglist2.append("cacao")
shoppinglist2.append("cacao")
shoppinglist2.append("orange")
shoppinglist2.append("orange")
shoppinglist2.append("orange")
shoppinglist2.append("orange")
shoppinglist2.append("orange")
shoppinglist2.append("banana")
shoppinglist2.append("orange")
print("My list now consists of these items : " + str(shoppinglist2))
print(" ")
print("How much times orange appears to my list ? Orange appears : {0:d} times".format(shoppinglist2.count("orange")))
print(" ")