#2. Write a program to input 2 numbers and one arithmetic operator. Perform operations as per arithmetic operator which is given as input

num1=int(input("enter number1 : "))
num2=int(input("enter number2 : "))
operation=(input("enter arithmatic operation : "))
if operation == '+':
    print("addition is ",num1+num2)
elif operation == '-' :
    print("substraction is ",num1-num2)
elif operation == '*':
    print("Multiplication is ",num1*num2)
elif operation == '/':
    print("Division is ",num1/num2)
    
    