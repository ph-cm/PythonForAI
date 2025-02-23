# Functions are operations we can perform on specific data types

#print() is a function
user_dict = {"Name":"Pedro", "Age":21, "Interests":["AI", "ML", "Music"]}

for i in user_dict.keys(): # "i" percorr the keys and we just print the values of the currently key
    print(i, ":", user_dict[i])
    
print("--------------------------------------------------")

#type() returns the datatype of the value
for i in user_dict.keys():
    print(i, ":", type(user_dict[i]))
    
print("--------------------------------------------------")

#Just for strings

#len() return the length of a variable
print(len(user_dict["Name"]))

#lowercases
print(user_dict["Name"].lower())

#uppercases
print(user_dict["Name"].upper())

#split = split into list based on a specific character sequence
print(user_dict["Name"].split("e"))

#replace() = replace a character sequence with another
print(user_dict["Name"].replace("P", "L"))

print("-------------------------------------------------")

#List methods
#Add an element to the end of a list
user_dict["Interests"].append("Entrepreneurship")
print(user_dict["Interests"])

#remove a specific element from a list
user_dict["Interests"].pop(0)
print(user_dict["Interests"])

#insert an element into a specific place in a list
user_dict["Interests"].insert(1, "AI")
print(user_dict["Interests"])

print("-------------------------------------------------")

#Dict methods
#Acessing the keys
print(user_dict.keys())

#Acessing dict values
print(user_dict.values())

#Acessing dict items
print(user_dict.items())

#Removing a key
user_dict.pop("Name")
print(user_dict.items())

#Adding a key
user_dict["Name"] = "Pedro"
print(user_dict.items())

print("------------------------------------------------")

#All of that functions are already included in python but we can create functions on our own
#Defining a function
def user_description(user_dict):
    """""
    Function to return a sentence {String} describing input user
    """""
    
    return f'{user_dict["Name"]} is {user_dict["Age"]} years old and is interested in {user_dict["Interests"]}'

description = user_description(user_dict)
print(description)

new_user_dict = {"Name":"Lucas", "Age": 32, "Interests":["Jokes", "Cassino", "ski"]}
print(user_description(new_user_dict))
#So this functions allow us to iterate more with differents input data

#Other custom function that count number of users interested in an arbitrary topic
def interested_user_counter(user_list, topic):
    """
    Function to count number of users interested in an arbitrary topic
    """
    count = 0
    
    for user in user_list:
        if topic in user["Interests"]:
            count = count + 1
    
    return count

#Define the user list
user_list = [user_dict, new_user_dict]
topic = "Jokes"

count = interested_user_counter(user_list, topic)
print(f"There are {count} users interested in {topic}")