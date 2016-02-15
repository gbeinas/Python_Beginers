# --------- Dictionaries Functions ----------------

# In this tutorial we are going to learn about some very basic functions that can be used for dictionaries
#
# - delete all the keys and its values in a dictionary  : clear()
# - delete a whole dictionary : del
# - the length of a dictionary : len()
# - extract which are the keys of a dictionary : .keys()
# - extract which are the values of a dictionary : .keys()
# - add two dictionaries : update()

# How to delete all the keys and its values from a dictionary

dictionary = {"George":25, "Antwnis":24, "Dimitris":22, "Sofia":29}
print("My dictionary is : " + str(dictionary))
print("Now I will clear the dictionary ")
dictionary.clear()
print("Mi dictionary is : " + str(dictionary))
print(" ")

# How to delete a whole dictionary

dictionary = {"George":25, "Antwnis":24, "Dimitris":22, "Sofia":29}
print("Mi dictionary is : " + str(dictionary))
# del dictionary # Uncomment to delete the dictionary
print(" ")

# How to learn the length of a dictionary

print("The length of the dictionary is : {0:d}".format(len(dictionary)))
print(" ")

# How to extract all the keys within a dictionary

dictionary_keys  = dictionary.keys()
print("The keys of my dictionary are : " + str(dictionary_keys))
print(" ")

# How to extract all the values within a dictionary

dictionary_values = dictionary.values()
print("The values of my dictionary are : " + str(dictionary_values))
print(" ")

# How to add two dictionaries

dictionary_2 = {"Geor":25, "Antw":24, "Dim":22, "Sof":29}
dictionary.update(dictionary_2)
print("My new updated dictionary is : " + str(dictionary))
