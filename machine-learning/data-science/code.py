# --------------
# Code starts here

# Create the lists 
class_1=["Geoffrey Hinton","Andrew Ng","Sebastian Raschka","Yoshua Bengio"]
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class=class_1+class_2
print(new_class)
# Append the list
new_class.append("peter warden")
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove("Carla Gentry")
# Print the list
print(new_class)


# Create the Dictionary
courses={"math":65,"english":70,"history":80,"french":70,"science":60}


# Slice the dict and stores  the all subjects marks in variable
maths=courses["math"]
english=courses["english"]
history=courses["history"]
french=courses["french"]
science=courses["science"]
# Store the all the subject in one variable `Total`
total=maths+english+history+french+science
# Print the total
print(total)
# Insert percentage formula
percentage=(total*100)/500
# Print the percentage
print(percentage)



# Create the Dictionary
mathematics={"geoffrey hinton":78,"andrew ng":95,"sebastian raschka":65,"yoshua benjio":50,"hilary mason":70,"corinna cortes":66,"peter warden":75}
topper=max(mathematics,key=mathematics.get)
print(topper)
# Given string
topper="andrew ng"

# Create variable first_name 
first_name=topper.split()[0]
# Create variable Last_name and store last two element in the list
Last_name=topper.split()[1]

# Concatenate the string
full_name=Last_name+" "+first_name
# print the full_name
print(full_name)
certificate_name=full_name.upper()
# print the name in upper case
print("is"+" "+certificate_name)

# Code ends here


