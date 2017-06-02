print "Calculator"
#selecting operators
operation = raw_input("PLEASE SELECT OPERATOR - ADD,SUB,DIV,MULTIPLY - ")
#conditions
#addition
if operation == "ADD":
	number1 = int(raw_input("Enter first integer "))
	number2 = int(raw_input("Enter second integer "))
	print (number1 + number2)
#subtaction
elif operation == "SUB":
	number1 = int(raw_input("Enter first integer "))
	number2 = int(raw_input("Enter second integer "))
	print (number1 - number2)
#division
elif operation == "DIV":
	number1 = int(raw_input("Enter first integer "))
	number2 = int(raw_input("Enter second integer "))
	print (number1 / number2)
#multiplication
elif operation == "MULTIPLY":
	number1 = int(raw_input("Enter first integer "))
	number2 = int(raw_input("Enter second integer "))
	print (number1 * number2)

else:
	print "SYNTAX ERROR"



