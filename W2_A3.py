
# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
number1 = raw_input("Enter an number: ")
number2 = raw_input("Enter an number greater than 1000: ")
adjective1 = raw_input("Enter one more adjective: ")
color1 = raw_input("Enter one color: ")
color2 = raw_input("Enter one color: ")
color3 = raw_input("Enter one color: ")
color4 = raw_input("Enter one color: ")
object1 = raw_input("Enter one more adjective: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!


story = "Welcome to children's playground. There are " + number1 + " lollipops here and " + number2 " bubbles." \
"There also are " + adjective1 + "candies. " + color1 + " " + color2 + " " colo3 + " " colo4 + ". " \
"The candies rolled into a rainbow. There is a group of " + object1 + " running on the rainbow bridge. " 



# finally we print the story
print (story)