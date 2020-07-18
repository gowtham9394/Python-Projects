#Simple calculator

#Function for addition
def add(x, y):
    return x + y

#Function for substraction
def sub(x, y):
    return x - y

#Function for the mutiplcation
def Multiply(x, y):
    return x * y

#Function for the division
def Divide(x, y):
    return x / y

print("Select your Operation")
print("1. Add")
print("2. Sub")
print("3. Multiply")
print("4. Divide")

while True:
    #User input for the operation
    choice = input("Enter your Operation (Example:1/2/3/4)")

    #checks the choice operation
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if choice == "1":
            print(add(num1, num2))
        if choice == "2":
            print(sub (num1, num2))
        if choice == "3":
            print(Multiply(num1, num2))
        if choice == "4":
            print(Divide(num1, num2))
        break
    else:
        print ("Please Enter valid input")
