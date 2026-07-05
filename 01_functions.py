# 1. Create a Simple Function,Write a function that prints:Welcome to Python Programming,Concepts: def, function call
def welcome_message():
    print("Welcome to Python Programming")      
welcome_message()

# 2. Function with Parameters,Write a function that accepts a person's name and prints:Hello, Jebisha!,Concepts: Parameters, arguments
def print_hello_message(name):
    print(f"Hello, {name}!")
print_hello_message("Jebisha")

# 3. Function with Return Value,Write a function that accepts two numbers and returns their sum,Concepts: return statement
def add_numbers(num1, num2):
    return num1 + num2  

result = add_numbers(5, 3)
print(result)

# 4. Arithmetic Calculator,Create four functions:add() subtract() multiply() divide() Call each function with two numbers and display the results.Concepts: Multiple functions, return values
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
print(add(5, 3))
print(subtract(5, 3))
print(multiply(5, 3))
print(divide(5, 3))

# 5. Even or Odd,Write a function that accepts a number and returns whether it is:Even or Odd
# Concepts: Parameters, conditions
def add_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
result=add_even(10)
print(result)

# 6. Factorial Function,Write a function to calculate the factorial of a number.Example:Input: 5,Output: 120
# Concepts: Functions, loops

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
result=factorial(10)
print(result)

# 7. Prime Number Function,Write a function to check whether a number is prime.Print:Prime Number,Not a Prime Number
# Concepts: Functions, loops, conditions
def prime_number(num):
    if num<=1:
        print("not a prime number")
    else:
        is_prime=True

        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break;
        if is_prime:
            print("prime")
        else:
            print("not prime")
result=prime_number(11)

# 8. Function with Default Arguments,Write a function to display employee details.Parameters:Name,Department (default = "IT"),Example:Name: John,Department: IT
# Concepts: Default arguments
def employee_detail(name,department="IT"):
    name=name
    department=department
    return name,department
print(employee_detail("jone","ai"))

# 9. Lambda Function,Write lambda functions to:Add two numbers,Find the square of a number,Print the results.
# Concepts: lambda
square=lambda a,b:a+b
print(square(10,29))
square = lambda x: x * x
print("Square:", square(7))

# 10. Mini Function Challenge,Create a menu-driven calculator using functions.Menu:1. Addition,2. Subtraction,3. Multiplication,4. Division,5. Exit
# Call the appropriate function based on the user's choice.

# Function for addition
def addition(a, b):
    return a + b

# Function for subtraction
def subtraction(a, b):
    return a - b

# Function for multiplication
def multiplication(a, b):
    return a * b

# Function for division
def division(a, b):
    if b == 0:
        return "Division by zero is not allowed!"
    return a / b

# Main program
while True:
    print("\n===== Calculator Menu =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Thank you for using the calculator!")
        break

    if choice >= 1 and choice <= 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = addition(num1, num2)
            print("Result:", result)

        elif choice == 2:
            result = subtraction(num1, num2)
            print("Result:", result)

        elif choice == 3:
            result = multiplication(num1, num2)
            print("Result:", result)

        elif choice == 4:
            result = division(num1, num2)
            print("Result:", result)

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
        


