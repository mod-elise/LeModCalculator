listOfValidOperators ['*', '/']

FUNCTION multiply(x, y)
    RETURN x * y
END FUNCTION


FUNCTION addition(x, y)
    RETURN x + y
END FUNCTION


FUNCTION subtraction(x, y)
    RETURN x - y
END FUNCTION


FUNCTION percent(x)
    RETURN x / 100
END FUNCTION


FUNCTION square(x)
    RETURN x * x
END FUNCTION


FUNCTION squareRoot(x)
    IF x < 0 THEN
        OUTPUT "Error"
    ELSE
        RETURN √x
    END IF
END FUNCTION


FUNCTION sin(x)
    RETURN sine(x)
END FUNCTION


FUNCTION cos(x)
    RETURN cosine(x)
END FUNCTION


FUNCTION tan(x)
    RETURN tangent(x)
END FUNCTION


FUNCTION factorial(x)
    def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
END FUNCTION


function evaluator (string)
	lookInString:
		if countNumberOfValidOperators not 1:
			error
		else:		
			splitNumbersAndOperator:
				return numbers, operator

function validate (numbers, operator)

	if operator == '*' and thereAreTwoNumbers:
		return True, numbers, operator
	if operator == '+' and thereAreTwoNumbers:
		return True, numbers, operator
	if operator == '-' and thereAreTwoNumbers:
		return True, numbers, operator
	if operator == '/' and thereAreTwoNumbers:
		return True, numbers, operator
	if operator == '%' and thereIsOneNumber:
		return True, numbers, operator
	if operator == 'sqr' and thereIsOneNumber:
		return True, numbers, operator
	if operator == 'sqrRoot' and thereIsOneNumber:
		return True, numbers, operator
	if operator == 'sin' and thereIsOneNumber:
		return True, numbers, operator
	if operator == 'sqrRoot' and thereIsOneNumber:
		return True, numbers, operator 
	if operator == 'sqrRoot' and thereIsOneNumber:
		return True, numbers, operator 

	else: return False, numbers, operator

function calculate(inputText)
	numbers, operator = evaluateString(inputText)
	if validate(numbers {list}, operator)
		case '*': multiply (numbers)
		case '/': divide (numbers)
		case '+': add (numbers)
		case '-': subtract (numbers)
		case '%':  // TO BE DECIDED
		case 'sqr': square (numbers)
		case 'sqrRoot': squareRoot (numbers)
		case 'sin': sine (numbers)
		case 'cos': cosine (numbers)
		case 'tan': tangent (numbers)
		
		outputResult
	else:
		outputError


function input:
	useGraphicalInterfaceToCreateString
	or
	useTextInput
	calculate (inputText)