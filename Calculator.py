def add (num1 , num2):
    return num1 + num2
def sub (num1 , num2):
    return num1 - num2
def multiply (num1 , num2):
    return num1 * num2
def divide (num1 , num2):
    return num1 / num2 
def avg (num1 , num2):
    return (num1 + num2)/2
print ("Please select an operation:\n "\
        "1. Addition\n" \
       "2. Substraction\n" \
        "3. Multiply\n"\
              "4. Division\n" \
                "5. Average\n")
select = int(input("Select an operation from 1,2,3,4,5: "))
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
if select == 1:
    print ("Sum of two numbers is: " , add(number1, number2))
elif select == 2:
    print ("Substraction of two numbers is: " , sub(number1, number2))
elif select == 3:
    print ("Multiplication of two numbers is: " , multiply(number1, number2))
elif select == 4:
    print ("Division of two numbers is: " , divide(number1, number2))
elif select == 5:
    print ("Average of two numbers is: " , avg(number1, number2))
else:
    print("Invalid operation! Please select again")









