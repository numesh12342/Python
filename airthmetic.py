#Basics airthmetic operations

#while loop for continiously asking for input
while(True):
    #Asking from user and storing input numbers
    num1=float(input("Enter the first number::"))
    num2=float(input("Enter the second number::"))

    #Addition of two numbers
    sum=float(num1+num2)
    print("The sum of the two numbers is =",sum)
    
    #subtraction of two numbers
    subtract=float(num1-num2)
    print("The subtraction of the two numbers is =",subtract)
    
    #multiplication of two numbers
    multiplication=float(num1*num2)
    print("The multiplication of the number is =",multiplication)

    #Division of two numbers
    Division=float(num1/num2)
    print("The division of the number is =",Division)
    
    #breaking the while loop
    back=str(input("Enter (back) to exit or hit 'enter' to continue:"))
    if back=="back":
        break