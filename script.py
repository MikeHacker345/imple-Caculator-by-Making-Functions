''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''

# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")

Output

Select operation.
1.Add
2.Subtract
3.Multiply
4.Divide
Enter choice(1/2/3/4): 3
Enter first number: 15
Enter second number: 14
15 * 14 = 210

In this program, we ask the user to choose the desired operation. Options 1, 2, 3 and 4 are valid. Two numbers are taken and an if...elif...else branching is used to execute a particular section. User-defined functions add(), subtract(), multiply() and divide() evaluate respective operations.
Check out these related examples:

    Add Two Numbers
    Find the Largest Among Three Numbers
    Find LCM
    Find HCF or GCD
    Print all Prime Numbers in an Interval
    Print the Fibonacci sequence
    Find the Factorial of a Number
    Check if a Number is Positive, Negative or 0

Want to learn more Python for Data Science? Head over to DataCamp and try their free Python Tutorial
Related Examples
Display Powers of 2 Using Anonymous Function
Find Numbers Divisible by Another Number
Convert Decimal to Binary, Octal and Hexadecimal
Find ASCII Value of Character
Find HCF or GCD
Find LCM
Find Factors of Number
Receive the latest tutorial to improve your programming skills.
