# Examples with Data Type : Strings

# Definition : Strings are amongst the most popular types in Python.
# We can create them simply by enclosing characters in quotes.
# Python treats single quotes the same as double quotes.
#  Creating strings is as simple as assigning a value to a variable.

# Define variables that are going to used next
FirstName = "George"
SecondName = "Beinas"
Age = 26

# Choose specific character within a String.Each string can be present as an array, which first character is placed
# at position 0 and last one at string's length. For example, let's say we have a string, "Hello". Based on above we
# have Hello[0] = H, Hello[1] = e and so on.

print FirstName[0]
print FirstName[1]
print FirstName[2]

# Now we are going to study what we will do if we want a specific range of characters within a String. This technique
# called string slicing. We are using the symbol ':'. Let's see an example on how to do this.

print FirstName[0:2] # this will print the first two characters of variable FirstName, i.e, Ge
print FirstName[0:4] # this will print the first two characters of variable FirstName, i.e, Geor

# print("Hello {0:s} {1:s} {2:d}".format(FirstName, SecondName, Age))

