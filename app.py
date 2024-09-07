#Exercise 1: Variable Assignment and String Manipulation
#Write a program that asks the user for their name and age, then prints a greeting message using string formatting.
print("Exercise 1: Variable Assignment and String Manipulation")

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print("Hello " + user_name + ". I hear you are " + user_age + " years old.")

#user_name = input("Enter your name: ")
#user_age = int(input("Enter your age: "))
#print(f"Hello {user_name}. I hear you are {user_age} years old.")

print("*****************************************************************************************************************************")

#Exercise 2: Basic Arithmetic and User Input
#Create a simple calculator that takes two numbers as input and performs addition, subtraction, multiplication, and division.
print("Exercise 2: Basic Arithmetic and User Input")
print("Hello, this is a simple caculator")

first_number = float(input("Enter a first number: "))
second_number = float(input("Enter a second number: "))
response: float

print("Choose the operation you want to do: 1:ADD, 2:SUB, 3:MUL, 4:DIV.")
operation_id = int(input("Enter the number of your choice: "))

if operation_id == 1:
    response= first_number + second_number
    print(f"Result: {first_number} + {second_number} = {response}")
elif operation_id == 2:
    response = first_number - second_number
    print(f"Result: {first_number} - {second_number} = {response}")
elif operation_id == 3:
    response = first_number * second_number
    print(f"Result: {first_number} * {second_number} = {response}")
elif operation_id == 4:
    response = first_number / second_number
    print(f"Result: {first_number} / {second_number} = {response}")
else:
    print("You have not made a choice")

print("End of your operation. Thanks for using our calculator.")



