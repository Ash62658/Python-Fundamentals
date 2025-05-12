#ODD or EVEN checker

#escape variable
esc = True
#get the number as integer

while (esc):
	n = int(input("Enter no. to check :"))
	#check even
	if(n%2==0):
		print(f"{n} is an Even no.")
	#if not even then Odd
	else:
		print(f"{n} is an Odd no.")
	esc = input("enter 0 to escape or enter anything to continue checking : ") != '0'
