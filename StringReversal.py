#Normal slicing string reversal

#get the input or make hard code variable
s1 = input("Please enter some text : ")
#s2 = "Hello, World!"

print(s1[::-1])

#with loop 

#get the string len
l1 = len(s1)
for i in range(len(s1)):
	#print last to first elemenr
	print(s1[l1-1], end="")
	#reduce len each time
	l1 = l1-1
print("\n")
