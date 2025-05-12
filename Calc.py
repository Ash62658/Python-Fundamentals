esc = True

while (esc):
	
	x = float(input("Value x (first variable) : "))
	y = float(input("Value y (second variable) : "))
	op = input("Enter operator [ +, -, *, / , % ]")

	if(y == 0):
		print("Error division by zero")
		break
	match(op):
		case '+':
			print(x+y)
		case '-':
			print(x-y)
		case '*':
			print(x*y)
		case '/':
			print(x/y)
		case '%':
			print(x%y)
	esc = input("enter 0 for escape or enter anything to continue ") != '0'
