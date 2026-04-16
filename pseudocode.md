

```python
FUNCTION Multiply(x, y)
    RETURN x * y
END FUNCTION

FUNCTION Add(x, y)
    RETURN x + y
END FUNCTION

FUNCTION Subtract(x, y)
    RETURN x - y
END FUNCTION

FUNCTION Divide(x, y)
    IF y = 0 THEN
        OUTPUT "Error: Cannot divide by zero"
    ELSE
        RETURN x / y
    END IF
END FUNCTION

FUNCTION Percent(x)
    RETURN x / 100
END FUNCTION

FUNCTION Square(x)
    RETURN x * x
END FUNCTION

FUNCTION SquareRoot(x)
    IF x < 0 THEN
        OUTPUT "Error: Invalid input"
    ELSE
        RETURN √x
    END IF
END FUNCTION

FUNCTION Sin(x)
    RETURN sine(x)
END FUNCTION

FUNCTION Cos(x)
    RETURN cosine(x)
END FUNCTION

FUNCTION Tan(x)
    RETURN tangent(x)
END FUNCTION

FUNCTION Factorial(x)
    IF x < 0 THEN
        OUTPUT "Error: Invalid input"
    ELSE IF x = 0 OR x = 1 THEN
        RETURN 1
    ELSE
        RETURN x * Factorial(x - 1)
    END IF
END FUNCTION
```

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
