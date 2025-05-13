#Grade Calculator

from datetime import datetime


#function for grading
def GetGrade(n):
	if(n < 40):
		return "F"
	elif(n < 60):
		return "D"
	elif(n < 75):
		return "C"
	elif(n < 90):
		return "B"
	elif(n <= 100):
		return "A"
	else:
		print("Invalid score")
	

#Value error Handling Function
def VErrorHandle():
	while(True):
		try:
			n = int(input(" : "))
			return n
		except ValueError:
			print("Enter a Valid integer Value")


#Main Logic

#get the no. of subjects with error handling
while(True):
			print("How many subjects are there to calculate the grade for?")
			nos = VErrorHandle()
			if(nos>0):
				break


#Empty lists for subjects, marks and grades 
subject_list = []
marks_list = []
grade_list = []


#get the names of subjects
for i in range(nos):
	print(f"Enter the name of subject {i+1}", end = "")
	subject = input(" : ")
	subject_list.append(subject)



#get the marks for subjects 
for i in range(len(subject_list)):
	print(f"Enter marks for subject {subject_list[i]} between 0 to 100", end="")
	
	marks = VErrorHandle()
	#checks if its between 0 to 100
	while(marks < 0 or marks > 100):
		marks = int(input("Please enter marks between 0 to 100 : "))
		
	marks_list.append(marks)
	grade_list.append(GetGrade(marks))

#calculate average
average_score = sum(marks_list)/len(marks_list)

#print total marks
print(f"You total marks are {sum(marks_list)} / {100*nos}.")
print(f"You total average is {average_score:.2f}.")

#Print the grade based on Average Score
print("Your Grade is : ", end=" ")
OverallGrade = GetGrade(average_score)
print(OverallGrade)

#showing subject wise marks 
with open("GradeData.txt", "w") as f:
	f.write("***The Grade Calculator Save Data***")
	f.write(f"\nSaved on : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
	
	print("Your subject wise marks are :")
	f.write("\nYour subject wise marks are :")
	
	for s,m in zip(subject_list, marks_list):
		print(f"{s} : {m}")
		f.write(f"\n{s} : {m}")
		
	print("Your subject wise grades are :")
	f.write("\nYour subject wise grades are :")
	
	
	for s, g in zip(subject_list, grade_list):
		print(f"{s} : {g}")
		f.write(f"\n{s} : {g}")
	
	f.write(f"\nYour total marks : {sum(marks_list)} / {100*nos}")
	f.write(f"\nYour overall Grade : {OverallGrade}")
	f.write(f"\nYour average score : {average_score:.2f}")
