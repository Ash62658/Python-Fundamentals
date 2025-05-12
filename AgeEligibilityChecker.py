#Age Eligibility Checker
#since single test so no loop

#Get the age as integer 
age = int(input("Please enter your age for the form : "))

#check for negative ages
if(age < 0):
	print("Sorry! You haven't been born yet")
#check age for under age 
elif(age < 18):
	print("You are underage for this role")
#check for Eligible age
elif(age < 60):
	print("You are eligible for this role congrats")
#check for Over age
else:
	print("Sorry! You are overaged")
