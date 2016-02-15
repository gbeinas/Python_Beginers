# Examples with Data Type : Dictionaries

# Each key is separated from its value by a colon (:), the items are separated by commas,
# and the whole thing is enclosed in curly braces.
# An empty dictionary without any items is written with just two curly braces, like this: {}.

# Keys are unique within a dictionary while values may not be.
# The values of a dictionary can be of any type,
# but the keys must be of an immutable data type such as strings, numbers, or tuples.

# Let's see how is this work.

# Define a dictionary with its keys and its values.

diction_example = {"George":25,"Maria":24,"John":27,"Dimitris":26}
print("The value of key 'George' is : {0:d} ".format(diction_example["George"]))
print(" ")


# More than one entry per key not allowed.  Which means no duplicate key is allowed.
# When duplicate keys encountered during assignment, the last assignment wins. For example -

dictionary_1 = {"George":25,"Maria":24,"John":27,"George":26}
print("The value of key 'George' is : {0:d} ".format(dictionary_1["George"]))
print("")

# How to update the value of a key inside a dictionary

print("My dictionary before the update is : " + str(diction_example))
diction_example["Maria"] = 30
print("My dictionary after the update  is : " + str(diction_example))
print (" ")

# How to delete a key with its value from a dictionary

print("My dictionary before the delete is : " + str(diction_example))
del diction_example["Maria"]
print("My dictionary after the delete is : " + str(diction_example))
print (" ")
