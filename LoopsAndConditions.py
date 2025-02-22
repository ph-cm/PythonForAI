# Loops runs a code cell multiple times

#For loop:
#The index starts in 0
# So the logic is for an "support" variable called "i", the cell code will run it 5 times(limited by me)
for i in range(5):
    print(i) #it would print the i of the currently step so, if im on step 0, i = 0, if im of step 1, i = 1
             #in other languages, we needed to increment i in the end of the cell loop but here no

user_interests = ["AI", "Machine Learning", "Music"]

for i in user_interests:
    print(i) #it print all itens in the list
    
#To iterate with dictionaries
user_dict = {"Name":"Pedro", "Age":21, "Interest":["AI", "ML", "Eletronics"]}

for i in user_dict.keys(): #.keys will extract each key of the dictionary and allow us to iterate them like how we do on lists
    print(i, "=", user_dict[i]) #this will print all the keys and its corresponding values
    
#--------------------------------------------------------------------------------------------------------------------------------------#

#Conditions make the logic of the program

#If-else statements
# Check if some data is or not true or false

if user_dict["Age"] >= 18:
    print(f"{user_dict['Name']} is an Adult") #if the condition is true, the cell code will happen if not, this cell code dont run 
else:
    print(f"{user_dict['Name']} is not an adult") #if the condition is false this code will run it

#--------------------------------------------------------------------------------------------------------------------------------------#

#Combine all together
#Count the number of users interested in bread

user_list = [{"Name":"Pedro", "Age":21, "Interests":["AI", "ML", "Bread"]},
             {"Name":"Luis", "Age":15, "Interests":["Samba", "Music", "Bread"]}]

count = 0 #Support variable

for i in user_list:
    if "Bread" in i["Interests"]: #if i that is inside the user_list, contains the "Bread" run the cell
        count = count + 1 #updating the support variable
        
print(count, " users interested in bread")