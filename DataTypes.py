#Python is a programming language used
# to give computers precise instructions
# to do things we dont want to do

# Data Types
# A way to classify data to process it appropriately

# Strings = characters = "Hello", 'hello "pedro"'

# Numbers
#     int = integer = 1, 12, 89;
#     Floats = numbers with decimals = 1.0, 96.4;
    
print("Hello im an String")
print("Im a integer number",  1) #you cant concatenate 2 different data types using "+" opp
print("Im a float number", 32.9)

# Lists = orderes collection of values
#     a list of strings
#         ["a", "b", "C"]
#     a list of ints
#         [1, 2, 3]
#     a list with a string, int and float
#         ["a", 2, 3.13]
#     a list of list
#         [["a", "b"], [1, 2], [2.0, 1.0]]

print("im a list ", [1, 2, 3])
print("im a list ", type([1, 2, 3]))

print("im not a list ", 1, 2, 3)
print("im not a list ", type(1), type(2), type(3))

# Dictionaries = key-values pair sequences similar to JSON file
#     a dictionary
#         {"Name" : "Pedro"}
#           Key      Value

#     a dictionary with multiple key-value pairs
#         {"Name":"Pedro", "Age":21, "Interests":["AI", "Music", "Sports"]}
    
#     a list of dictionary
#         [{"Name":"Pedro", "Age":21, "Interests":["AI", "Music", "Sports"]}
#          {"Name":"Luis", "Age":19, "Interests":["Golf", "show", "Beer"]}]
    
#     a nested dictionary
#         {"User":{"Name":"Pedro", "Age":21, "Interests":["AI", "Music", "Sports"]},
#         "Last_Login":"2024-07-12",
#         "Membership_Tier":"Free"}
