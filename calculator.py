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
# print "Calculator"
# number1=input('enter the first number: ')
# number2=input('enter the second number: ')
# print'The sum is ........',number1+number2
# print'The difference is..',number1-number2
# print'The quotient is....',number1/number2
# print'The product is.....',number1*number2

